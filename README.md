# 🔒 AI-Powered Privacy Protection System

## Overview
This project is a **prototype demo** for detecting hidden cameras in changing rooms, hotels, and other private spaces.  
It uses a **mock AI model** (randomized detection) to simulate:
- Camera lens reflection detection
- RF signal anomaly detection

## Features
- Upload room images and get a "Safe" or "Suspicious Device Detected" result
- Simulated RF signal scanning
- Simple Streamlit web app interface

## Tech Stack
- Python
- Streamlit
- OpenCV (for image handling, not real detection in this mock)

## Run Locally
```bash
git clone https://github.com/your-username/AI-Privacy-Protection.git
cd AI-Privacy-Protection
pip install -r requirements.txt
streamlit run app.py
