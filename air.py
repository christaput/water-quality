import pickle
import streamlit as st

# Load model 
cb_water = pickle.load(open('cb_water.sav', 'rb'))

# Judul
st.title('Prediksi Kualitas Air dan kelayakan konsumsi')
st.write('Gunakan web ini untuk memprediksi kualitas air.')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    ph = st.text_input('Input nilai ph')
    Hardness = st.text_input('Input nilai Hardness')
    Solids = st.text_input('Input nilai Solids')
    Chloramines = st.text_input('Input nilai Chloramines')
    Sulfate = st.text_input('Input nilai Sulfate')
with col2 :
    Conductivity = st.text_input('Input nilai Conductivity')
    Organic_carbon = st.text_input('Input nilai organic carbon')
    Trihalomethanes = st.text_input('Input nilai Trihalomethanes')
    Turbidity = st.text_input('Input nilai Turbidity')

# Kode prediksi
water_quality_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Kualitas Air'):
    water_quality_prediction = cb_water.predict([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])

    if(water_quality_prediction[0] == 1):
        water_quality_diagnosis = 'HATI-HATI!! Air tidak layak dikonsumsi.'
        st.error(water_quality_diagnosis)
    else :
        water_quality_diagnosis = 'SELAMAT!! Air layak dikonsumsi.'
        st.success(water_quality_diagnosis)
   

# Footer
st.markdown("---")
footer = """
    <style>
    .footer {
        left: 0;
        bottom: 0;
        width: 100%;
        color: White;
        text-align: center;
        padding: 10px;
    }
    </style>
"""
st.markdown(footer, unsafe_allow_html=True)

# CSS untuk tema gelap
page_bg_img = '''
<style>
.stApp {
  background: #1e1e1e;
  color: #e0e0e0;
  font-family: 'Arial', sans-serif;
}
</style>
'''
# Menyisipkan CSS ke dalam aplikasi
st.markdown(page_bg_img, unsafe_allow_html=True)