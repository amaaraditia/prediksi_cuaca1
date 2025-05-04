import streamlit as st
import joblib
import numpy as np

# Load model
loaded_model = joblib.load("random_forest_model.pkl")

st.title("Prediksi Kelas Cuaca")

st.markdown("Masukkan data iklim untuk memprediksi kelas cuaca:")

# Input form
temp_average = st.number_input("Suhu Rata-rata (°C)", value=27.5)
temp_max = st.number_input("Suhu Maksimum (°C)", value=32.0)
curah_hujan = st.number_input("Curah Hujan (mm)", value=150.2)
penyinaran_matahari = st.number_input("Penyinaran Matahari (jam)", value=7.4)
kelembaban_average = st.number_input("Kelembaban Rata-rata (%)", value=80.5)
kec_angin_average = st.number_input("Kecepatan Angin Rata-rata (m/s)", value=3.2)
arah_angin_most = st.number_input("Arah Angin Paling Sering (°)", value=180.0)
arah_angin = st.number_input("Arah Angin Saat Ini (°)", value=190.0)

if st.button("Prediksi Kelas Cuaca"):
    input_data = np.array([
        temp_average,
        temp_max,
        curah_hujan,
        penyinaran_matahari,
        kelembaban_average,
        kec_angin_average,
        arah_angin_most,
        arah_angin
    ]).reshape(1, -1)

    prediction = loaded_model.predict(input_data)
    st.success(f"Kelas cuaca yang diprediksi: **{prediction[0]}**")