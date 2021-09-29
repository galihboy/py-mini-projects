# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:30:12 2021

@author: galih-hermawan
Repository: https://github.com/galihboy/py-mini-projects/tree/main/Satuan_Berat
Web: https://galih.eu
-----------------------------------------

** Satuan Berat (versi sederhana) **

Menghitung atau mengkonversi sebuah nilai dari sebuah satuan berat ke 
satuan berat yang lain.
"""

'''
Fungsi hitung digunakan untuk menghitung sebuah nilai dari satuan asal (sumber) \
ke satuan tujuan (target)

nilai: bilangan (numerik)
satSumber: satuan sumber
satTarget: satuan target
luaran: nilai x (10^selisih)   -> 10 pangkat selisih
'''
def hitung(nilai, satSumber, satTarget):
	idxSumber = satuan.index(satSumber) # indeks satuan sumber
	idxTarget = satuan.index(satTarget) # indeks satuan target
	selisih = idxTarget-idxSumber # selisih diantara kedua indeks satuan
	return nilai * (10**selisih) # perhitungan akhir dengan luaran berupa nilai (skalar)

'''
Indeks Satuan.
    
idx=2, kosong karena tidak mengandung nama satuan

no indeks:  0        1       2   3     4    5    6   7     8    9
'''
satuan = ['ton', 'kuintal', '','kg', 'hg','dag','g','dg','cg','mg']

# format masukan "x[spasi]satuan", dimana x diset float, kemudian spasi, dan
# salah satu satuan yang harus ada di daftar "satuan" tersebut di atas
masukan = '250 mg' 
satTarget = 'g' # salah satu satuan yang akan dijadikan target/tujuan konversi

# pisahkan data masukan berdasarkan spasi
nilai = float(masukan.split(' ')[0]) # data pertama (numerik)
satSumber = masukan.split(' ')[1] # data kedua (string satuan)

formatLuaran = "{0:.2f}" # batasi hingga 2 digit angka di belakang koma
hasil = hitung(nilai, satSumber, satTarget) # menyimpan nilai fungsi hitung()

# tampilkan ke layar
print(f'{masukan} = {formatLuaran.format(hasil)} {satTarget}')