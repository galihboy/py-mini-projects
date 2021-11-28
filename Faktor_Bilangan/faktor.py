"""
Galih Hermawan
https://galih.eu
"""


def faktor_bilangan(angka):
    listAngka, listTemp, listOutput = [], [], []

    for i in range(1, angka + 1):
        if angka % i == 0:
            listAngka.append(i)
            hasilBagi = angka // i
            if i not in listTemp:
                listTemp.append(hasilBagi)
                listOutput.append(f"{i} x {hasilBagi}")
    return listAngka, listOutput


if __name__ == "__main__":
    while True:
        try:
            angka = int(input("Masukkan bilangan (isi dengan angka 0 untuk keluar): "))
            assert angka > 0
        except ValueError:
            print("Angka harus bilangan bulat integer.")
        except AssertionError:
            break
        else:
            bilFaktor, bilKali = faktor_bilangan(angka)
            print(f"Faktor bilangan dari {angka} adalah {bilFaktor}")
            print(f"Daftar perkalian : {bilKali}")
