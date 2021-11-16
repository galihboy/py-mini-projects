"""
Daftar Jabat Tangan (Salaman)
---------------------------------------
https://blog.galih.eu
https://galihboy.github.io
----------------------------------------
2 orang = AB -> A-B (1x salaman)
3 orang = ABC -> A-B, A-C, B-C (3x salaman)
4 orang = ABCD -> A-B, A-C, A-D, B-C, B-D, C-D (6x salaman)
5 orang = ABCDE -> A-B, A-C, A-D, A-E, B-C, B-D, B-E, C-D, C-E, D-E (10x salaman)
"""

# inisialisasi jumlah orang
jml_orang = 5

# jumlah orang harus lebih dari 1
assert jml_orang > 1
# penampung jumlah salaman, inisialisasi 0
jml_salaman = 0

for i in range(1, jml_orang):
    for j in range(i + 1, jml_orang + 1):
        jml_salaman += 1
        print(f"Orang {i} - Orang {j}")

print(f"\nJumlah salaman: {jml_salaman}")