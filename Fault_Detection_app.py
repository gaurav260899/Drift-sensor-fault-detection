import os
import numpy
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import serial
import time
import schedule
import streamlit as st


def prediction_funct():

    arduino = serial.Serial('com14', 9600) #Reading values from Arduino IDE code
    while True: #infinite loop until there is disconnectivity

        readTemp = float(arduino.readline().strip().decode('utf-8')) #reading value from temp
        
        if readTemp ==1.0 or readTemp ==0.0:
            print('Actual Value = ',readTemp)
            signal = []
            for i in range (100): #this value can be changed according to need
                point = float(arduino.readline().strip().decode('utf-8'))
                signal.append(point) #reading value from temp
                #print(point) #printing all values coming from Arduino
                    
            Max = float(max(signal)) #For feature extraction
            Mean = float(numpy.mean(signal)) #For feature extraction
            
            #Paste your Joblib or Pickle file path here of trained data
            with open('SVM_Trained_Code_FaultDetection_PICKLE','rb') as f: #trained algorithm on PC then shifted here using sklearn Pickle because RP has low processing to do training each time
                prediction = pickle.load(f) #0.21.2 version of sklearn needed on both training & testing systems

            X_test = [Max,Mean] #extracted features storing into the list or we can say variable
            print('Max/Mean: ', X_test) #printing the extracted features
            predicted_value = prediction.predict([X_test]) #this line of code will be able to predict the sensor fault, because of trained model
            print('Predicted = ',predicted_value) #Faulty-Signal [0] || Normal-Signal [1]
            st.write('Max/Mean: ',X_test)
            output = predicted_value[0]
            if output == 0:
                pred = 'Faulty'
            else:
                pred = 'Normal'
            return pred

def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:orange;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Sensor Fault Detection using ML </h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
 #   st.title('Fault Detection sensor')  

    m = st.markdown("""
    <style>
    <div style ="background-color:orange;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Prediction
    """, unsafe_allow_html=True)

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button(" Predict "): 
        result = prediction_funct() 
        st.success('Your Sensor is {}'.format(result))
        if result=='Faulty':
            st.warning("""
                 ## **Prediction:** Your sensor is Faulty. Replace!!
                 """
                 )
        else:
            st.warning("""
                 ## **Prediction:** Your sensor is Normal!!
                 """
                 )
            st.balloons()

if __name__=='__main__': 
    main()