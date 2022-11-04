import pickle
import streamlit as st
import numpy as np
import pandas as pd
X =pickle.load(open('X_new.pkl','rb'))
st.set_page_config(page_title='Car price prediction', page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("CAR PRICE PREDICTION")


pipe =pickle.load(open('pipe_new.pkl','rb'))
X_test =pickle.load(open('X_new.pkl','rb'))

col1, col2 = st.columns(2 ,gap="medium")
with col1:
    Brand=st.selectbox('Enter name of the model :',
    (np.sort(X['Brand'].unique())))
    z = X['Brand'] == Brand
    df_new = pd.DataFrame(X[z])

    Model=st.selectbox('Enter name of the model :',
    (np.sort(df_new['Model'].unique())))    

    Location=st.selectbox('Enter the location :',
    (np.sort(X['Location'].unique())))

    Year=st.number_input("Enter Year of Purchase :",min_value=1, step=1 , format ='%d')

with col2:
    Kilometers_Driven=st.number_input("Enter kilometers Driven :")
    Fuel_Type=st.selectbox('Enter Fuel Type :',
    (X['Fuel_Type'].unique()))
    Owner_Type=st.selectbox('Enter Owner Type :',
    (X['Owner_Type'].unique()))
    Engine=st.number_input("Enter Engine in (CC) :",min_value=1, step=1 , format ='%d')

Mileage=st.number_input("Enter Mileage :",min_value=1, step=1 , format ='%d')

def predict(Brand, Model,Location	,Year,	Kilometers_Driven	,Fuel_Type,	Owner_Type,	Engine,	Mileage):
      return pipe.predict(pd.DataFrame(columns=X_test.columns,data=np.array([Brand, Model, Location, Year, Kilometers_Driven, Fuel_Type, Owner_Type, Engine, Mileage]).reshape(1,9)))[0]

col11, col12,col13 = st.columns([1.5,1,1] ,gap="medium")

with col12:
    s = st.button("SUBMIT")

if (s) :
    st.markdown("<h1 style='color: orange;'><b>Expected Car Price:</b></h1>",unsafe_allow_html=True)
    ans = predict(Brand, Model, Location, Year, Kilometers_Driven, Fuel_Type, Owner_Type, Engine, Mileage)
    if(ans<-1000):
        ans = ans*(-10)
        ans = np.round(ans,2)
        st.markdown(f'<h3 style="color: orange;">\u20B9\t{ans}\tK</h3>',unsafe_allow_html=True)  
    elif(ans<0):
        ans = ans*(-1)
        ans = ans*(10000)
        ans = np.round(ans,2)
        st.markdown(f'<h3 style="color: orange;">\u20B9\t{ans}\tK</h3>',unsafe_allow_html=True)
    else:
        ans = np.round(ans,2)
        st.markdown(f'<h3 style="color: orange;">\u20B9\t{ans}\tL</h3>',unsafe_allow_html=True)

