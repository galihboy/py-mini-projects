# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:51:11 2021

@author: galih-hermawan
"""

#from . import libBacaBilangan as lib
from libBacaBilangan import BacaAngka, FixBugsNol, CekAngka

while True:
    print("\nMasukkan bilangan bulat atau kosongkan jika ingin keluar.")
    angka = input("Angka: ")
    
    if not angka.strip(): break
    elif not CekAngka(angka):
        print("Format bilangan tidak sesuai.")
    else:
        #print(BacaAngka("102"))
        hasil = BacaAngka(angka)
        hasil = FixBugsNol(hasil)
        
        print(f"dibaca: {hasil}")
    
