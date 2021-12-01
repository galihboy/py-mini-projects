"""
Galih Hermawan
https://blog.galih.eu

Versi Penelusuran Pohon Faktor - Rekursif
        12
       /  \
      2    6
          / \
         2   3
luaran = [2, 2, 3]
"""
from collections import Counter

def faktor_prima_rekursif(angka, lst=[]):
    # jika list kosong
    if not lst:
        if angka == 1:
            return [angka]
        elif angka < 1:
            return None

    # pembagi adalah faktor bilangan terkecil di atas angka 1
    pembagi = next(i for i in range(2, angka+1) if angka % i == 0)

    if angka == pembagi:
        lst.append(angka)
        return lst

    pengali = angka // pembagi
    print(f"Perkalian tingkat {len(lst) + 1} = {pembagi} x {pengali}")

    if pembagi != pengali:
        lst.append(pembagi)
        return faktor_prima_rekursif(pengali)
    else:
        lst.extend([pembagi, pengali])
        return lst

# menyederhanakan tampilan hasil faktorisasi prima dengan bilangan prima berpangkat
def kamus_penyederhanaan(listFaktorPrima):
    if listFaktorPrima:
        kamus = Counter(listFaktorPrima)
        lst = []
        for i in kamus:
            # print(i, kamus[i])
            lst.append(f"{i}^{kamus[i]}")
        if len(lst)>1:
            return " x ".join(lst)
        else:
            return lst[0]
    else:
        return None


if __name__ == '__main__':
    angka = 12
    faktor_prima = faktor_prima_rekursif(angka)
    bentuk_sederhana = kamus_penyederhanaan(faktor_prima)
    print(f"Hasil: {faktor_prima}")
    print(f"Bentuk sederhana: {bentuk_sederhana}")

