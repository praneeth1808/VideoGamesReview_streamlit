import streamlit as st
import pandas as pd
import numpy as np


form = st.form(key='my-form')
name = form.text_input('Enter your name')
submit = form.form_submit_button('Submit')

st.write('Press submit to have your name printed below')

if submit:
    st.write(f'Hello {name}!')