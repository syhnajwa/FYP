import streamlit as st
import requests
import numpy as np
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_1pxqjqps.json")

font = "sans serif"
st.title("Child Obesity Risk Level Detection")
st.text("A system where you can check your child's risk of getting obesity! Check it out to know more.")
with st.container():
    st.write("---")
    left_column,right_column =st.columns(2)
    with left_column:
        st.header("What You Need to Know")
        (st.write('##'))
    content = '''<p style="font-size: 18px; text-align:justify">child obesity has been one of the most worrying topic in the world.Obesity is a complex disease that is characterized by an excess of body fat. Obesity is more than just a minor issue. It is a medical condition that raises the risk of developing other diseases and health concerns,
        such as heart disease, diabetes, hypertension, as well as certain cancers.
        An estimated 38.2 million children under the age of five were overweight or obese in 2019. Overweight and obesity, 
        once thought to be a problem only in high-income countries, are now on the rise in low- and middle-income countries, particularly in urban areas.</p>'''
    #)
    read_me = st.markdown(content, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

    st.sidebar.markdown("# Main page ")
    st.write("---")
    st.header("BMI Percentile")
    left_column,right_column =st.columns(2)
    with left_column:
        img= Image.open("bmiB.jpg")
        st.image(img)
        
    with right_column:
        img= Image.open("BMIG.jpg")
        st.image(img)
#image




