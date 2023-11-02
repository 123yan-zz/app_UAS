import streamlit as st
import pandas as pd
import numpy as np

# Judul aplikasi
st.markdown('<div style="text-align: center;"><h1>Analisis Penjualan Supermarket</h1></div>', unsafe_allow_html=True)

# Sidebar untuk menu
menu = st.sidebar.radio("Menu", ["Beranda", "Data Penjualan", "Grafik", "Tentang"])

# Konten utama berdasarkan pilihan menu
if menu == "Beranda":
    # Menampilkan gambar dari direktori lokal
    image = st.image('gambar2.png', caption='Sales Analysis', use_column_width=True)
    st.write("Selamat datang di halaman beranda Analisis penjualan pada Supermarket. Silakan pilih menu lain untuk mengetahui analisis penjualannya.")
elif menu == "Data Penjualan":
    st.subheader("Data Penjualan")
    df=pd.read_csv('supermarket_sales.csv')
# Tampilkan data dalam bentuk tabel
    st.dataframe(df)
elif menu == "Grafik":
    st.subheader("Grafik Penjualan")
    df=pd.read_csv('supermarket_sales.csv')
    # Tambahkan grafik penjualan di sini (gunakan library seperti Matplotlib, Plotly, dll.)
    # Hitung frekuensi metode pembayaran
    pembayaran = df['Payment'].value_counts()
# Tampilkan metode pembayaran terbanyak
# Menambahkan teks dengan ukuran huruf yang diatur
    st.markdown("<h1 style='text-align: center; font-size: 30px;'>Metode Pembayaran Terbanyak</h1>", unsafe_allow_html=True)
    metode_pembayaran = pembayaran.idxmax()
    st.markdown("<p style='font-size: 18px;'>Metode pembayaran yang sering dilakukan oleh pelanggan:</p>", unsafe_allow_html=True) 
    st.markdown(f"<p style='font-size: 18px;'>Metode pembayaran : {metode_pembayaran}</p>", unsafe_allow_html=True)

# Opsional: Tampilkan grafik frekuensi metode pembayaran
    st.markdown("<h2 style='text-align: center; font-size: 20px;'>Grafik Frekuensi Metode Pembayaran</h2>", unsafe_allow_html=True)
    st.bar_chart(pembayaran)

#Hitung jumlah anggota member dan non-member
    jmlh_pembeli_member = (df['Customer type'] == 'Member').sum()
    jmlh_pembeli_normal = (df['Customer type'] == 'Normal').sum()

# Tampilkan perbandingan anggota member dan non-member
    st.markdown("<h1 style='text-align: center; font-size: 30px;'>Perbandingan Anggota Member dan Anggota Normal</h1>", unsafe_allow_html=True)
    st.write(f"<p style='font-size: 18px;'>Anggota Member: {jmlh_pembeli_member}</p>", unsafe_allow_html=True)
    st.write(f"<p style='font-size: 18px;'>Anggota Normal: {jmlh_pembeli_normal}</p>", unsafe_allow_html=True)

# Opsional: Tampilkan grafik perbandingan
    st.markdown("<h2 style='text-align: center; font-size: 20px;'>Grafik Perbandingan Anggota Member dan Normal</h2>", unsafe_allow_html=True)
    st.bar_chart({"Member": jmlh_pembeli_member, "Normal": jmlh_pembeli_normal})
# Hitung jumlah anggota member dan non-member di berbagai cabang
    customer_type = df.groupby(['Customer type', 'City'])['Branch'].count().unstack(fill_value=0)

# Tampilkan tabel perbandingan anggota member dan non-member di berbagai cabang
    st.markdown("<p style=' font-size: 18px;'>Jumlah Anggota Member dan Normal di berbagai Cabang</p>", unsafe_allow_html=True)
    st.dataframe(customer_type)
# Opsional: Tampilkan grafik perbandingan anggota member dan non-member di berbagai cabang
    st.markdown("<h2 style='text-align: center; font-size: 20px;'>Grafik Perbandingan Anggota Member dan Normal di Berbagai Cabang</h2>", unsafe_allow_html=True)
    st.bar_chart(customer_type)
