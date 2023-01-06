import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

markdown = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://img.freepik.com/free-vector/geometric-shape-perspective-floor_1409-1837.jpg?w=2000");
background-size: cover;
}
[data-testid="stSidebar"] {
    background-color: #A9E1FF;
}
</style>
"""

st.set_page_config(
    page_title="K-means app"
)
st.markdown(markdown, unsafe_allow_html=True)

st.title("K-means")

st.write("Hallo selamat datang..")

selected = option_menu(
    menu_title=None,
    options=["Tujuan", "Pengertian K-Means", "Kelebihan dan Kekurangan"],
    default_index=0,
    orientation="horizontal",
    styles={
        "nav-link-selected" : {"background-color": "#00BFFF"},
    }
)

if selected == "Tujuan":
    st.write("""
            **Aplikasi ini dibuat untuk pengelompokan tingkat peminatan genre game menggunakan 
            algoritma data mining K-means clustering.**
    """)
    st.write("**Manfaat dari penelitian adalah sebagai berikut :**")
    st.write("""
             **1. Memberikan hasil berupa informasi dari pengelompokan genre game dengan 
                klasifikasi dan penentuan genre game yang tidak disukai, disukai dan sangat disukai;**
             """) 
    st.write("""
             **2. Membantu mengidentifikasi beberapa genre game untuk menentukan tidak 
                disukai, disukai dan genre sangat disukai.**
             """)
    st.write("**Alur dari program K-Means sebagai berikut :**")
    image = Image.open('/app/aplikasi_k-means/final/image/flowchart.jpg')
    st.image(image)

if selected == "Pengertian K-Means":
    st.write("""
            **K-Means Clustering adalah suatu metode penganalisaan data
            atau metode Data Mining yang melakukan proses pemodelan 
            unssupervised learning dan menggunakan metode yang mengelompokan data berbagai partisi.**
    """)
    image = Image.open('/app/aplikasi_k-means/final/image/k-means-clustering.png')
    st.image(image)
    st.write("**Sumber :** https://www.trivusi.web.id/2022/06/algoritma-kmeans-clustering.html")
if selected == "Kelebihan dan Kekurangan":
    st.write("**Karakteristik Kelebihan dari K-Means clustering :** ")
    st.write("**1. Cepat dalam proses clustering**")
    st.write("**2. Sensitif terhadap nilai centroid**")
    st.write("**3. Hasil dari Kmeans selalu berubah ubah(dikarenakan tidak unik)**")
    st.write("**4. Sulit meraih global optimum**")

    st.write("**Karakteristik Kekurangan dari K-Means clustering :**")
    st.write("**1. Cluster model berbeda ditemukan**")
    st.write("**2. Sulit untuk memilih jumlah cluster yang tepat**")
    st.write("**3. Overlapping**")
    st.write("**4. Kegagalan dalam konverge**")