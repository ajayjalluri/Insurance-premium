import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import base64


page = st.sidebar.selectbox("Select Activity", ["Introduction", "Analytics","Percentage Prediction",])

if page=="Introduction":
    st.header("Prediction of Insurance Premium Pay Defaulters")
    st.subheader("1 Your client is an Insurance company and they need your help in building a model to predict whether the policyholder (customer) will pay next premium on time or not..")

    st.subheader("2 An insurance policy is an arrangement by which a company undertakes to provide a guarantee of compensation for specified loss, damage, illness, or death in return for the payment of a specified premium. A premium is a sum of money that you pay regularly to an insurance company for this guarantee.")
    st.subheader("3 Building a model to predict whether a customer would make the premium payment can be extremely helpful for the company because it can then accordingly plan its communication strategy to reach out to those customers who are less likely to pay and convince them to continue making timely payment.")
    st.subheader("4 Now, in order to predict, whether the customer would pay the next premium or not, you have information about past premium payment history for the policyholders along with their demographics (age, monthly income, area type) and sourcing channel etc.")

    st.header("Features that depends on prediction of Policy payment")
    st.subheader("* Percentage of premium amount paid by cash or credit car")
    st.subheader("* Age in years of policy holder")
    st.subheader("* Monthly Income of policy holder in rupees")
    st.subheader("* Underwriting Score of the applicant at the time of application")
    st.subheader("* No of premiums late by 3 to 6 months")
    st.subheader('* No of premiums late by 6 to 12 months')
    st.subheader('* No of premiums late by more than 12 months')
    st.subheader("* Total premiums paid on time till now")
    st.subheader('* Area type of Residence ')
    st.subheader('* Sourcing channel for application ')


if page =="Percentage Prediction" :

    st.header("Prediction of Insurance Premium Pay Defaulters")
    st.subheader("Your client is an Insurance company and they need your help in building a model to predict whether the policyholder (customer) will pay next premium on time or not..")
    st.text(" \n")
    form = st.form(key='my_form2')

    x1 = form.text_input(label='Age in years of policy holder')
    form.text(" \n")
    x2 = form.text_input(label='Monthly Income of policy holder in rupees')
    form.text(" \n")
    x3 = form.text_input(label='Percentage of premium amount paid by cash or credit card')
    form.text(" \n")
    x4 = form.text_input(label='Underwriting Score of the applicant at the time of application')
    form.text(" \n")
    x5 = form.text_input(label='No of premiums late by 3 to 6 months')
    form.text(" \n")
    x6 = form.text_input(label='No of premiums late by 6 to 12 months')
    form.text(" \n")
    x7 = form.text_input(label='No of premiums late by more than 12 months')
    form.text(" \n")
    x8 = form.text_input(label ="Total premiums paid on time till now")
    form.text(" \n")
    x9 = form.selectbox('Area type of Residence ', ['Urban','Rural'], key=1)
    form.text(" \n")
    x10 = form.selectbox('Sourcing channel for application ', ['A','B',"C","D","E"], key=2)
    form.text(" \n")

    submit_button = form.form_submit_button(label='Predict Percentage')
    if submit_button:
        st.write(0.9)

#
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()
#
# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
#
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return
#
# set_png_as_page_bg('backgroung.png')