# Hitung total pendapatan untuk anggota member dan non-member
    pendapatan_pembeli = df.groupby('Customer type')['gross income'].sum()
# Tampilkan perbandingan pendapatan antara anggota member dan non-member
    st.markdown("<p style='font-size: 18px;'>Perbandingan Pendapatan Kotor Antara Anggota Member dan Normal</p>", unsafe_allow_html=True) 
    st.dataframe(pendapatan_pembeli)
# Opsional: Tampilkan grafik perbandingan pendapatan
    st.markdown("<h2 style='text-align: center; font-size: 20px;'>Grafik Perbandingan Pendapatan Kotor Anggota Member dan Normal</h2>", unsafe_allow_html=True)
    st.bar_chart(pendapatan_pembeli)


 # Hitung jumlah penjualan untuk setiap produk
    produk = df['Product line'].value_counts()
# Tampilkan produk yang paling banyak dibeli
    nama_produk = produk.idxmax()
    jmlh_produk_beli = produk.max()
    st.markdown("<h1 style='text-align: center; font-size: 30px;'>Produk Yang Banyak Dibeli</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px;'>Produk: {nama_produk}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px;'>Jumlah Penjualan: {jmlh_produk_beli}</h2>", unsafe_allow_html=True)

# Opsional: Tampilkan grafik produk yang paling banyak dibeli
    st.markdown("<h2 style='text-align: center; font-size: 20px;'>Grafik Produk yang Banyak Dibeli</h2>", unsafe_allow_html=True)
    st.bar_chart(produk)

# Ubah kolom tanggal menjadi tipe data datetime
    df['Date'] = pd.to_datetime(df['Date'])
# Hitung total penjualan per hari
    daily_sales = df.groupby(df['Date'].dt.date)['Quantity'].sum()

# Tampilkan penjualan per hari
    st.markdown("<p style='font-size: 18px;'>Penjualan Per Hari Produk</p>", unsafe_allow_html=True) 
    st.dataframe(daily_sales)

# Opsional: Tampilkan grafik penjualan per hari
    st.markdown("<h2 style='text-align: center; font-size: 20px;'>Grafik Penjualan Perhari Produk</h2>", unsafe_allow_html=True)
    st.line_chart(daily_sales)

# Hitung jumlah pembeli di setiap cabang
    jumlah_pembeli = df['City'].value_counts()

# Tampilkan perbandingan jumlah pembeli di setiap cabang
    st.markdown("<p style='font-size: 18px;'>Jumlah Pembeli Di setiap Cabang</p>", unsafe_allow_html=True) 
    st.dataframe(jumlah_pembeli)
# Tampilkan grafik perbandingan jumlah pembeli di setiap cabang
    st.markdown("<h2 style='text-align: center; font-size: 20px;'>Grafik Perbandingan Jumlah Pembeli di Setiap Cabang</h2>", unsafe_allow_html=True)
    st.bar_chart(jumlah_pembeli)

# Mengelompokkan data berdasarkan cabang dan menghitung profit per cabang
    st.markdown("<h1 style='text-align: center; font-size: 30px;'>Pendapat Kotor Supermarket di Berbagai Cabang</h1>", unsafe_allow_html=True)
    pendapat_kotor = df.groupby('City')['gross income'].sum()
# Tampilkan pendapatan bersih per cabang
    st.write("Pendapatan Kotor di Berbagai Cabang:")
    st.dataframe(pendapat_kotor)

# Opsional: Tampilkan grafik pendapatan bersih di berbagai cabang
    st.markdown("<h2 style='text-align: center; font-size: 20px;'>Grafik Pendapatan Kotor Di Berabagai Cabang</h2>", unsafe_allow_html=True)
    st.bar_chart(pendapat_kotor)

elif menu == "Tentang":
    st.subheader("Tentang Analisis")
    # Menampilkan gambar dari direktori lokal
    image = st.image('gambar1.jpg', caption='Supermarket', use_column_width=True)
    st.write("Ini adalah analisis sederhana terkait dengan penjualan yang dibuat dengan Streamlit. Analisis penjualan supermarket ini mengambil data dari salah satu supermarket yang ada pada Negaara Myanmar. Data yang diambil dari kota Yangon, Napitaw, dan Mandalay")

