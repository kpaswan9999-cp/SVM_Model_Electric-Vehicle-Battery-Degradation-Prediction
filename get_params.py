import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import json
import os

# Reproduce the notebook's preprocessing for 9 features
csv_path = r'c:\Users\kpasw\ML Prect\Models\SVM\ev_battery_degradation.csv'
df = pd.read_csv(csv_path)

# Notebook# Data cleaning to match notebook exactly
df['Avg_Temperature_C'] = pd.to_numeric(df['Avg_Temperature_C'], errors='coerce')
df['Car_Model'] = df['Car_Model'].astype(str)

# Fill NaNs as per notebook logic
categorical_cols_all = ["Car_Model", "Battery_Type", "Driving_Style"]
for col in categorical_cols_all:
    df[col].fillna(df[col].mode()[0], inplace=True)

df["Vehicle_Age_Months"].fillna(df["Vehicle_Age_Months"].median(), inplace=True)
df["Total_Charging_Cycles"].fillna(df["Total_Charging_Cycles"].median(), inplace=True)
df["Avg_Temperature_C"].fillna(df["Avg_Temperature_C"].median(), inplace=True)
df["Avg_Discharge_Rate_C"].fillna(df["Avg_Discharge_Rate_C"].median(), inplace=True)
df["Internal_Resistance_Ohm"].fillna(df["Internal_Resistance_Ohm"].median(), inplace=True)
df["SoH_Percent"].fillna(df["SoH_Percent"].median(), inplace=True)

# Step 5: Encode categorical columns (Reproducing notebook logic exactly)
label = LabelEncoder()
mappings = {}
for col in categorical_cols_all:
    df[col] = df[col].astype(str)
    df[col] = label.fit_transform(df[col])
    mapping = dict(zip(label.classes_, label.transform(label.classes_).tolist()))
    mappings[col] = mapping

# Step 6: Feature-Target Separation
# x=df.drop(columns=['Vehicle_ID','Battery_Type','Driving_Style','Battery_Status'])
x = df.drop(columns=['Vehicle_ID', 'Battery_Type', 'Driving_Style', 'Battery_Status', 'Unnamed: 13', 'Unnamed: 14'], errors='ignore')
y_col = "Battery_Status"
le_y = LabelEncoder()
df[y_col] = df[y_col].astype(str)
df[y_col] = le_y.fit_transform(df[y_col])
status_mapping = dict(zip(le_y.classes_, le_y.transform(le_y.classes_).tolist()))
mappings['Battery_Status'] = status_mapping

# Step 7: Scaling
scaler = StandardScaler()
scaler.fit(x)

# Output the parameters for preprocessing.json
preprocessing = {
    "mappings": mappings,
    "scaler_mean": scaler.mean_.tolist(),
    "scaler_scale": scaler.scale_.tolist(),
    "features": x.columns.tolist()
}

output_path = r'c:\Users\kpasw\ML Prect\Models\SVM\preprocessing.json'
with open(output_path, 'w') as f:
    json.dump(preprocessing, f)

print("Features Used (9):", x.columns.tolist())
print("Successfully generated preprocessing.json")
