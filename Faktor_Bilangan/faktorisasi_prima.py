"""
Galih Hermawan
https://blog.galih.eu
"""
import math
from collections import Counter


# menghasilkan faktor bilangan dari sebuah angka
def faktor_bilangan(angka):
    listOutput = []
    faktor = [i for i in range(1, angka + 1) if angka % i == 0]
    jml = len(faktor) // 2 + len(faktor) % 2
    for i, data in enumerate(faktor):
        if i == jml: break
        listOutput.append([faktor[i], faktor[-1 - i]])
    return faktor, listOutput


# menimpa data list yang memiliki akar kuadrat dengan nilai akarnya
def akar_kuadrat_v2(listAngka):
    for angka in listAngka:
        akar = math.sqrt(angka)
        if int(akar + 0.5) ** 2 == angka:
            yield int(akar)
        else:
            yield angka


# menyeleksi data list yang termasuk dalam bilangan prima
def seleksi_prima(listAngka):
    for angka in listAngka:
        bilFaktor, hasilKali = faktor_bilangan(angka)
        if len(hasilKali) == 1 and angka != 1:
            yield angka


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
    angka = 100

    # 1. Membangkitkan bilangan faktor
    bilFaktor, hasilKali = faktor_bilangan(angka)
    print(f"Faktor bilangan dari angka {angka} adalah {bilFaktor}")

    # 2. Cari bilangan yang memiliki akar kuadrat, ganti angka lama dengan angka akar kuadratnya.
    list_pasca_akar_kuadrat = [i for i in akar_kuadrat_v2(bilFaktor)]
    print(f"Hasil penggantian bilangan yang memiliki akar kuadrat: {list_pasca_akar_kuadrat}")

    # 3. Seleksi hanya yang termasuk bilangan prima
    list_prima = [i for i in seleksi_prima(list_pasca_akar_kuadrat)]
    print(f"List faktor prima: {list_prima}")

    # 4. Penyederhanaan
    strSederhana = " x ".join(kamus_penyederhanaan(list_prima))
    print(f"Bentuk sederhana: {strSederhana}")
