import numpy as np
import pandas as pd
import streamlit as st
import mysql.connector

markdown = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://img.freepik.com/free-vector/geometric-shape-perspective-floor_1409-1837.jpg?w=2000");
background-size: cover;
}
[data-testid="stDataFrameResizable"] {
width: 800px;
}
</style>
"""

st.set_page_config(
    page_title="K-means app"
)

st.markdown(markdown, unsafe_allow_html=True)

#conn = mysql.connector.connect(
#    host="localhost",
#    database="db_dataset",
#    user="root",
#    password="")

st.title("Dataset")

st.write(""" **Dataset didapat dari penyebaran kuisioner didapatkan sebanyak
         200 data responden dengan dataset berupa data durasi lama bermain, 
         ketertarikan terhadap cerita, dan tingkat kesulitan dari 7 genre game yang umum dimainkan. 
         seperti action, sport, race, rpg, fps, simulasi, dan strategi.**
         """)

nama_dataset = st.sidebar.selectbox(
    "**Pilih dataset**",
    ('Durasi', 'Kesulitan', 'Cerita')
)

#mycursor = conn.cursor()

st.write(f"## Tabel dataset dari : {nama_dataset}")

if (nama_dataset == 'Durasi') :

    st.write(" **Berikut ini merupakan tabel dataset durasi lama bermain.** ")
    st.write(" **Keterangan : nilai pada tabel dalam satuan jam.** ")
    st.write(" **0 : tidak pernah memainkan.** ")
    st.write(" **5 : dimainkan selama 5 jam atau lebih.** ")
    st.write(" **Dikarenakan data berupa array maka dimulai dari data ke 0, maka data 0 diartikan sebagai data ke 1 dan seterusnya.** ")


    #query = "SELECT `action`, `sport`, `race`, `rpg`,`fps`, `simulasi`, `strategy` FROM durasi"
    #mycursor.execute(query)
    #data1 = mycursor.fetchall()
    data1 = pd.read_csv('/app/aplikasi_k-means/final/durasi.csv', sep=";", usecols=[
    "action", "sport", "race", "rpg", "fps", "simulasi", "strategy"])
    array = np.array(data1)
    array = pd.DataFrame(array, columns=['Action', 'Sport', 'Race', 'RPG','FPS', 'Simulasi', 'Strategi'])
    array

if (nama_dataset == 'Kesulitan') :
    st.write(" **Berikut ini merupakan tabel dataset tingkat kesulitan.** ")
    st.write(" **Keterangan :** ")
    st.write(" **1 : Mudah.** ")
    st.write(" **2 : Sedang.** ")
    st.write(" **3 : Sulit.** ")
    st.write("Dikarenakan data berupa array maka dimulai dari data ke 0, maka data 0 diartikan sebagai data ke 1 dan seterusnya.")


    #query = "SELECT `action`, `sport`, `race`, `rpg`,`fps`, `simulasi`, `strategy` FROM kesulitan"
    #mycursor.execute(query)
    #data2 = mycursor.fetchall()
    data2 = pd.read_csv('/app/aplikasi_k-means/final/kesulitan.csv', sep=";", usecols=[
    "action","sport","race","rpg","fps","simulasi","strategy"])
    array = np.array(data2)
    array = pd.DataFrame(array, columns=['Action', 'Sport', 'Race', 'RPG','FPS', 'Simulasi', 'Strategi'])
    array
    
if (nama_dataset == 'Cerita') :
    st.write(" **Berikut ini merupakan tabel dataset ketertarikan cerita.** ")
    st.write(" **Keterangan :** ")
    st.write(" **0 : Tidak tertarik.** ")
    st.write(" **6 : Sangat tertarik.** ")
    st.write(" **Dikarenakan data berupa array maka dimulai dari data ke 0, maka data 0 diartikan sebagai data ke 1 dan seterusnya.** ")
    
    #query = "SELECT `action`, `sport`, `race`, `rpg`,`fps`, `simulasi`, `strategy` FROM cerita"
    #mycursor.execute(query)
    #data3 = mycursor.fetchall()
    data3 = pd.read_csv('/app/aplikasi_k-means/final/cerita.csv', sep=";", usecols=[
    "action","sport","race","rpg","fps","simulasi","strategy"])
    array = np.array(data3)
    array = pd.DataFrame(array, columns=['Action', 'Sport', 'Race', 'RPG','FPS', 'Simulasi', 'Strategi'])
    array