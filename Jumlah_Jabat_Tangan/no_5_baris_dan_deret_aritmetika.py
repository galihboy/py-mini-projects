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

Metode Pola Bilangan -> Baris dan Deret Aritmetika
---------------------------------------------------
JUMLAH ORANG       JABAT TANGAN            TOTAL
----------------------------------------------------
2 orang                  1                   1
3 orang                1 + 2                 3
4 orang              1 + 2 + 3               6
5 orang            1 + 2 + 3 + 4            10
----------------------------------------------------
a = 1
b = 1 (selisih jumlah item di jabat tangan)
n = n-1

.: Suku ke-n :.
Un = a + (n-1)b = 1 + (n-1-1)1 = n-1
.: Jumlah suku ke-n :.
Sn = n/2 x (a + Un) = n/2 x (2a + (n-1)b) => (n-1)/2 x (2x1 + (n-1-1)x1) = (n^2 - n) / 2
"""
def Deret_Aritmetika(jml_orang):
    return int((jml_orang**2 - jml_orang)/2)

"""
.: Jumlah suku ke-n - Versi lain :.

2 orang adalah 1
3 orang adalah (1 + 2)
4 orang adalah (1 + 2 + 3)
5 orang adalah (1 + 2 + 3 + 4)
n orang adalah (1 + 2 + 3 + … + (n – 1))
------------------------------------------
Sn = n/2 . (a + Un)
n = jumlah orang - 1
a = suku pertama = 1
Un = suku ke n (jumlah orang - 1)

"""
def Deret_Aritmetika_Versi2(jml_orang):
    return int(((jml_orang-1) / 2) * (1 + jml_orang-1))


if __name__ == "__main__":
    # inisialisasi jumlah orang
    jml_orang = 5
    # jumlah orang harus lebih dari 1
    assert jml_orang > 1
    print(f"\nJumlah salaman 1: {Deret_Aritmetika(jml_orang)}")
    print(f"\nJumlah salaman 2: {Deret_Aritmetika_Versi2(jml_orang)}")