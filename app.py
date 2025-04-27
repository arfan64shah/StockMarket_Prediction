# import required libraries
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# load the saved model
model = load('knn_model.joblib')

# title
st.title("Stock Market Prediction")
st.markdown('Predict **Trading Volume**')

# inputs
st.sidebar.header('Input Stock Prices')
open = st.sidebar.number_input('Open Price', min_value=0.0, value=0.9)
high = st.sidebar.number_input('High Price', min_value=0.0, value=0.9)
low = st.sidebar.number_input('Low Price', min_value=0.0, value=0.9)
close = st.sidebar.number_input('Closing Price', min_value=0.0, value=0.9)

# create a predict button and the use the model to provide output
if st.sidebar.button('Predict Volume'):

    # create a dataframe
    data = pd.DataFrame([[open, high, low, close]], columns=['Open', 'High', 'Low', 'Close'])

    # predict
    predict = model.predict(data)

    # display the output
    st.success(f"**Predicted Trading Volume:** {predict[0]:,.0f} shares")