import streamlit as st
import pandas as pd
from PIL import Image


def run():
    st.write("## Exploratory Data Analysis Sustainable LifeStyle")

    st.write("Pada bagian ini akan dijelaskan isi dari dataset yang digunakan untuk membuat Machine Learning untuk memprediksi Rating Sustainable Lifestyle")

    st.markdown('---')
    st.write("### Dataset yang digunakan")
    # Import DataFrame
    df = pd.read_csv('lifestyle_sustainability_data.csv')
    st.dataframe(df)
    st.write("Dataset memiliki data sebanyak 499 baris data dengan 20 kolom")

    st.markdown('---')
    st.write("### Korelasi antar Feature Numerik")
    st.image('feature_correlation.png')
    st.write("Dalam visualisasi Heatmap terlihat nilai korelasi setiap feature numerik. Adapun feature yang sangat banyak mempengaruhi target 'Rating' yaitu konsumsi listrik, konsumsi air, dan tingkat kesadaran lingkungan")

    st.markdown('---')
    st.write("### Mengelompokkan Feature berdasarkan Tipe Data")
    st.write(" ")
    # Menentukan kategorikal nominal dan ordinal
    for i in df.columns:
        if df[i].nunique() < 6 :
            st.write(f"Feature `{i}` : {df[i].unique()}")
    st.write(" ")
    st.write('''
             Pada penelusuran unique Value dapat ditentukan Tipe Data Numerikal, Kategorikal Nominal, dan Kategorikal Ordinal.

             Yang termasuk kedalam Kategorikal Ordinal yaitu `LocalFoodFrequency`, `ClothingFrequency`, dan `UsingPlasticProducts` dengan urutan Rarely, Sometimes, Often, Always. Ada juga `EnvironmentalAwareness` dengan urutan 1, 2, 3, 4, 5.

             Kategorikal Nominal yaitu `Location`, `DietType`, `TransportationMode`, `EnergySource`, `HomeType`, `SustainableBrands`, dan `DisposalMethods`.

             Untuk Numerikal yaitu `Age`, `HomeSize`, `MonthlyElectricityConsumption`, dan `MonthlyWaterConsumption`.

             Selain dari itu, ada beberapa feature yang tidak diikutkan kedalam model karena berbagai hal seperti isi feature tidak berpengaruh ke hasil prediksi dan feature memiliki missing value namun tidak berhubungan dengan kolom manapun sehingga tidak mempengaruhi model prediksi.

             Total Feature yang akan dipakai adalah sebanyak 15 feature dan 1 target `Rating`
            ''')
    
    st.markdown("---")
    st.write("### Persebaran Rating 5 (Very Good) berdasarkan Location")
    st.image('pie_chart.png')
    st.write('''
            Dari visualisasi diatas, terlihat lokasi dengan rating diatas 4 terbagi cukup seimbang antara Urban dan Suburban.

            Partisipan ternyata cenderung cukup puas dengan kehidupan di Urban, dan Suburban dibandingkan dengan yang berada di Rural area, hal ini kemungkinan karena mudahnya akses ke berbagai fasilitas modern dan terjaminnya kehidupan kedepannya.
            ''')
    
    st.markdown("---")
    st.write("### Penyederhanaan Value Target")
    st.write(df['Rating'].value_counts())
    st.write("""
             Dari tabel diatas terlihat persebaran data setiap class nya tidak merata, hal ini dapat mengakibatkan model menjadi bias dan tidak akurat.
             
             Oleh karena itu, value target akan disederhanakan menjadi `Poor`, `Good`, dan `Very Good` dengan rincian sebagai berikut :

             - `Poor` : Rating 1-3
             - `Good` : Rating 4
             - `Very Good` : Rating 5
             """)

if __name__ == '__main__':
    run()