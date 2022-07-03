import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/94716/Desktop/Streamlit/Diabetes Prediction/trained_model.sav', 'rb'))

def diabetes_predictor(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
       return 'The person is not diabetic'
    else:
        return 'The person is diabetic'



def main():

    #giving title
    st.title("Diabetes prediction web app")

    #input fields from user
    # Pregnancies,Glucose,BloodPressure,SkinThickness,
    # Insulin,
    # BMI,DiabetesPedigreeFunction,Age,Outcome

    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose')
    BloodPressure = st.text_input('BloodPressure')
    SkinThickness = st.text_input('SkinThickness')
    Insulin = st.text_input('Insulin')
    bmi = st.text_input('BMI')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
    Age = st.text_input('Age')

    #prediction
    diagnosis = ''

    #button
    if st.button('Get Diagnosiss'):
        diagnosis = diabetes_predictor([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, bmi, DiabetesPedigreeFunction, Age])

    st.success(diagnosis)


if __name__ == '__main__':
    main()

