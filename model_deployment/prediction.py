import streamlit as st
import pandas as pd
import pickle

with open('best_model.pkl', 'rb') as file_1:
    model = pickle.load(file_1)

def run():
    st.write("## Predict Sustainability Rating")
    with st.form(key='Form Parameters'):
        Age = st.number_input("Age", step=1)
        Location = st.selectbox('Location', ('Urban', 'Suburban', 'Rural'), index=1)
        DietType = st.selectbox('DietType', ('Mostly Plant-Based','Balanced','Mostly Animal-Based'), index=1)
        LocalFoodFrequency = st.selectbox('LocalFoodFrequency', ('Often', 'Sometimes', 'Rarely'), index=1)
        TransportationMode = st.selectbox('TransportationMode', ('Walk', 'Bike','Public Transit','Car'), index=1)
        EnergySource = st.selectbox('EnergySource', ('Renewable','Mixed','Non-Renewable'), index=1)
        HomeType = st.selectbox('HomeType', ('Apartment','House'), index=1)
        HomeSize = st.number_input('HomeSize', step=1, help='in Square Feet')
        ClothingFrequency = st.selectbox('ClothingFrequency', ('Often','Sometimes','Rarely'), index=1)
        SustainableBrands = st.checkbox('SustainableBrands', value=False)
        EnvironmentalAwareness = st.slider('EnvironmentalAwareness', 1, 5, help='Rate 1 to 5')
        CommunityInvolvement = st.selectbox('CommunityInvolvement', ('Low', 'Moderate','High'), index=1)
        MonthlyElectricityConsumption = st.number_input('MonthlyElectricityConsumption', step=1)
        MonthlyWaterConsumption = st.number_input('MonthlyWaterConsumption', step=1)
        Gender = st.selectbox('Gender', ('Male','Female'), index=1)
        UsingPlasticProducts = st.selectbox('UsingPlasticProducts', ('Often','Sometimes','Rarely'), index=1)
        DisposalMethods = st.selectbox('DisposalMethods', ('Composting','Recycling','Landfill','Combination'), index=1)
        PhysicalActivities = st.selectbox('PhysicalActivities', ('Low','Moderate','High')) 

        submitted = st.form_submit_button('Predict Rating')

    data_inf = {
        'Age':Age,
        'Location':Location,
        'DietType':DietType,
        'LocalFoodFrequency':LocalFoodFrequency,
        'TransportationMode':TransportationMode,
        'EnergySource':EnergySource,
        'HomeType':HomeType,
        'HomeSize':HomeSize,
        'ClothingFrequency':ClothingFrequency,
        'SustainableBrands':SustainableBrands,
        'EnvironmentalAwareness':EnvironmentalAwareness,
        'CommunityInvolvement':CommunityInvolvement,
        'MonthlyElectricityConsumption':MonthlyElectricityConsumption,
        'MonthlyWaterConsumption':MonthlyWaterConsumption,
        'Gender':Gender,
        'UsingPlasticProducts':UsingPlasticProducts,
        'DisposalMethods':DisposalMethods,
        'PhysicalActivities':PhysicalActivities
    }

    data_inf = pd.DataFrame([data_inf])
    

    if submitted:
        st.dataframe(data_inf)
        pred = model.predict(data_inf)
        st.write('## Your Sustainability Rating : ', str(pred))

if __name__ == '__main__':
    run()