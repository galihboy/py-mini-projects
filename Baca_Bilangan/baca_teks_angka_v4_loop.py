# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 02:04:54 2021

@author: galih-hermawan
"""

from libTulisBilangan import PengelompokanKalimat, KalimatBaru, EvaluasiKalimat, CekKalimat

while True:
    print("\nMasukkan kalimat atau kosongkan jika ingin keluar.")
    kalimat_asli = input("Kalimat: ")
    kalimat = kalimat_asli.strip().lower()
    
    if not kalimat: break
    elif not CekKalimat(kalimat):
        print("Format teks bilangan tidak sesuai.")
    else:
        # rapikan kalimat - cek kamus alias
        kalimat = KalimatBaru(kalimat) 
        kalimat_OK = CekKalimat(kalimat)
        
        #print("Kalimat asli: ", kalimat_asli)
        if kalimat_OK:
            #print("Kalimat asli: ", kalimat_asli)
            # pengelompokan kalimat
            kelompokKalimat = PengelompokanKalimat(kalimat)
            # evaluasi kalimat
            total = EvaluasiKalimat(kelompokKalimat)
            # luaran    
            print("\nTotal nilai: ", total)
            # menggunakan pemisah ribuan - tergantung regional settings
            print(f"Total nilai (lokal): {total:n}")
        else:
            print("Ada komponen kalimat yang tidak terdaftar.")
        
        #print(f"dibaca: {hasil}")