import pickle
import streamlit as st

model1 = pickle(load("Area.pkl"))

def myf1():
    area = st.number_input("Enter the area: ")
    pred = st.button("Prediction")
   

if pred:
    op = model1.predict([[area]])
    st.write("Price of Area is: ",op)
    
   
myf1()
