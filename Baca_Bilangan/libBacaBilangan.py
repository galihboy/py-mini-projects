# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:48:58 2021

@author: galih-hermawan
"""

# memperbaiki bugs 'nol'
def FixBugsNol(teks):
    listTeks = teks.split()
    jmlKata = len(listTeks)
    if jmlKata > 1:
        if 'nol' in teks:
            # hapus string nol jika jumlah angka > 0
            teks = teks.replace("nol", "")
    # rapikan teks - buang kelebihan spasi            
    teks = " ".join(teks.split())

    return teks

# validasi angka masukan - hanya menerima bilangan integer (negatif atau positif)
def CekAngka(angka):
    try:
        float(angka)
    except ValueError:
        return False
    else:
        return float(angka).is_integer()
    
def BacaAngka(angka):
    # inisialisasi label untuk angka 0 s/d 11
    labelAngka = ('nol', 'satu', 'dua', 'tiga', 'empat', 'lima', \
         'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas')
    
    # memastikan angka masukan adalah integer
    if not CekAngka(angka): return "Hanya menerima bilangan integer."
        
    angka = int(angka)
    teks = ""
    
    # cek untuk bilangan kurang dari nol atau nilai minus
    if angka < 0:
        depan = "minus"
        angka = angka * -1 # dibaca angka positifnya saja
    else:
        depan = ""
    
    # teks satuan hingga sebelas
    if angka <= 11:
        teks += labelAngka[angka]
    # belasan
    elif angka <= 19:
        angkaDepan = labelAngka[angka-10]
        satuan = "belas"
        teks += f"{angkaDepan} {satuan}"
    # puluhan atau 10¹
    elif angka < 100:
        angkaDepan = BacaAngka(angka // 10)
        satuan = "puluh"
        sisa = BacaAngka(angka % 10)
        teks += f"{angkaDepan} {satuan}{sisa}"
    # ratusan atau 10²
    elif angka < 1000:
        angkaDepan = BacaAngka(angka // 100)
        sisa = BacaAngka(angka % 100)
        if angka//100 == 1:
            angkaDepan = ""
            satuan = "seratus"
        else:
            satuan = "ratus"
        teks += f"{angkaDepan} {satuan}{sisa}"
    # ribuan atau 10³
    elif angka < 10000:
        angkaDepan = BacaAngka(angka // 1000)
        sisa = BacaAngka(angka % 1000)
        if angka//1000 == 1:
            angkaDepan = ""
            satuan = "seribu"
        else:
            satuan = "ribu"
        teks += f"{angkaDepan} {satuan}{sisa}"
    # puluhan dan ratusan ribu atau 10⁴ s/d 10⁵
    elif angka < 1000000:
        angkaDepan = BacaAngka(angka // 1000)
        sisa = BacaAngka(angka % 1000)
        satuan = "ribu"
        teks += f"{angkaDepan} {satuan}{sisa}"
    # jutaan atau 10⁶ s/d 10⁸
    elif angka < 1000000000:
        angkaDepan = BacaAngka(angka // 1000000)
        sisa = BacaAngka(angka % 1000000)
        satuan = "juta"
        teks += f"{angkaDepan} {satuan}{sisa}"    
    # milyaran atau 10⁹ s/d 10¹¹
    elif angka < 1000000000000:
        angkaDepan = BacaAngka(angka // 1000000000)
        sisa = BacaAngka(angka % 1000000000)
        satuan = "milyar"
        teks += f"{angkaDepan} {satuan}{sisa}"
    # triliunans atau 10¹² s/d 10 ¹⁴
    elif angka < 1000000000000000:
        angkaDepan = BacaAngka(angka // 1000000000000)
        sisa = BacaAngka(angka % 1000000000000)
        satuan = "triliun"
        teks += f"{angkaDepan} {satuan}{sisa}"
    else:
        teks += "Sorry, angka maksimal kurang dari 1 kuadriliun/dwiyar"
    
    return f"{depan} {teks}"

if __name__ == "__main__":
    bil = '-1239844'
    hasil = BacaAngka(bil)
    hasil = FixBugsNol(hasil)
    
    print(hasil)
    