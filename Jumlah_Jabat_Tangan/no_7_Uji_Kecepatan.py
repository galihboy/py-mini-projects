"""
Uji Kecepatan Waktu - Menghitung Jumlah Jabat Tangan (Salaman)
---------------------------------------
https://blog.galih.eu
https://galihboy.github.io
----------------------------------------
"""
import no_2_metode_iterative as dua
import no_3_metode_rekursif as tiga
import no_4_metode_barisan_aritmatika as empat
import no_5_baris_dan_deret_aritmatika as lima
import no_6_kombinasi as enam
import time


if __name__ == "__main__":
    # inisialisasi list nama metode dan waktu
    lstMetode = ["Iteratif", "Rekursif", "Barisan aritmatika tingkat 2", "Deret aritmatika", "Kombinasi"]
    lstWaktu = []

    # inisialisasi jumlah orang
    jml_orang = 200
    # jumlah orang harus lebih dari 1
    assert jml_orang > 1

    print("Metode 1 - Iteratif")
    mulai = time.perf_counter_ns()
    jmlSalaman = dua.Hitung_Jumlah_Salaman(jml_orang)
    print(f"Jumlah salaman: {jmlSalaman}")
    akhir = time.perf_counter_ns()
    selisih = (akhir-mulai)/1000
    lstWaktu.append(selisih)
    print(f"Waktu: {selisih} milidetik")
    # ----------------
    print("\nMetode 2 - Rekursif")
    mulai = time.perf_counter_ns()
    jmlSalaman = tiga.Rekursif_Jumlah_Salaman(jml_orang)
    print(f"Jumlah salaman: {jmlSalaman}")
    akhir = time.perf_counter_ns()
    selisih = (akhir - mulai) / 1000
    lstWaktu.append(selisih)
    print(f"Waktu: {selisih} milidetik")
    # -----------------
    print("\nMetode 3 - Barisan Aritmatika Bertingkat Dua")
    mulai = time.perf_counter_ns()
    jmlSalaman = empat.Barisan_Aritmatika_Tingkat_2(jml_orang)
    print(f"Jumlah salaman: {jmlSalaman}")
    akhir = time.perf_counter_ns()
    selisih = (akhir - mulai) / 1000
    lstWaktu.append(selisih)
    print(f"Waktu: {selisih} milidetik")
    # -------------------
    print("\nMetode 4 - Deret Aritmatika (Jumlah Suku)")
    mulai = time.perf_counter_ns()
    jmlSalaman = lima.Deret_Aritmatika(jml_orang)
    print(f"Jumlah salaman: {jmlSalaman}")
    akhir = time.perf_counter_ns()
    selisih = (akhir - mulai) / 1000
    lstWaktu.append(selisih)
    print(f"Waktu: {selisih} milidetik")
    # --------------------
    print("\nMetode 5 - Kombinasi (Faktorial)")
    mulai = time.perf_counter_ns()
    jmlSalaman = enam.Kombinasi_Salaman(jml_orang)
    print(f"Jumlah salaman: {jmlSalaman}")
    akhir = time.perf_counter_ns()
    selisih = (akhir - mulai) / 1000
    lstWaktu.append(selisih)
    print(f"Waktu: {selisih} milidetik")

    print(f"\nDaftar metode sesuai urut waktu secara ascending "
          f"[{jml_orang} orang - {jmlSalaman} salaman].")
    print("----------------------------------------------------------------------------")
    # gabungan list metode dan list waktu
    lstGabungan = list(zip(lstMetode, lstWaktu))
    for i,j in (sorted(lstGabungan, key=lambda indeks: indeks[1])): # indeks[1] adalah waktu
        print(f"{j} mikrodetik - {i}")
