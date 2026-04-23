import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title("House Price Prediction App")

st.write("Enter the details below to predict house price:")

# User inputs
area = st.number_input("Area (in sq ft)", min_value=0)


# Predict button
if st.button("Predict Price"):
    # Convert inputs into array
    features = np.array([[area]])
    
    # Prediction
    prediction = model.predict(features)
    
    # Output
    st.success(f"Estimated House Price: ₹ {round(prediction[0], 2)}")