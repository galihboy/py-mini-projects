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

Metode Iteratif
2 orang = 1
3 orang = 1 + 2 = 3
4 orang = 1 + 2 + 3 = 6
5 orang = 1 + 2 + 3 + 4 = 10
"""

def Hitung_Jumlah_Salaman(jml_orang):
    total = 0
    for i in range(1, jml_orang):
        total += i
    return total


if __name__ == "__main__":
    # inisialisasi jumlah orang
    jml_orang = 5
    # jumlah orang harus lebih dari 1
    assert jml_orang > 1
    print(f"\nJumlah salaman: {Hitung_Jumlah_Salaman(jml_orang)}")
