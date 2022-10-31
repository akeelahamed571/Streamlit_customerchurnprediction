import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

model = pickle.load(open('customer_churn_model', 'rb'))
