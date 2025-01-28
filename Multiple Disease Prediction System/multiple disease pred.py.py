# -*- coding: utf-8 -*-
"""
Created on Sat May  4 20:50:03 2024

@author: HARI PRASANTH
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open('C:/Users/HARI PRASANTH/Desktop/Multiple Disease Prediction System\savedmodel/diabetes_model.sav'))


heart_disease_model = pickle.load(open('C:/Users/HARI PRASANTH/Desktop/Multiple Disease Prediction System\savedmodel/heart_disease_model.sav'))

parkinsons_model = pickle.load(open('C:/Users/HARI PRASANTH/Desktop/Multiple Disease Prediction System\savedmodel/parkinsons_model.sav'))


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Prediction',
                            'Parkinsons Prediction'].
                           default_index = 0)