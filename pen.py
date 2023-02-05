# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 18:55:26 2022

@author: sande
"""




import pandas as pd

import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open("sandeep_trained_model_pendrive.sav", 'rb'))


    
    

def main():
     # giving a title
    st.title('Pendrive Price Prediction')
    
    
    # getting the input data from the user
    
    
    Product_name = st.text_input('Product name')
    Model_name=st.text_input('Model_name')
    storage= st.text_input('storage')
    drive_type = st.text_input('drive_type')
    rating = st.text_input('rating')
    
    
    
    # code for Prediction
    price = ''
    
    # creating a button for Prediction
    
    if st.button('Predict Price'):
        
        price=loaded_model.predict(pd.DataFrame([[Product_name,Model_name,storage,drive_type,rating]],columns=["Product_name","Model_name" ,"storage" ,"drive_type", "rating"]))


        
    st.success(price)
    
    
    
if __name__ == '__main__':
    main()