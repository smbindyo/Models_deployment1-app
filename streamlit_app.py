#import libraries
import streamlit as st
#tittle
st.title("Model1 deployment web app")
#header
st.header('Loan prediction web app')
#paragraph
st.write('This is a web app for loan predictions. This app takes user information and predicts his/her eligibility')
st.markdown('This is a test project')
#subheader
st.subheader('Data info')
st.write('some info on the data')
#linear equation
st.latex(r"y = \beta_0x_0+\beta_1x_1+\cdots\beta_nx_n+\epsilon")
#caption
st.caption('Linear regression1')
