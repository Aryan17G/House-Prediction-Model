import streamlit as st 
import joblib
import numpy as np

model=joblib.load("model.pkl")
st.title("House Price Prediction App")
st.divider()
st.write("This Application uses machine Learning for predicting house price")
st.divider()
bedrooms= st.number_input("Number of Bedrooms",min_value =0, value=0)
bathrooms= st.number_input("Numbers of Bathrooms", min_value=0 , value=0)
livingarea= st.number_input("Living Area", min_value=0,value=3000)
condition=st.number_input("Condition",min_value=0,value=3)
numberofschool=st.number_input("Number of Schools nearby", min_value=0,value=0)
st.divider()

X=[[bedrooms,bathrooms,livingarea,condition,numberofschool]]

predictbutton=st.button("Predict")

if predictbutton:
    st.balloons
    X_array =np.array(X)
    prediction = model.predict(X_array)
    st.write(f"Price Prediction is {prediction}")

else:
    st.write("Please use predcit button after entering values")