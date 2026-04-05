# Live Link: https://svm-model-electric-vehicle-battery.vercel.app

# 🔋 EV Battery Health Predictor

A high-fidelity, cybernetic dashboard for predicting and monitoring Electric Vehicle battery degradation. This application uses a Support Vector Machine (SVM) machine learning model to analyze battery telemetry and provide actionable health insights.

## 🚀 Live Demo
- **Frontend (Vercel)**: `https://your-vercel-project.vercel.app`
- **Backend API (Render)**: `https://ev-battery-health.onrender.com`

## ✨ Features
- **Neural Diagnostic Engine**: Real-time SOH (State of Health) prediction using a trained SVM model.
- **Cybernetic UI/UX**: Immersive dark-mode interface with global particle animations and glass-morphism.
- **Interactive Analytics**: 
  - Dynamic Degradation Curves.
  - Fleet-wide Health Distribution (Doughnut charts with centered metrics).
  - Historical Scan Tracking.
- **Diagnostic History**: 
  - Rich reconstruction of previous scans.
  - CSV Export functionality.
- **Mobile Responsive**: Fully optimized for desktop and mobile diagnostics.

## 🛠️ Tech Stack
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (ES6+), Chart.js, FontAwesome.
- **Backend**: Python 3.10, Flask, Flask-CORS.
- **ML Engine**: Scikit-Learn (SVM), Joblib, NumPy, Pandas.
- **Deployment**: Vercel (Frontend), Render (Backend).

## 📦 Installation & Local Setup

### Prerequisites
- Python 3.9+
- Git

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/kpaswan9999-cp/SVM_Model_Electric-Vehicle-Battery-Degradation-Prediction.git
   cd SVM_Model_Electric-Vehicle-Battery-Degradation-Prediction
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the backend**:
   ```bash
   python app.py
   ```

4. **Launch the frontend**:
   Open `index.html` in your browser.

## 🚢 Deployment Guide

### Render (Backend)
1. Create a **Web Service** on Render.
2. Build Command: `pip install -r requirements.txt`
3. Start Command: `gunicorn app:app`

### Vercel (Frontend)
1. Connect your repository to Vercel.
2. Ensure `API_BASE_URL` in `script.js` matches your Render URL.
3. Deploy!

## 📜 License
This project is licensed under the MIT License.
