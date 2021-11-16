"""
Jumlah Jabat Tangan (Salaman)
---------------------------------------
https://blog.galih.eu
https://galihboy.github.io
----------------------------------------
2 orang = AB -> A-B (1x salaman)
3 orang = ABC -> A-B, A-C, B-C (3x salaman)
4 orang = ABCD -> A-B, A-C, A-D, B-C, B-D, C-D (6x salaman)
5 orang = ABCDE -> A-B, A-C, A-D, A-E, B-C, B-D, B-E, C-D, C-E, D-E (10x salaman)
------------------------------------------------------------------------------------

Metode Rekursif -> F() adalah fungsi rekursif
2 orang = F(2) = 1
3 orang = F(2) + 2 = 1 + 2 = 3
4 orang = F(3) + 3 = 3 + 3 = 6
5 orang = F(4) + 4 = 6 + 4 = 10
...
x orang = F(x-1) + (x-1)
"""


def Rekursif_Jumlah_Salaman(jml_orang):
    if jml_orang == 2:
        return 1
    else:
        return Rekursif_Jumlah_Salaman(jml_orang - 1) + (jml_orang - 1)


if __name__ == "__main__":
    # inisialisasi jumlah orang
    jml_orang = 5
    # jumlah orang harus lebih dari 1
    assert jml_orang > 1
    print(f"\nJumlah salaman: {Rekursif_Jumlah_Salaman(jml_orang)}")
