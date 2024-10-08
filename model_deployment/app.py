import streamlit as st
import eda
import prediction

st.set_page_config(
    page_title='Sustainability Lifestyle Rating',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Judul
st.title("Machine Learning to Predict Sustainable Lifestyle Rating")

st.write(
'''
Feature yang akan digunakan pada project ini sebagai berikut :

|Nama Feature|Deskripsi|
|---|---|
|ParticipantID|ID Partisipan|
|Age|Usia Partisipan|
|Location|Tempat tinggal partisipan (Urban, Suburban, Rural)|
|DietType|Preferensi Diet (Mostly Plant-Based, Balanced, Mostly Animal-Based)|
|LocalFoodFrequency|Frekuensi Konsumsi makanan lokal (Often, Sometimes, Rarely)|
|TransportationMode|Alat transportasi utama (Bike, Public Transit, Car, Walk)|
|EnergySource|Sumber energi utama (Renewable, Mixed, Non-Renewable)|
|HomeType|Tipe tempat tinggal (Apartment, House)|
|HomeSize|Luas tempat tinggal|
|ClothingFrequency|Frekuensi pembelian pakaian (Often, Sometimes, Rarely)|
|SustainableBrands|Prioritas belanja produk merk berkelanjutan (True, False)|
|EnvironmentalAwareness|Tingkat kesadaran lingkungan (1-5)|
|CommunityInvolvement|Keterlibatan masyarakat (High, Moderate, Low)|
|MonthlyElectricityConsumption|Rata-rata penggunaan listrik|
|MonthlyWaterConsumption|Rata-rata penggunaan air|
|Gender|Jenis kelamin partisipan|
|UsingPlasticProducts|Penggunaan produk berbahan plastik (Often, Sometimes, Rarely)|
|DisposalMethods|Metode utama membuang sampah (Composting, Recycling, Landfill, Combination)|
|PhysicalActivities|Aktifitas fisik (High, Moderate, Low)|
|Rating|Peringkat Sustainibility partisipan (1-5)|


''')

# Navigasi Bar
navigation = st.sidebar.selectbox("Halaman : ", ("EDA", "Predict Sustainability Rating"))
st.sidebar.write('''
                Creator : Muhammad Asril Hanif
                 
                Batch : RMT-034
                ''')

if navigation == "EDA":
    eda.run()
else:
    prediction.run()