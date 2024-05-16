import streamlit as st
import textwrap

st.set_page_config(
    page_title='Halo',
    page_icon='🙌'
)

st.title('Selamat Datang!')
st.image("Audiimage.jpg", width=400)

text = """
Audi adalah merek mobil yang berasal dari Jerman, dikenal karena kombinasi antara desain elegan, teknologi inovatif, dan performa yang canggih. Berdiri sebagai bagian dari Volkswagen Group, Audi telah menjadi salah satu pemimpin dalam industri otomotif global. Performa menjadi fokus utama Audi, dengan rentang model mulai dari mobil kompak hingga supercar. Mesin bertenaga tinggi, transmisi yang responsif, serta sistem suspensi yang terkemuka, menjadikan Audi sebagai pilihan bagi para penggemar mobil yang mencari keseimbangan antara kekuatan dan kenyamanan. Dalam pasar mobil bekas, mobil Audi bekas masih menawarkan pengalaman mengemudi yang memuaskan. Performa mesin yang kuat, kabin yang nyaman, dan fitur-fitur teknologi yang masih relevan membuatnya tetap menjadi pilihan menarik bagi banyak pembeli mobil bekas. Dengan pemilihan yang tepat dan perawatan yang baik, mobil Audi bekas dapat memberikan nilai yang baik dan kepuasan dalam jangka waktu yang panjang kepada pemiliknya.
"""

wrapped_text = textwrap.fill(text, width=70)

st.markdown(f"<div style='text-align: justify'>{wrapped_text}</div>", unsafe_allow_html=True)

st.sidebar.success('Silahkan Pilih Halaman Diatas')