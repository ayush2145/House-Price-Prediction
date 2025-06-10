import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.title("House Price Prediction App")

# Input fields
OverallQual = st.slider("Overall Quality", 1, 10, 5)
GrLivArea = st.number_input("Above Ground Living Area (sq ft)", value=1500)
GarageCars = st.slider("Garage Cars Capacity", 0, 5, 2)
TotalBsmtSF = st.number_input("Total Basement Area (sq ft)", value=800)
YearBuilt = st.number_input("Year Built", value=2000)
FullBath = st.slider("Number of Full Bathrooms", 0, 5, 2)
KitchenQual = st.selectbox("Kitchen Quality", ["Ex", "Gd", "TA", "Fa"])
LotFrontage = st.number_input("Lot Frontage", value=60)

# Encode KitchenQual
kitchen_map = {"Ex": 4, "Gd": 3, "TA": 2, "Fa": 1}
KitchenQual_encoded = kitchen_map[KitchenQual]

# Combine features
features = np.array([
    OverallQual, GrLivArea, GarageCars, TotalBsmtSF,
    YearBuilt, FullBath, KitchenQual_encoded, LotFrontage
]).reshape(1, -1)

if st.button("Predict Sale Price"):
    prediction = model.predict(features)
    st.success(f"Predicted Sale Price: ${round(prediction[0], 2)}")
