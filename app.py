import os
import json
import joblib
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('.', path)


# Load the model
try:
    model = joblib.load('model.pkl')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Load preprocessing parameters
with open('preprocessing.json', 'r') as f:
    preprocessing = json.load(f)

mappings = preprocessing['mappings']
scaler_mean = np.array(preprocessing['scaler_mean'])
scaler_scale = np.array(preprocessing['scaler_scale'])
features_list = preprocessing['features']

# Dataset medians for hidden fields — used when user doesn't provide them
HIDDEN_DEFAULTS = {
    'Avg_Temperature_C': 16.0,
    'Avg_Discharge_Rate_C': 1.51,
    'Internal_Resistance_Ohm': 0.0267,
}

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model not loaded'}), 500
    
    try:
        data = request.json
        
        # Prepare input data
        input_data = []
        for feature in features_list:
            val = data.get(feature)
            
            # Handle categorical encoding
            if feature in mappings:
                val_str = str(val) if val is not None else 'nan'
                encoded_val = mappings[feature].get(val_str, mappings[feature].get('nan', 0))
                input_data.append(encoded_val)
            else:
                # Use dataset median for hidden fields when not provided
                if val is None:
                    val = HIDDEN_DEFAULTS.get(feature, 0.0)
                input_data.append(float(val))
        
        # Convert to numpy array and scale
        input_array = np.array(input_data).reshape(1, -1)
        scaled_data = (input_array - scaler_mean) / scaler_scale
        
        # Prediction
        prediction = model.predict(scaled_data)[0]
        
        # Ensure status is a string (model returns ['Healthy'])
        status = str(prediction)
        
        return jsonify({
            'status': status,
            'feedback': f'Battery diagnostic complete. Current status: {status}'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/metadata', methods=['GET'])
def get_metadata():
    return jsonify({
        'car_models': [m for m in list(mappings['Car_Model'].keys()) if m.lower() != 'nan']
    })

if __name__ == '__main__':
    # Use the port assigned by the hosting provider (Render)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
