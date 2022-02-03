from multiprocessing.sharedctypes import Value
import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('ml_model.pkl','rb'))

@st.cache(allow_output_mutation=True)
def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

header_content = st.container()
prediction = st.container()
dataset_descrb = st.container()
#main


with header_content:
    st.title('Hello Friends ! , This is an End to End to Machine Learning Project :smile:')
    first_para = '<p style="font-family:Helvetica; color:Black; font-size: 20px;">In this project I have developed a ML model to indicates if water is safe for human consumption . Lets see about the Data dictionary.... </p>'
    st.markdown(first_para, unsafe_allow_html=True)

    st.header('About the Data dictionary:')
    st.subheader('pH value:')
    st.markdown('PH is an important parameter in evaluating the acid–base balance of water. It is also the indicator of acidic or alkaline condition of water status. WHO has recommended maximum permissible limit of pH from 6.5 to 8.5. The current investigation ranges were 6.52–6.83 which are in the range of WHO standards.')
    st.subheader('Hardness:')
    st.markdown('Hardness is mainly caused by calcium and magnesium salts. These salts are dissolved from geologic deposits through which water travels. The length of time water is in contact with hardness producing material helps determine how much hardness there is in raw water. Hardness was originally defined as the capacity of water to precipitate soap caused by Calcium and Magnesium.')
    st.subheader('Solids (Total dissolved solids - TDS):')
    st.markdown('Water has the ability to dissolve a wide range of inorganic and some organic minerals or salts such as potassium, calcium, sodium, bicarbonates, chlorides, magnesium, sulfates etc. These minerals produced un-wanted taste and diluted color in appearance of water. This is the important parameter for the use of water. The water with high TDS value indicates that water is highly mineralized. Desirable limit for TDS is 500 mg/l and maximum limit is 1000 mg/l which prescribed for drinking purpose.')
    st.subheader('Chloramines:')
    st.markdown('Chlorine and chloramine are the major disinfectants used in public water systems. Chloramines are most commonly formed when ammonia is added to chlorine to treat drinking water. Chlorine levels up to 4 milligrams per liter (mg/L or 4 parts per million (ppm)) are considered safe in drinking water.')
    st.subheader('Sulfate:')
    st.markdown('Sulfates are naturally occurring substances that are found in minerals, soil, and rocks. They are present in ambient air, groundwater, plants, and food. The principal commercial use of sulfate is in the chemical industry. Sulfate concentration in seawater is about 2,700 milligrams per liter (mg/L). It ranges from 3 to 30 mg/L in most freshwater supplies, although much higher concentrations (1000 mg/L) are found in some geographic locations.')
    st.subheader('Conductivity:')
    st.markdown('Pure water is not a good conductor of electric current rather’s a good insulator. Increase in ions concentration enhances the electrical conductivity of water. Generally, the amount of dissolved solids in water determines the electrical conductivity. Electrical conductivity (EC) actually measures the ionic process of a solution that enables it to transmit current. According to WHO standards, EC value should not exceeded 400 μS/cm.')
    st.subheader('Organic_carbon:')
    st.markdown('Total Organic Carbon (TOC) in source waters comes from decaying natural organic matter (NOM) as well as synthetic sources. TOC is a measure of the total amount of carbon in organic compounds in pure water. According to US EPA < 2 mg/L as TOC in treated / drinking water, and < 4 mg/Lit in source water which is use for treatment.')
    st.subheader('Trihalomethanes:')
    st.markdown('THMs are chemicals which may be found in water treated with chlorine. The concentration of THMs in drinking water varies according to the level of organic material in the water, the amount of chlorine required to treat the water, and the temperature of the water that is being treated. THM levels up to 80 ppm is considered safe in drinking water')
    st.subheader('Turbidity:')
    st.markdown('The turbidity of water depends on the quantity of solid matter present in the suspended state. It is a measure of light emitting properties of water and the test is used to indicate the quality of waste discharge with respect to colloidal matter. The mean turbidity value obtained for Wondo Genet Campus (0.98 NTU) is lower than the WHO recommended value of 5.00 NTU.')

with dataset_descrb:
    st.header('*Water Potability dataset*')
    second_para = '<p style="font-family:Helvetica; color:Black; font-size: 20px;">Lets see the insights of the dataset by visualizing the dataset...</p>'
    st.markdown(second_para, unsafe_allow_html=True)
    df = load_data("water_potability.csv")
    load_data = ['Organic_carbon']
    features = df[load_data]
    d1=features.head(50)
    st.line_chart(d1)
    load_data1= ['Solids']
    features = df[load_data1]
    d2=features.head(50)
    st.line_chart(d2)
    with st.expander("See explanation"):
     st.write("""The above chart is derived using the below given data set...""")
     st.dataframe(df)

with prediction:
    st.header(""" Let's predict""")
    third_para = '<p style="font-family:Helvetica; color:Black; font-size: 20px;">Enter the values below and lets indicates if water is safe for human consumption</p>'
    st.markdown(third_para, unsafe_allow_html=True)
    a, b = st.columns(2)
    pH = a.text_input('Enter pH of water :',0)
    ph = float(pH)
    Hardness = b.text_input('Enter the Hardness of water (mg/L):', 0)
    Hardness = float(Hardness)
    Solids = a.text_input('Enter the Solids of water (ppm):', 0)
    Solids = float(Solids)
    Chloramines = b.text_input('Enter the Amount of Chloramines of water (ppm):', 0)
    Chloramines = float(Chloramines)
    Sulfates = a.text_input('Enter the Amount of Sulfates dissolved of water (mg/L):', 0)
    Sulfates = float(Sulfates)
    Conductivity  = b.text_input('Enter the Electrical conductivity of water  (μS/cm):', 0)
    Conductivity  = float(Conductivity)
    Organic_carbon = a.text_input('Enter the Amount of organic carbon  of water (ppm):', 0)
    Organic_carbon = float(Organic_carbon)
    Trihalomethanes = b.text_input('Enter the Amount of Trihalomethanes of water (μg/L):', 0)
    Trihalomethanes = float(Trihalomethanes)
    Turbidity = a.text_input('Enter the Turbidity of water (Nephelometric Turbidity Units):', 0)
    Turbidity = float(Turbidity)
    new_data = [[pH,Hardness,Solids, Chloramines,Sulfates,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]]
    predict_value = model.predict(new_data)
    result = st.button("Predict")
    if result:
        if predict_value == 1:
            st.subheader('I am very happy to say that water is safe for human consumption :smile:')
        else:
            st.subheader('Sorry I am sad to say that water is not safe for human consumption :pensive:')