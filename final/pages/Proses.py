import numpy as np
import pandas as pd
import mysql.connector
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import streamlit as st
from sklearn.preprocessing import StandardScaler

#conn = mysql.connector.connect(
#    host="3306",
#    database="db_dataset",
#    user="root",
#    password="")

#mycursor = conn.cursor()

markdown = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://img.freepik.com/free-vector/geometric-shape-perspective-floor_1409-1837.jpg?w=2000");
background-size: cover;
}
[data-testid="stTable"] {
height: 400px;
border-style: outset;
background-color: rgb(255, 255, 255);
}
</style>
"""

st.set_page_config(
    page_title="K-means app"
)

data = pd.read_csv('/app/aplikasi_k-means/final/dataolah.csv', sep=";", usecols=[
   "Kesulitan", "Durasi", "Cerita"])

st.markdown(markdown, unsafe_allow_html=True)

st.title("Proses K-Means")
st.write("""
            Dalam pengelompokan menggunakan K-means dibutuhkan penentuan jumlah
            klaster yang akan menjadi penentu data mana yang merupakan anggota
            dari klaster.
            """)

nilai = st.slider('**Input klaster :**', 0, 3, 6)

tab1, tab2 = st.tabs(["Data set olah", "Data set input user"])

with tab1:
    st.title("Dataset yang diolah :")
    st.write("""
            Tabel berikut ini merupakan tabel akumulasi data responden dari
            data set Kesulitan, Durasi dan Cerita.
            """)
    st.write("Dikarenakan data berupa array maka dimulai dari data ke 0, maka data 0 diartikan sebagai data ke 1 dan seterusnya.")

    #query = "SELECT `kesulitan`, `durasi`, `cerita` FROM data_olah"
    #mycursor.execute(query)
    #data1 = mycursor.fetchall()
    arr = np.array(data)
    arr = pd.DataFrame(arr, columns=['Kesulitan','Durasi','Cerita'])
    st.table(arr)

    st.write("0 = Action, 1 = Sport, 2 = Race, 3 = RPG, 4 = FPS, 5 = Simulasi, 6 = Strategi.")

    st.write("""
            Jika sudah menginput klaster yang diinginkan maka klik tombol "Proses" dibawah
            ini untuk memproses k-means dan melihat hasil pengelompokan data sesuai dengan
            klaster. Klaster yang dapat ditentukan hanya sampai 6 klaster karena jika lebih
            dari 6 klaster proses k-means pada data tidak effisien dalam memberikan hasil.
            """)

    if st.button('Proses'):
        if(nilai == 3):
            st.write("""
                Tabel dibawah ini merupakan tabel hasil data setelah melalui sekala ulang dan
                sudah melalui tahap pengelompokan data mining menggunakan k-means. 
                """)
            st.write("Keterangan :")
            st.write("0 = Action, 1 = Sport, 2 = Race, 3 = RPG, 4 = FPS, 5 = Simulasi, 6 = Strategi.")
            scaler = StandardScaler()
            scaler.fit(arr)
            df_scaled = scaler.transform(arr)
            df_scaled = pd.DataFrame(df_scaled, columns=['Kesulitan','Durasi','Cerita'])
            st.table(df_scaled)
            
            km = KMeans(n_clusters=nilai)
            
            y_predicted = km.fit_predict(df_scaled[['Kesulitan','Durasi','Cerita']])
            data_y = y_predicted
            data_y = pd.DataFrame(data_y, columns=['Nilai Klaster'])
            
            st.write("""
                    Setelah diproses dengan K-means hasil pengelompokan data sesuai dengan
                    klaster yang sudah ditentukan seperti pada tabel dibawah ini : 
                """)
            
            conditions = [
            (data_y['Nilai Klaster']==0),
            (data_y['Nilai Klaster']==1),
            (data_y['Nilai Klaster']==2),
            (data_y['Nilai Klaster']==3),
            (data_y['Nilai Klaster']==4),
            (data_y['Nilai Klaster']==5),
            (data_y['Nilai Klaster']==7)]
            choices = ['C1','C2','C3','C4','C5','C6','C7']
            data_y['Klaster'] = np.select(conditions, choices)
            data_y = pd.DataFrame(data_y, columns=['Nilai Klaster', 'Klaster'])
            st.table(data_y)
        
            conditions = [
            (data_y['Klaster']=='C1'),
            (data_y['Klaster']=='C2'),
            (data_y['Klaster']=='C3')]
            choices = ['Tidak disukai','Disukai','Sangat disukai']
            data_y['Kelompok genre game'] = np.select(conditions, choices)
            data_y = pd.DataFrame(data_y, columns=['Nilai Klaster', 'Klaster', 'Kelompok genre game'])
            st.table(data_y)
            
            st.write("Keterangan : ")
            st.write("""
                    Nilai Klaster merupakan tabel data dari klaster yang sudah didapatkan,
                    dikarenakan data merupakan data array maka dimulai dari data ke 0 dan seterusnya.
                    """
                    )
            st.write("""
                    0 = klaster 1, 1 = klaster 2, 2 = klaster 3, dan seterusnya sampai data klaster akhir sesuai input klaster sebelumnya.
                    """
                    )
            st.write("C merupakan inisialisasi dari kluster, jadi jika C1 itu merupakan klaster 1 dan seterusnya.")
        else :
            st.write(' :red[Untuk data set olah hanya menggunakan 3 klaster, karena sesuai dengan rancangan pembuatan aplikasi ini]')
            st.write("Silahkan input klaster yang sesuai.")
with tab2:
    def main():
        st.write("File yang diinput harus bertype csv dan berformat seperti gambar dibawah ini :") 
        st.image("/app/aplikasi_k-means/final/image/datatabel.png", width=500)
        st.write("Catatan :")
        st.write("Dengan kolom yang bernama col1, col2, dan col3")        
        file = st.file_uploader("Upload file", type=["csv"])
        show_file = st.empty()
    
        if not file:
            show_file.info("Please upload a file of type: " + ", ".join(["csv"]))
            return
    
        content = file.getvalue()

        st.write("""
            Tabel berikut ini merupakan tabel data dari input user untuk dilakukan proses Kmeans.
            """)
        st.write("Dikarenakan data berupa array maka dimulai dari data ke 0, maka data 0 diartikan sebagai data ke 1 dan seterusnya.")
        data = pd.read_csv(file, sep=";", usecols=["col1","col2","col3"])
        st.dataframe(data.head(10))
        file.close()
        
        if st.button('Proses data'):
            st.write("""
                Tabel dibawah ini merupakan tabel hasil data setelah melalui sekala ulang dan
                sudah melalui tahap pengelompokan data mining menggunakan k-means. 
                """)
            st.write("Keterangan :")
            st.write("0 = Action, 1 = Sport, 2 = Race, 3 = RPG, 4 = FPS, 5 = Simulasi, 6 = Strategi.")
            scaler = StandardScaler()
            scaler.fit(data)
            df_scaled = scaler.transform(data)
            df_scaled = pd.DataFrame(df_scaled, columns=['col1','col2','col3'])
            st.table(df_scaled)
            
            km = KMeans(n_clusters=nilai)
            
            y_predicted = km.fit_predict(df_scaled[['col1','col2','col3']])
            data_y = y_predicted
            data_y = pd.DataFrame(data_y, columns=['Nilai Klaster'])
            
            st.write("""
                    Setelah diproses dengan K-means hasil pengelompokan data sesuai dengan
                    klaster yang sudah ditentukan seperti pada tabel dibawah ini : 
                """)
            
            conditions = [
            (data_y['Nilai Klaster']==0),
            (data_y['Nilai Klaster']==1),
            (data_y['Nilai Klaster']==2),
            (data_y['Nilai Klaster']==3),
            (data_y['Nilai Klaster']==4),
            (data_y['Nilai Klaster']==5),
            (data_y['Nilai Klaster']==7)]
            choices = ['C1','C2','C3','C4','C5','C6','C7']
            data_y['Klaster'] = np.select(conditions, choices)
            data_y = pd.DataFrame(data_y, columns=['Nilai Klaster', 'Klaster'])
            st.table(data_y)
            
            st.write("Keterangan : ")
            st.write("""
                    Nilai Klaster merupakan tabel data dari klaster yang sudah didapatkan,
                    dikarenakan data merupakan data array maka dimulai dari data ke 0 dan seterusnya.
                    """
                    )
            st.write("""
                    0 = klaster 1, 1 = klaster 2, 2 = klaster 3, dan seterusnya sampai data klaster akhir sesuai input klaster sebelumnya.
                    """
                    )
            st.write("C merupakan inisialisasi dari kluster, jadi jika C1 itu merupakan klaster 1 dan seterusnya.")
    
    main()