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

Metode Kombinasi
----------------
> Kombinasi 2 unsur dari jml_orang unsur
> i = salaman melibatkan dua orang = 2
> j = jumlah orang terlibat = jml_orang
> Rumus kombinasi.
             j                      jml_orang
            C   = j!/(j−i)!.i! --> C = Faktorial(jml_orang) / ( Faktorial(jml_orang-2) x Faktorial(2) )
             i                      2

"""
def Faktorial(bil):
    if bil in [0, 1]:
        return 1
    else:
        return Faktorial(bil - 1) * bil

def Kombinasi_Salaman(jml_orang):
    return int(Faktorial(jml_orang) / (Faktorial(jml_orang - 2) * Faktorial(2)))


if __name__ == "__main__":
    # inisialisasi jumlah orang
    jml_orang = 5
    # jumlah orang harus lebih dari 1
    assert jml_orang > 1
    print(f"\nJumlah salaman: {Kombinasi_Salaman(jml_orang)}")