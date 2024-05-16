import streamlit as st
import pickle
import numpy as np
import pandas as pd

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Prediksi Harga Mobil Audi Bekas")

model = st.selectbox('Input Model Mobil', df['model'].unique())
year = st.selectbox('Input Tahun Mobil', df['year'].unique())
transmission = st.selectbox('Input Transmisi Mobil', df['transmission'].unique())
fuelType = st.selectbox('Input Jenis Bahan Bakar Mobil', df['fuelType'].unique())
mileage = st.number_input('Input Jarak Tempuh Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi Bahan Bakar Mobil')
engineSize = st.number_input('Input Ukuran Mesin Mobil')

if st.button('Prediksi Harga Mobil'):
    query = pd.DataFrame({
        'model': [model],
        'year': [year],
        'transmission': [transmission],
        'fuelType': [fuelType],
        'mileage': [mileage],
        'tax': [tax],
        'mpg': [mpg],
        'engineSize': [engineSize]
    })

    st.write(f"<p style='font-size: 30px; font-weight: bold;'>Prediksi Harga Mobil Audi Bekas Dalam Rupiah yaitu Rp {int(np.exp(pipe.predict(query)[0]) * 20000)}</p>", unsafe_allow_html=True)
