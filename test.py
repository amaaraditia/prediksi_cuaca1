import streamlit as st
import joblib
import numpy as np

# Load model
loaded_model = joblib.load("random_forest_model.pkl")

st.title("Prediksi Kelas Cuaca")

st.markdown("Masukkan data iklim untuk memprediksi kelas cuaca:")

# Input form
temp_average = st.number_input("Suhu Rata-rata (°C)")
temp_max = st.number_input("Suhu Maksimum (°C)")
curah_hujan = st.number_input("Curah Hujan (mm)")
penyinaran_matahari = st.number_input("Penyinaran Matahari (%)")
kelembaban_average = st.number_input("Kelembaban Rata-rata (%)")
kec_angin_average = st.number_input("Kecepatan Angin Rata-rata (m/s)")
arah_angin_most = st.number_input("Arah Angin Paling Sering (°)")
arah_angin = st.number_input("Arah Angin Saat Ini (°)")

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
