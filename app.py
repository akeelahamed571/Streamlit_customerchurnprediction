import pickle
import streamlit as st
from streamlit_option_menu import option_menu

from sklearn import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics

# loading the saved models
model = pickle.load(open('customer_churn_model.sav', 'rb'))
file="WA_Fn-UseC_-Telco-Customer-Churn.csv"
df_1=pd.read_csv(file)
col=df_1['tenure']
q = ""
# sidebar for navigation
with st.sidebar:
    
	selected = option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],icons=['activity','heart','person'],default_index=0)
	# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
		    # page title
		    st.title('Diabetes Prediction using ML')
		    
		    
		    # getting the input data from the user
		    col1, col2, col3 = st.columns(3)
		    
		    with col1:
		        inputQuery1 = st.text_input('inputQuery1')
		        
		    with col2:
		        inputQuery2 = st.text_input('inputQuery2')
		    
		    with col3:
		        inputQuery3 = st.text_input('inputQuery3')
		    
		    with col1:
		        inputQuery4 = st.text_input('inputQuery4')
		    
		    with col2:
		        inputQuery5 = st.text_input('inputQuery5')
		    
		    with col3:
		        inputQuery6 = st.text_input('inputQuery6')
		    
		    with col1:
		        inputQuery7 = st.text_input('inputQuery7')
		    
		    with col2:
		        inputQuery8 = st.text_input('inputQuery8')

		    with col3:
		        inputQuery9 = st.text_input('inputQuery9')

		    with col1:
		        inputQuery10 = st.text_input('inputQuery10')
		    
		    with col2:
		        inputQuery11 = st.text_input('inputQuery11')

		    with col1:
		        inputQuery12 = st.text_input('inputQuery12')

		    with col2:
		        inputQuery13 = st.text_input('inputQuery13')
		    
		    with col3:
		        inputQuery14 = st.text_input('inputQuery14')

		    with col1:
		        inputQuery15 = st.text_input('inputQuery15')

		    with col2:
		        inputQuery16 = st.text_input('inputQuery16')
		    
		    with col3:
		        inputQuery17 = st.text_input('inputQuery17')

		    with col1:
		        inputQuery18 = st.text_input('inputQuery18')

		    with col2:
		        inputQuery19 = st.text_input('inputQuery19')

            #preparing
                data=[[inputQuery1, inputQuery2, inputQuery3,inputQuery4, inputQuery5, inputQuery6, inputQuery7, inputQuery8,inputQuery9,inputQuery10,inputQuery11,inputQuery12,inputQuery13,inputQuery14,inputQuery15,inputQuery16,inputQuery17,inputQuery18,inputQuery19]]

		    new_df = pd.DataFrame(data, columns = ['SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender',  'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'tenure'])

		    df_3 = pd.concat([df_1, new_df], ignore_index = True)

		    new_df__dummies = pd.get_dummies(df_3[['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService','MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies','Contract', 'PaperlessBilling', 'PaymentMethod']])
		    col=df_1['tenure']

		    inputQuery19=pd.DataFrame([inputQuery19])
		    col = pd.concat([inputQuery19,col.loc[:]]).reset_index(drop=True)
		    new_df__dummies=new_df__dummies.join(col)

		    # code for Prediction
		    diab_diagnosis = ''
		    
		    # creating a button for Prediction
		    
		    if st.button('Diabetes Test Result'):
		        diab_prediction = model.predict(new_df__dummies.tail(1))
		        if (diab_prediction[0] == 1):
		          diab_diagnosis = 'The person is churning'
		        else:
		          diab_diagnosis = 'The person is not churn'
		        
		    st.success(diab_diagnosis)



    