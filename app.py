import streamlit as st
import random
import cv2
import numpy as np

st.set_page_config(page_title="AI Privacy Protection System", page_icon="🔒")

st.title("🔒 AI-Powered Privacy Protection System")
st.write("Detect hidden cameras in changing rooms, hotels, and other sensitive spaces.")

# File uploader
uploaded_file = st.file_uploader("📷 Upload an image of the room", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display uploaded image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    st.image(img, channels="BGR", caption="Uploaded Room Image")

    # Mock detection (random outcome)
    result = random.choice(["Safe ✅", "Suspicious Device Detected 🚨"])
    explanation = (
        "No anomalies found in reflection or RF signals."
        if result == "Safe ✅"
        else "Possible hidden camera lens reflection detected near reflective surfaces."
    )

    st.subheader("🔎 Scan Result:")
    st.success(result) if "Safe" in result else st.error(result)
    st.write("📝 Explanation: ", explanation)

# Mock RF Signal Analysis
st.subheader("📡 RF Signal Analysis (Simulated)")
if st.button("Run RF Scan"):
    rf_result = random.choice(["No unusual RF signals detected ✅", 
                               "Unidentified RF signal detected 🚨"])
    st.write(rf_result)
