# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 02:02:47 2021

@author: galih-hermawan
Github: https://github.com/galihboy/
Web: http://galih.eu
"""

import locale
locale.setlocale(locale.LC_ALL, '') 

# fungsi untuk memeriksa sintaks ekspresi sebelum dievaluasi
def CekSintaks(ekspresi):
    try:
        eval(ekspresi)
    except SyntaxError:
        return False
    else:
        return True

# pemeriksaan komponen kalimat harus ada di daftar Kamus
def CekKalimat(kalimat):
    lstKalimat = kalimat.split()
    for k in lstKalimat:
        if k not in kamusSatuan and k not in kamusAngka and k not in kamusAlias:
            return False
    return True
    
# fungsi untuk merapikan kalimat berdasarkan data alias
def KalimatBaru(kalimat):
    lstKalimat = kalimat.split()
    lstKalimat = [kamusAlias[x] if x in kamusAlias else x for x in lstKalimat]
    kalimatBaru = " ".join(lstKalimat)
    return kalimatBaru

# fungsi untuk menentukan kelompok (klaster) sub kalimat sebelum digabung
def PengelompokanKalimat(kalimat):
    lstKata = kalimat.split()
    lstSatuan = []
    
    # mengambil komponen (kata) terakhir dari teks
    kataTerakhir = lstKata[-1]
    
    # cari satuan dan tampung di list
    lstSatuan = [[kamusSatuan[i], no, i] for no, i in enumerate(lstKata) if i in kamusSatuan]
    
    lstSatuanProses = []
    lstCek = lstSatuan.copy()
    idxAwal = 0
    
    if len(lstSatuan) == 0:
        # jika kalimat tidak mengandung satuan, langsung keluarkan
        lstSatuanProses = [kalimat]
    else:
        while len(lstCek) != 0:
            # cari satuan paling besar, temukan indeksnya, 
            # dan ambil semua kata dari kiri hingga indeks tersebut
            maks = max(lstCek)
            idx = maks[1]
            lstAmbil = lstKata[idxAwal:idx+1]
            teks = " ".join(lstAmbil)
            lstSatuanProses.append(teks)
            
            # indeks awal pindah ke sebelah kanannya
            idxAwal = idx+1
            idCek = lstCek.index(maks)
            # hapus isi list yang sudah dibaca, dan isinya dipindahkan
            del lstCek[0:idCek+1]
            
        # jika terdapat angka (bukan satuan) di bagian terakhir kalimat
        if kataTerakhir in kamusAngka:
            lstSatuanProses.append(kataTerakhir)
        
    return lstSatuanProses
    
# evaluasi kalimat secara menyeluruh
def EvaluasiKalimat(kalimat):
    jmlKalimat = len(kalimat)

    total = 0
    for k in range(jmlKalimat):
        teks = ""
        lstKalimat = kalimat[k].split()
        ukuran = len(lstKalimat)
        for i, sat in enumerate(lstKalimat):
            if sat in kamusAngka:
                teks += "+" + kamusAngka[sat]
            elif sat == "belas":
                teks = teks[:-1] + "1" + teks[-1:]
            elif sat in kamusSatuan:
                pengali = 10**kamusSatuan[sat]
                if i == ukuran-1:
                    teks = "(" + teks[:] + ")" + "*" + str(pengali)
                else:
                    teks += "*" + str(pengali)
                
        #print(f"\nKalimat {k+1}: {kalimat[k]}")
        #print(f"Ekspresi: {teks}")
        #print(f"Hasil evaluasi: {eval(teks)}")
        
        if CekSintaks(teks):
            nilai = eval(teks)
            #print(f"Nilai evaluasi: {nilai}")
            total += nilai
        else:
            print(f"Format teks '{teks}' tidak valid.")
            return None
    return total

kamusSatuan = {
           'puluh': 1,
           'ratus': 2,
           'belas': 2.5,
           'ribu': 3,
           'juta': 6,
           'milyar': 9,
           'triliun': 12
       }

kamusAngka = {
            'nol': '0',
            'satu': '1',
            'dua': '2',
            'tiga': '3',
            'empat': '4',
            'lima': '5',
            'enam': '6',
            'tujuh': '7',
            'delapan': '8',
            'sembilan': '9'
    }

kamusAlias = {
            'sepuluh' : 'satu puluh',
            'sebelas' : 'satu belas',
            'seratus' : 'satu ratus',
            'seribu' : 'satu ribu'
    }

#--------------------------------------------------

if __name__ == "__main__":
    
    
    kalimat_asli = "dua belas juta seratus lima puluh empat ribu lima belas"
    #kalimat_asli = "sebelas ribu sebelas"
    #kalimat_asli = "seratus enam puluh dua ribu tiga ratus dua puluh satu"
    #kalimat_asli = "tiga ratus dua belas"
    #kalimat_asli = "seribu lima ratus lima"
    #kalimat_asli = "seratus ribu lima ratus"
    
    # rapikan kalimat - cek kamus alias
    kalimat = KalimatBaru(kalimat_asli) 
    kalimat_OK = CekKalimat(kalimat)
    
    print("Kalimat asli: ", kalimat_asli)
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