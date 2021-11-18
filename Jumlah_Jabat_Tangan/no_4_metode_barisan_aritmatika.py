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

Metode Pola Bilangan -> Barisan Aritmatika

Jml Orang         = 2   3   4   5
Jml Salaman       = 1___3___6___10
Selisih Tingkat 1 =   2___3___4
Selisih Tingkat 2 =     1___1

Termasuk kategori barisan aritmatika bertingkat 2 (dua).
Un = an^2 + bn + c
dimana,
    a = 1/2, b = 1/2, c = 0
"""
def Barisan_Aritmatika_Tingkat_2(jml_orang):
    # n = jml_orang - 1
    a, b, c = 0.5, 0.5, 0
    # un = a*(n**2) + (b*n) + c
    return a*((jml_orang-1)**2) + (b*(jml_orang-1)) + c


if __name__ == "__main__":
    # inisialisasi jumlah orang
    jml_orang = 5
    # jumlah orang harus lebih dari 1
    assert jml_orang > 1
    print(f"\nJumlah salaman: {Barisan_Aritmatika_Tingkat_2(jml_orang)}")