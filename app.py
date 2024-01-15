import streamlit as st
import pickle
import numpy as np
import pandas as pd

model =  pickle.load(open('model.sav', 'rb'))

st.title("Diabetes Prediction System")
st.write("""### Please answer the questions below then click on the predict button""")
    
age_to_value = {
    '18 to 24': 1,
    '25 to 29': 2,
    '30 to 34': 3,
    '35 to 39': 4,
    '40 to 44': 5,
    '45 to 49': 6,
    '50 to 54': 7,
    '55 to 59': 8,
    '60 to 64': 9,
    '65 to 69': 10,
    '70 to 74': 11,
    '75 to 79': 12,
    '80 or older': 13,
}

hbp_to_value = {'No':0, 'Yes':1}
hc_to_value = {'No':0, 'Yes':1}
cc_to_value = {'No':0, 'Yes':1}
smoker_to_value = {'No':0, 'Yes':1}
stroke_to_value = {'No':0, 'Yes':1}
hda_to_value = {'No':0, 'Yes':1}
pa_to_value = {'No':0, 'Yes':1}
fruits_to_value = {'No':0, 'Yes':1}
veggies_to_value = {'No':0, 'Yes':1}
hac_to_value = {'No':0, 'Yes':1}
ahc_to_value = {'No':0, 'Yes':1}
ndc_to_value = {'No':0, 'Yes':1}
dw_to_value = {'No':0, 'Yes':1}
sex_to_value = {'Female':0, 'Male':1}

gh_to_value = {
    'Excellent': 1,
    'Very Good': 2,
    'Good': 3,
    'Fair': 4,
    'Poor': 5,
}
edu_to_value = {
    'Never Attended School': 1,
    'Elementary': 2,
    'Secondary': 3,
    'Diploma/Vocational/Foundation/Matriculation': 4,
    'Undergraduate Degree': 5,
    'Masters and Higher': 6,
}
inc_to_value = {
    'Less Than $10,000': 1,
    'Less than $15,000 ($10,000 to < $15,000)': 2,
    'Less than $20,000 ($15,000 to < $20,000)': 3,
    'Less than $25,000 ($20,000 to < $25,000)': 4,
    'Less than $35,000 ($25,000 to < $35,000)': 5,
    'Less than $50,000 ($35,000 to < $50,000)': 6,
    'Less than $75,000 ($50,000 to < $75,000)': 7,
    'Less than $100,000? ($75,000 to < $100,000)': 8,
    'Less than $150,000? ($100,000 to < $150,000)': 9,
    'Less than $200,000? ($150,000 to < $200,000)': 10,
    '$200,000 or more': 11,
}

def user_report():
    selected_hbp_name = st.selectbox("Do you have High Blood Pressure?:", list(hbp_to_value.keys()))
    selected_hbp_value = hbp_to_value[selected_hbp_name]

    selected_hc_name = st.selectbox("Do you have High Cholestrol?:", list(hc_to_value.keys()))
    selected_hc_value = hc_to_value[selected_hc_name]

    selected_cc_name = st.selectbox("Have you had a cholesterol check in 5 years?:", list(cc_to_value.keys()))
    selected_cc_value = cc_to_value[selected_cc_name]

    selected_bmi_value = st.slider("What is your current BMI:", 0,100,27)

    selected_smoker_name = st.selectbox("Have you smoked at least 100 cigarettes in your entire life?:", list(smoker_to_value.keys()))
    selected_smoker_value = smoker_to_value[selected_smoker_name]

    selected_stroke_name = st.selectbox("Have you ever had a stroke?:", list(stroke_to_value.keys()))
    selected_stroke_value = stroke_to_value[selected_stroke_name]

    selected_hda_name = st.selectbox("Have you ever had a heart attack or a heart disease (Coronary Heart Disease (CHD) or Myocardial Infarction (MI))?:", list(hda_to_value.keys()))
    selected_hda_value = hda_to_value[selected_hda_name]

    selected_pa_name = st.selectbox("Have you ever any physical activity in the past 30 days - not including your job:", list(pa_to_value.keys()))
    selected_pa_value = pa_to_value[selected_pa_name]

    selected_fruits_name = st.selectbox("Do you consume at least 1 fruit per day:", list(fruits_to_value.keys()))
    selected_fruits_value = fruits_to_value[selected_fruits_name]

    selected_veggies_name = st.selectbox("Do you consume at least 1 vegetable per day:", list(veggies_to_value.keys()))
    selected_veggies_value = veggies_to_value[selected_veggies_name]

    selected_hac_name = st.selectbox("Are you a heavy drinker (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week):", list(hac_to_value.keys()))
    selected_hac_value = hac_to_value[selected_hac_name]

    selected_ahc_name = st.selectbox("Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMO:", list(ahc_to_value.keys()))
    selected_ahc_value = ahc_to_value[selected_ahc_name]

    selected_ndc_name = st.selectbox("Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?:", list(ndc_to_value.keys()))
    selected_ndc_value = ndc_to_value[selected_ndc_name]

    selected_gh_name = st.selectbox("Would you say that in general your health is:", list(gh_to_value.keys()))
    selected_gh_value = gh_to_value[selected_gh_name]

    selected_mh_value = st.slider("Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?:", 0,30,0)

    selected_ph_value = st.slider("Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?:", 0,30,0)

    selected_dw_name = st.selectbox("Do you have serious difficulty walking or climbing stairs?:", list(dw_to_value.keys()))
    selected_dw_value = dw_to_value[selected_dw_name]

    selected_sex_name = st.selectbox("What is your gender:", list(sex_to_value.keys()))
    selected_sex_value = sex_to_value[selected_sex_name]

    selected_age_name = st.selectbox("Select Age Group:", list(age_to_value.keys()))
    selected_age_value = age_to_value[selected_age_name]

    selected_edu_name = st.selectbox("What is your highest level of education?:", list(edu_to_value.keys()))
    selected_edu_value = edu_to_value[selected_edu_name]

    selected_inc_name = st.selectbox("What is your household annual income?:", list(inc_to_value.keys()))
    selected_inc_value = inc_to_value[selected_inc_name]

    user_report_data = {
        'HighBP': selected_hbp_value,
        'HighChol': selected_hc_value,
        'CholCheck': selected_cc_value,
        'BMI': selected_bmi_value,
        'Smoker': selected_smoker_value,
        'Stroke': selected_stroke_value,
        'HeartDiseaseorAttack': selected_hda_value,
        'PhysActivity': selected_pa_value,
        'Fruits': selected_fruits_value,
        'Veggies': selected_veggies_value,
        'HvyAlcoholConsump': selected_hac_value,
        'AnyHealthcare': selected_ahc_value,
        'NoDocbcCost': selected_ndc_value,
        'GenHlth': selected_gh_value,
        'MentHlth': selected_mh_value,
        'PhysHlth': selected_ph_value,
        'DiffWalk': selected_dw_value,
        'Sex': selected_sex_value,
        'Age': selected_age_value,
        'Education': selected_edu_value,
        'Income': selected_inc_value
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

user_data = user_report()
st.subheader('The data entered by the user')
st.write(user_data)

def predict():
    diabetes = model.predict(user_data)[0]
    
    if diabetes == 0:
        st.success('You are not diabetic :thumbsup:')
    else:
        st.error('You are prediabetic or already are a diabetic :thumbsdown:')
    
st.button('Predict', on_click=predict)

