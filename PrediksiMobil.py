import streamlit as st
import pickle
import numpy as np
import pandas as pd
import textwrap

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title('Selamat Datang!')
st.image("Audiimage.jpg", width=400)

text = """
Audi adalah merek mobil yang berasal dari Jerman, dikenal karena kombinasi antara desain elegan, teknologi inovatif, dan performa yang canggih. Berdiri sebagai bagian dari Volkswagen Group, Audi telah menjadi salah satu pemimpin dalam industri otomotif global. Performa menjadi fokus utama Audi, dengan rentang model mulai dari mobil kompak hingga supercar. Mesin bertenaga tinggi, transmisi yang responsif, serta sistem suspensi yang terkemuka, menjadikan Audi sebagai pilihan bagi para penggemar mobil yang mencari keseimbangan antara kekuatan dan kenyamanan. Dalam pasar mobil bekas, mobil Audi bekas masih menawarkan pengalaman mengemudi yang memuaskan. Performa mesin yang kuat, kabin yang nyaman, dan fitur-fitur teknologi yang masih relevan membuatnya tetap menjadi pilihan menarik bagi banyak pembeli mobil bekas. Dengan pemilihan yang tepat dan perawatan yang baik, mobil Audi bekas dapat memberikan nilai yang baik dan kepuasan dalam jangka waktu yang panjang kepada pemiliknya.
"""

wrapped_text = textwrap.fill(text, width=70)

st.markdown(f"<div style='text-align: justify'>{wrapped_text}</div>", unsafe_allow_html=True)

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
