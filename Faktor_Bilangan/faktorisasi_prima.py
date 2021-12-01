"""
Galih Hermawan
https://blog.galih.eu
"""
import math
from collections import Counter


# fungsi untuk memeriksa apakah sebuah angka memiliki akar kuadrat dengan mengeluarkan nilai akarnya jika punya
def akar_kuadrat(angka):
    akar = math.sqrt(angka)
    if int(akar+0.5) ** 2 == angka:
        return int(akar)
    else:
        return None

# menghasilkan faktor bilangan dari sebuah angka
def faktor_bilangan(angka):
    listOutput = []
    faktor = [i for i in range(1,angka+1) if angka%i==0]
    jml = len(faktor)//2 + len(faktor)%2
    for i, data in enumerate(faktor):
        if i==jml: break
        listOutput.append([faktor[i], faktor[-1-i]])
    return faktor, listOutput

# menghasilkan hasil faktorisasi prima dari sebuah angka
def faktorisasi_prima(angka):
    lstFaktorisasiPrima = []
    lstTemp = [angka]

    while True:
        angka = lstTemp[0]
        akar = akar_kuadrat(angka)
        if akar:
            lstTemp.remove(angka)
            lstTemp.extend([akar, akar])
        else:
            _, lstFaktor = faktor_bilangan(angka)
            if len(lstFaktor)>1:
                lstTemp.remove(angka)
                lstTemp.extend(lstFaktor[1])
            else: # prima
                lstTemp.remove(angka)
                lstFaktorisasiPrima.append(angka)

        if not lstTemp: break
    return lstFaktorisasiPrima

# menyederhanakan tampilan hasil faktorisasi prima dengan bilangan prima berpangkat
def kamus_penyederhanaan(listFaktorPrima):
    kamus = Counter(listFaktorPrima)
    # print(kamus)
    lst = []
    for i in kamus:
        # print(i, kamus[i])
        lst.append(f"{i}^{kamus[i]}")
    return lst


if __name__ == '__main__':
    angka = 90000

    bilFaktor, hasilKali = faktor_bilangan(angka)
    print(f"Faktor bilangan dari angka {angka} adalah {bilFaktor}")
    print(f"Kombinasi hasil perkalian: {hasilKali}")

    hasil = faktorisasi_prima(angka)
    print(f"Hasil faktorisasi prima dari angka {angka} adalah {hasil}")

    strSederhana = " x ".join(kamus_penyederhanaan(hasil))
    print(f"Bentuk sederhana: {strSederhana}")
