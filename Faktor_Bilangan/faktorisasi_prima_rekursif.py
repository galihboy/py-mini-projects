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


if __name__ == '__main__':
    angka = 12
    print("Hasil: ", faktor_prima_rekursif(angka))

