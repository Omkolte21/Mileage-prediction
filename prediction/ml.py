import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("LR.pkl","rb")
LR=pickle.load(pickle_in)

def predict_note_authentication(cylinder,displacement,horsepower,weight,modelyear,origin):
    new_mileage=LR.predict([[cylinder,displacement,horsepower,weight,modelyear,origin]])
    return new_mileage

def main():
    st.title("Vehicle Mileage Prediction App")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    
    cylinder = st.text_input("Cylinder")
    if not cylinder.isdigit():
        st.error("Please enter valid integer.")
        
    displacement = st.text_input("Displacement")
    if not displacement.replace(".", "").isdigit():
        st.error("Please enter valid integer.")
        
    horsepower = st.text_input("Horsepower")
    if not horsepower.replace(".", "").isdigit():
        st.error("Please enter a valid integer.")
        
    weight = st.text_input("Weight")
    if not weight.isdigit():
        st.error("Please enter a valid integer")
        
    modelyear = st.text_input("Model Year")
    if not modelyear.isdigit():
        st.error("Please enter a valid integer .")
        
    origin = st.selectbox("Origin", options=["1", "2", "3"])
    
    result=""
    if st.button("Predict"):
        result = predict_note_authentication(float(cylinder), float(displacement), float(horsepower), 
                                              int(weight), int(modelyear), int(origin))
    st.success('The Predicted Mileage is  {}'.format(result[0]))

if __name__=='__main__':
    main()
