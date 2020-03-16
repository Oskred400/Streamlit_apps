import sys

import os

#some ML code
#App to perform logistic regression
import numpy as np


from matplotlib import pyplot as plt
#sample streamlit app
#1. python scripting
#2. Use widgets as variables
#3.
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

import streamlit as stlit

#slider functionality

x_axis = stlit.slider('x')

x_val = np.arange(10).reshape(-1,1)
y_values = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

#write it's cube
#and cuberoot
stlit.write(x_axis,'cubed is', x_axis*x_axis*x_axis)
stlit.write(x_axis,'cube root is', x_axis ** (1/3) )

#port settings: default is 8501???
