# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 01:51:40 2021

@author: galih-hermawan
Repository: https://github.com/galihboy/py-mini-projects/tree/main/Satuan_Waktu
Web: https://galih.eu
"""


from libGraph import Graph

# fungsi untuk memeriksa apakah data masukan (nilai) dapat dikonversi ke tipe float
# untuk mendeteksi bahwa nilai masukan harus berupa bilangan (int/float)
def IsFloat(strBil):
    try:
        float(strBil)
    except ValueError:
        return False
    else:
        return True
    
# untuk memvalidasi format data masukan
def Validasi(dataMasukan, kamus):
    # cek jumlah item (nilai, satuan) harus genap
    dataMentah = dataMasukan.split(" ")
    if len(dataMentah) % 2 == 1: 
        return False
    else:
        # data nilai harus bilangan
        dataNilai = dataMentah[::2]
        for nilai in dataNilai:
            if not IsFloat(nilai):
                print(nilai)
                return False
                break
        # data satuan harus terdaftar di kamus
        dataSatuan = dataMentah[1::2]
        for sat in dataSatuan:
            if sat not in kamus:
                print(sat)
                return False
                break
    return True

# kamus satuan waktu
# cara baca: 1 abad = 100 tahun, 1 bulan = 3o hari, dst...
satuan = [
            ('abad', 'tahun', 100),
            ('milenium', 'tahun', 1000),
            ('dasawarsa', 'tahun', 10),
            ('dekade', 'tahun', 10),
            ('windu', 'tahun', 8),
            ('lustrum', 'tahun', 5),
            ('tahun', 'bulan', 12),
            ('tahun', 'hari', 365),
            ('bulan', 'minggu', 4),
            ('bulan', 'hari', 30),
            ('minggu', 'hari', 7),
            ('hari', 'jam', 24),
            ('jam', 'menit', 60),
            ('menit', 'detik', 60)
        ]

# inisialisasi class/object
g = Graph(satuan)

print("\n---------------------------------")
print("Konversi Antar Satuan Waktu.")
print(f"Satuan yang dikenali: {list(g.kamus.keys())}.")
print("Contoh masukan: '1 tahun 2 bulan 3 minggu'.")
print("Untuk luaran cukup pilih salah satu dari satuan waktu.")
print("-----------------------------------")

while True:
    while True:
        masukan = input("Data masukan: ")
        masukan = masukan.strip().lower()
        if Validasi(masukan, g.kamus): break
        else: print("Format masukan tidak sesuai.") 
    while True:
        luaran = input("Satuan luaran: ")
        luaran = luaran.strip().lower()
        if luaran in g.kamus.keys(): break
        else: print("Penulisan luaran tidak sesuai.") 
    
    # ambil semua bagian data masukan
    dataMentah = masukan.split(" ")
    
    dataNilai = dataMentah[::2] # menampung nilai
    dataSatuan = dataMentah[1::2] # menampung satuan
    
    total = 0
    for i in range(int(len(dataMentah)/2)):
        jml = float(dataNilai[i])
        satAwal = dataSatuan[i]
        # gunakan method di class
        jalurLengkap = g.Jalur_Terhubung(satAwal, luaran)
        jalur = g.Rute_Terpendek(jalurLengkap)
        hasil = g.Hitung(jml, jalur)
        # jumlahkan nilai dari setiap satuan
        total += hasil
        
    print(f"{masukan} = {total} {luaran}")
    
    pil = input("Ketik 'y' untuk mengulang, atau ketik apapun untuk keluar >> ")
    if pil.strip().lower() != 'y': break
    print("-----------------------------------")
