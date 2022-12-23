import pickle
import numpy as np
import streamlit as st

# membaca model
jenis_model = pickle.load(open('kismis.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Jenis Kismis')



Area = st.number_input('Input Nilai Daerah')

MajorAxisLength = st.number_input('Input Nilai Panjang Sumbu Utama')

MinorAxisLength = st.number_input('Input Nilai Panjang Sumbu Kecil')

Eccentricity = st.number_input('Input Nilai Keanehan')

ConvexArea = st.number_input('Input Nilai Convex Area')

Extent = st.number_input('Input Nilai Cakupan')

Perimeter = st.number_input('Input Nilai Perimeter')


# code untuk prediksi
hasil = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Jenis Kismis '):
    jenis_predic = jenis_model.predict([[Area, MajorAxisLength, MinorAxisLength, Eccentricity, ConvexArea, Extent, Perimeter]])

    if(jenis_predic[0] == 1):
        hasil = 'Jenis Kecimen'
    else :
        hasil = 'Jenis Besni'
 
st.success(hasil)