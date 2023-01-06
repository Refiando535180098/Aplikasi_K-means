import numpy as np
import pandas as pd
import mysql.connector
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import streamlit as st
from sklearn.preprocessing import StandardScaler
from streamlit_option_menu import option_menu

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
            **Dalam pengelompokan menggunakan K-means dibutuhkan penentuan jumlah
            klaster yang akan menjadi penentu data mana yang merupakan anggota
            dari klaster.**
            """)

nilai = st.slider('**Input klaster :**', 1, 10, 20)

selected = option_menu(
    menu_title=None,
    options=["Data set olah", "Data set input user"],
    default_index=0,
    orientation="horizontal",
    styles={
        "nav-link-selected" : {"background-color": "#00BFFF"},
    }
)

if selected == "Data set olah":
    st.title("Dataset yang diolah :")
    st.write("""
            **Tabel berikut ini merupakan tabel akumulasi data responden dari
            data set Kesulitan, Durasi dan Cerita.**
            """)
    st.write("**Dikarenakan data berupa array maka dimulai dari data ke 0, maka data 0 diartikan sebagai data ke 1 dan seterusnya.**")

    arr = np.array(data)
    arr = pd.DataFrame(arr, columns=['Kesulitan','Durasi','Cerita'])
    st.table(arr)

    st.write("**0 = Action, 1 = Sport, 2 = Race, 3 = RPG, 4 = FPS, 5 = Simulasi, 6 = Strategi.**")

    st.write("""
            **Jika sudah menginput klaster yang diinginkan maka klik tombol "Proses" dibawah
            ini untuk memproses k-means dan melihat hasil pengelompokan data sesuai dengan
            klaster.**
            """)

    if st.button('Proses'):
        if(nilai == 3):
            st.write("""
                **Tabel dibawah ini merupakan tabel hasil data setelah melalui sekala ulang dan
                sudah melalui tahap pengelompokan data mining menggunakan k-means.** 
                """)
            st.write("**Keterangan :**")
            st.write("**0 = Action, 1 = Sport, 2 = Race, 3 = RPG, 4 = FPS, 5 = Simulasi, 6 = Strategi.**")
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
                    **Setelah diproses dengan K-means hasil pengelompokan data sesuai dengan
                    klaster yang sudah ditentukan seperti pada tabel dibawah ini :** 
                """)
            st.write("**Keterangan :** ")
            st.write("""
                    **Nilai Klaster merupakan tabel data dari klaster yang sudah didapatkan,
                    dikarenakan data merupakan data array maka dimulai dari data ke 0 dan seterusnya.**
                    """
                    )
            st.write("**C merupakan inisialisasi dari kluster, jadi jika C1 itu merupakan klaster 1 dan seterusnya.**")
            st.write("""
                    **0 = klaster 1, 1 = klaster 2, 2 = klaster 3, dan seterusnya sampai data klaster akhir sesuai input klaster sebelumnya.**
                    """
                    )
            
            conditions = [
            (data_y['Nilai Klaster']==0),
            (data_y['Nilai Klaster']==1),
            (data_y['Nilai Klaster']==2),]
            choices = ['C1','C2','C3']
            data_y['Klaster'] = np.select(conditions, choices)
            data_y = pd.DataFrame(data_y, columns=['Nilai Klaster', 'Klaster'])

            genre = pd.DataFrame({
                      'Genre Games':['Action', 'Sport', 'Race', 'RPG','FPS', 'Simulasi', 'Strategi']
                      })
            
            conditions = [
            (data_y['Klaster']=='C1'),
            (data_y['Klaster']=='C2'),
            (data_y['Klaster']=='C3')]
            choices = ['Tidak disukai','Disukai','Sangat disukai']
            data_y['Kelompok genre game'] = np.select(conditions, choices)
            data_y = pd.DataFrame(data_y, columns=['Nilai Klaster','Klaster', 'Kelompok genre game'])
            st.table(data_y)
            data_y = pd.DataFrame(data_y, columns=['Klaster', 'Kelompok genre game'])
            genre_game = [genre, data_y]
            tb_genre = pd.concat(genre_game, axis=1)
            st.write("")
            st.write("**Dari hasil pengelompokan maka dapat diambil kesimpulan seperti tabel dibawah ini:**")
            st.table(tb_genre)
            
        else :
            st.write(' :red[**Untuk data set olah hanya menggunakan 3 klaster, karena sesuai dengan rancangan pembuatan aplikasi ini**]')
            st.write("**Silahkan input klaster yang sesuai.**")
if selected == "Data set input user":
    def main():
        st.write("**File yang diinput harus bertype csv dan berformat seperti gambar dibawah ini :**") 
        st.image("/app/aplikasi_k-means/final/image/datatabel.png", width=500)
        st.write("**Catatan :**")
        st.write("**Agar program dapat membaca file, format kolom harus dengan Kolom 1, Kolom 2, dan Kolom 3.**")        
        file = st.file_uploader("**Upload file :**", type=["csv"])
        show_file = st.empty()
    
        if not file:
            show_file.info("**Please upload a file of type:** " + ", ".join(["csv"]))
            return
    
        content = file.getvalue()

        st.write("""
            **Tabel berikut ini merupakan tabel data dari input user untuk dilakukan proses Kmeans.**
            """)
        st.write("Dikarenakan data berupa array maka dimulai dari data ke 0, maka data 0 diartikan sebagai data ke 1 dan seterusnya.")
        data = pd.read_csv(file, sep=";", usecols=["Kolom 1","Kolom 2","Kolom 3"])
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
            df_scaled = pd.DataFrame(df_scaled, columns=['Kolom 1','Kolom 2','Kolom 3'])
            st.table(df_scaled)
            
            km = KMeans(n_clusters=nilai)
            
            y_predicted = km.fit_predict(df_scaled[['Kolom 1','Kolom 2','Kolom 3']])
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
            (data_y['Nilai Klaster']==6),
            (data_y['Nilai Klaster']==7),
            (data_y['Nilai Klaster']==8),
            (data_y['Nilai Klaster']==9),
            (data_y['Nilai Klaster']==10),
            (data_y['Nilai Klaster']==11),
            (data_y['Nilai Klaster']==12),
            (data_y['Nilai Klaster']==13),
            (data_y['Nilai Klaster']==14),
            (data_y['Nilai Klaster']==15),
            (data_y['Nilai Klaster']==16),
            (data_y['Nilai Klaster']==17),
            (data_y['Nilai Klaster']==18),
            (data_y['Nilai Klaster']==19)]
            choices = ['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14'
                       ,'C15','C16','C17','C18','C19','C20']
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