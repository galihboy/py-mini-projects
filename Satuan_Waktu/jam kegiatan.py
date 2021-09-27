# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:27:24 2020

@author: galih-hermawan
Github: https://github.com/galihboy
Web: https://galih.eu
Mail: galih.hermawan@gmail.com
"""

jam = input("Jam mulai kegiatan (contoh: 08.35): ")
waktu = jam.split(".") # pisahkan jam dan menit
j=int(waktu[0]) # jam
m=int(waktu[1]) # menit
assert 0 <= m <= 59 # menit harus berada pada rentang 0-59

lama = int(input ("Lama menit kegiatan (contoh: 45): "))

totalmulai = j * 60 + m # total menit dari waktu mulai
totalwaktu = totalmulai + lama # total menit setelah waktu mulai ditambah lama menit

jamselesai = int(totalwaktu/60) # pembagian bilangan bulat
menitselesai = totalwaktu%60 # sisa hasil bagi

if jamselesai < 10: 
    jamselesai = f"0{jamselesai}"
elif jamselesai >= 24:
    jamselesai = f"0{jamselesai-24}"
    
if menitselesai < 10: menitselesai = f"0{menitselesai}"

print(f"Waktu selesai kegiatan: {jamselesai}.{menitselesai}")

