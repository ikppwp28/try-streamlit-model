import streamlit as st
import pandas as pd
import pickle
import sklearn

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Streamlit app
st.title("Customer Churn Prediction")

# Input form for user
st.write("Enter customer information:")
number_vmail_messages = st.number_input("Number of Voicemail Messages")
total_intl_minutes = st.number_input("Total International Minutes")
total_intl_calls = st.number_input("Total International Calls")
total_intl_charge = st.number_input("Total International Charge")
total_net_minutes = st.number_input("Total Network Minutes")
total_net_calls = st.number_input("Total Network Calls")
total_net_charge = st.number_input("Total Network Charge")
number_customer_service_calls = st.number_input("Number of Customer Service Calls")
international_plan = st.radio("International Plan (Yes/No)", ['Yes', 'No'])
voice_mail_plan = st.radio("Voicemail Plan (Yes/No)", ['Yes', 'No'])
proporsi_churn = st.number_input("Proporsi Churn State")
loyal_customer = st.radio("Loyal Customer (Yes/No)", ['Yes','No'])

# Convert user inputs to DataFrame
input_data = pd.DataFrame({
    'number_vmail_messages': [number_vmail_messages],
    'total_intl_minutes': [total_intl_minutes],
    'total_intl_calls': [total_intl_calls],
    'total_intl_charge': [total_intl_charge],
    'total_net_minutes': [total_net_minutes],
    'total_net_calls': [total_net_calls],
    'total_net_charge': [total_net_charge],
    'number_customer_service_calls': [number_customer_service_calls],
    'international_plan': [1 if international_plan == 'Yes' else 0],
    'voice_mail_plan': [1 if voice_mail_plan == 'Yes' else 0],
    'proporsi_churn': [proporsi_churn],
    'loyal_customer': [1 if loyal_customer == 'No' else 0],
})

# Make prediction
prediction = loaded_model.predict(input_data)

# Display prediction result
if prediction[0] == 'Yes':
    st.write("The customer is likely to churn.")
else:
    st.write("The customer is not likely to churn.")

# Run the app
if __name__=='__main__':
    main()
