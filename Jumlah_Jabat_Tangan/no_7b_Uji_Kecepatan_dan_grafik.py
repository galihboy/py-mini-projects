"""
Uji Kecepatan Waktu - Menghitung Jumlah Jabat Tangan (Salaman)
---------------------------------------
https://blog.galih.eu
https://galihboy.github.io
----------------------------------------
"""
import no_2_metode_iterative as dua
import no_3_metode_rekursif as tiga
import no_4_metode_barisan_aritmetika as empat
import no_5_baris_dan_deret_aritmetika as lima
import no_6_kombinasi as enam
import time
import numpy as np
import matplotlib.pyplot as plt

# menghitung waktu eksekusi setiap metode
def Hitung_Waktu(NamaFungsi, jml_orang=2, jml_uji=1):
    lstWaktu = []
    for i in range(jml_uji):
        # satuan: nanosecond (nanodetik)
        mulai = time.perf_counter_ns()
        NamaFungsi(jml_orang)
        akhir = time.perf_counter_ns()
        # selisih = (akhir - mulai)  # satuan: nanodetik
        selisih = (akhir - mulai) / 1000  # satuan: mikrodetik
        lstWaktu.append(selisih)
    return np.array(lstWaktu)

# fungsi untuk normalisasi nilai (gak jadi dipakai)
def normalize_list(list_normal):
    max_value = max(list_normal)
    min_value = min(list_normal)
    for i in range(len(list_normal)):
        list_normal[i] = (list_normal[i] - min_value) / (max_value - min_value)
    return list_normal


if __name__ == "__main__":
    # inisialisasi list nama metode dan waktu
    lstMetode = ["Iteratif", "Rekursif", "Barisan Ar. Tk.2", "Deret Ar.", "Kombinasi"]
    lstWaktu = []
    kamus = {}

    # inisialisasi
    jml_orang = 2000
    jml_uji = 10
    satuan = "mikrodetik"
    # jumlah orang harus lebih dari 1
    assert jml_orang > 1

    print("Metode 1 - Iteratif")
    selisih = Hitung_Waktu(dua.Hitung_Jumlah_Salaman, jml_orang, jml_uji)
    print(f"Waktu: {selisih} {satuan}")
    print(f"Max: {selisih.max()}, Min: {selisih.min()}, Avg: {selisih.mean()}")
    lstWaktu.append(selisih)
    # ----------------
    print("\nMetode 2 - Rekursif")
    selisih = Hitung_Waktu(tiga.Rekursif_Jumlah_Salaman, jml_orang, jml_uji)
    print(f"Waktu: {selisih} {satuan}")
    print(f"Max: {selisih.max()}, Min: {selisih.min()}, Avg: {selisih.mean()}")
    lstWaktu.append(selisih)
    # -----------------
    print("\nMetode 3 - Barisan Aritmetika Bertingkat Dua")
    selisih = Hitung_Waktu(empat.Barisan_Aritmetika_Tingkat_2, jml_orang, jml_uji)
    print(f"Waktu: {selisih} {satuan}")
    print(f"Max: {selisih.max()}, Min: {selisih.min()}, Avg: {selisih.mean()}")
    lstWaktu.append(selisih)
    # -------------------
    print("\nMetode 4 - Deret Aritmetika (Jumlah Suku)")
    selisih = Hitung_Waktu(lima.Deret_Aritmetika, jml_orang, jml_uji)
    print(f"Waktu: {selisih} {satuan}")
    print(f"Max: {selisih.max()}, Min: {selisih.min()}, Avg: {selisih.mean()}")
    lstWaktu.append(selisih)
    # --------------------
    print("\nMetode 5 - Kombinasi (Faktorial)")
    selisih = Hitung_Waktu(enam.Kombinasi_Salaman, jml_orang, jml_uji)
    print(f"Waktu: {selisih} {satuan}")
    print(f"Max: {selisih.max()}, Min: {selisih.min()}, Avg: {selisih.mean()}")
    lstWaktu.append(selisih)

    # buat gambar grafik
    fig = plt.figure()
    fig.suptitle(f'Grafik Perbandingan Waktu Eksekusi - Jumlah Orang {jml_orang}', fontsize=16)

    fig.set_figheight(8)
    fig.set_figwidth(8)
    fig.subplots_adjust(hspace=.5)

    ax1 = plt.subplot2grid(shape=(2, 1), loc=(0, 0))
    ax2 = plt.subplot2grid((2, 1), (1, 0))

    # pemrosesan grafik semua data
    ukuran = len(lstWaktu)

    lstRekap = np.empty([ukuran, 4])  # idx, min, avg, max

    # grafik 1
    ax1.title.set_text(f'Uji Kecepatan Pemrosesan {len(lstWaktu)} Metode dalam {jml_uji} x Pengujian')
    for i in range(ukuran):
        lstRekap[i] = [i, lstWaktu[i].min(), lstWaktu[i].mean(), lstWaktu[i].max()]

        ax1.plot(np.linspace(1, jml_uji, jml_uji), lstWaktu[i])
        ax1.scatter(np.linspace(1, jml_uji, jml_uji), lstWaktu[i])

    ax1.set_ylabel(f'Waktu ({satuan})')
    ax1.set_xlabel('Nomor Urut Pengujian')
    ax1.set_xticks(np.linspace(1, jml_uji, jml_uji))
    ax1.set_xticklabels(range(1, jml_uji + 1))
    ax1.legend(lstMetode)

    # grafik 2
    ax2.title.set_text(f'Grafik Perbandingan Kecepatan Tiap Metode')
    lebarBatang = 0.07
    indeks = np.linspace(0, 1, ukuran)
    dataMin, dataAvg, dataMaks = lstRekap[:, 1], lstRekap[:, 2], lstRekap[:, 3]
    bar1 = ax2.bar(indeks, dataMin, lebarBatang, color='r')
    bar2 = ax2.bar(indeks + lebarBatang, dataAvg, lebarBatang, color='b')
    bar3 = ax2.bar(indeks + lebarBatang * 2, dataMaks, lebarBatang, color='g')

    ax2.set_ylabel(f'Waktu ({satuan})')
    ax2.set_xticks(indeks + lebarBatang / 2)
    ax2.set_xticklabels(lstMetode)
    ax2.legend((bar1, bar2, bar3), ('Min', 'Rerata', 'Maks'))

    plt.show()

    # pemrosesan data eksekusi terbaik
    best = np.amin(dataMin)  # tercepat
    indeks = np.where(dataMin == best)
    bestOverall = np.amin(dataAvg)  # rata-rata tercepat
    indeksRata2 = np.where(dataAvg == bestOverall)
    print(f"\nWaktu tercepat: {best:0.3f} {satuan}, Metode: {lstMetode[indeks[0][0]]}")
    print(f"Waktu tercepat rata-rata: {bestOverall:0.3f} {satuan}, Metode: {lstMetode[indeksRata2[0][0]]}")
