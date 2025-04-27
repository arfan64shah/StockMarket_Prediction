# import required libraries
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# load the saved model
model = load('knn_model.joblib')