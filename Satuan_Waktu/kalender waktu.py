# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:20:18 2020

@author: galih-hermawan
Github: https://github.com/galihboy
Web: https://galih.eu
Mail: galih.hermawan@gmail.com
"""

soal=input("Lama masa (contoh: 1 dasawarsa 2 windu 3 tahun 4 bulan): ")
#soal = "10 dasawarsa 2 windu 3 tahun"
target=input("Satuan (tahun/bulan/hari): ")
#target = "hari"

if (target == "tahun"):
    bulan=1
    hari=1
elif (target == "bulan"):
    bulan=12
    hari=1
elif (target == "hari"):
    bulan=1
    hari=365
else:
    bulan=0
    hari=0

kata = soal.split()
angka=[]
satuan=[]
x=0
y=0
jmlsatuan=0
jml=0
tambahan=""
tambahan1=""
tambahan2=""

for i in range(len(kata)):
    #print(i,kata[i])
    if i % 2 == 0:
        angka.append(kata[i])
        x=x+1
    else:
        satuan.append(kata[i])
        y=y+1
        #print(i,kata[i])

for j in range(len(satuan)):
    if (satuan[j]=="dasawarsa"):
        jmlsatuan=int(angka[j])*10*bulan*hari
    elif (satuan[j]=="windu"):
        jmlsatuan=int(angka[j])*8*bulan*hari
    elif (satuan[j]=="tahun"):
        jmlsatuan=int(angka[j])*bulan*hari
    elif (satuan[j]=="bulan"):
        if (target=="bulan"):
            jmlsatuan=int(angka[j])
        elif (target=="hari"):
            jmlsatuan=int(angka[j])*30
        else:
            jmlsatuan=0
            tambahan1=angka[j]+" bulan"
    elif (satuan[j]=="hari"):
        if (target=="hari"):
            jmlsatuan=int(angka[j])
        else:
            jmlsatuan=0
            tambahan2=angka[j]+" hari"
        
    jml=jml+jmlsatuan

tambahan = tambahan1 + tambahan2

print(jml,target,tambahan)