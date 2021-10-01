## Satuan Waktu.
###### Developed by [Galih Hermawan](https://galih.eu).
---

File berikut dibuat karena dulu membantu saya mengevaluasi tugas anak SD kelas 4 pada materi satuan waktu. Walaupun satuan waktunya belum lengkap.

1. menit ke jam.py
	- mengkonversi total menit menjadi jam
	- contoh luaran:
        ```
        Masukkan jumlah menit: 80
		1 jam dan 20 menit
        ```
        

        ```
        Masukkan jumlah menit: 135
		2 jam dan 15 menit
        ```
        
2. jam kegiatan.py
	- menentukan jam selesai dengan cara menambahkan sejumlah menit ke jam mulai (awal)
	- contoh luaran:
		```
        Jam mulai kegiatan (contoh: 08.35): 8.35
		Lama menit kegiatan (contoh: 45): 45
		Waktu selesai kegiatan: 09.20
        ```
        

        ```
		Jam mulai kegiatan (contoh: 08.35): 22.10
		Lama menit kegiatan (contoh: 45): 150
		Waktu selesai kegiatan: 00.40
        ```
3. kalender waktu.py
	- konversi dari kombinasi satuan waktu: dasawarsa, windu, tahun, bulan, hari; ke dalam satuan waktu yang dipilih
	- contoh luaran:
	```
	Lama masa (contoh: 1 dasawarsa 2 windu 3 tahun 4 bulan): 1 dasawarsa 1 windu 3 tahun
	Satuan (tahun/bulan/hari): tahun
	Total: 21 tahun 
	```

	```
	Lama masa (contoh: 1 dasawarsa 2 windu 3 tahun 4 bulan): 1 tahun 3 bulan
	Satuan (tahun/bulan/hari): hari
	Total: 455 hari  
	```
4. libGraph.py
	- diambil dan diadaptasi dari [lib Graph Satuan Berat](https://github.com/galihboy/py-mini-projects/blob/main/Satuan_Berat/G2_satuan_berat_graph.py)
	- cukup diganti isi kamus datanya
5. konversi satuan waktu.py
	- menerima masukan berupa kalimat yang berisi banyak nilai dan satuan
	- menggunakan class (library) di file **"libGraph.py"** sebelumnya
	- terdapat validasi untuk data masukan dan satuan luaran
	- contoh hasil eksekusi program:
		```
		Data masukan: 1 milenium 2 abad 3 lustrum 2 windu
		Satuan luaran: tahun
		1 milenium 2 abad 3 lustrum 2 windu = 1231.0 tahun
		```
		
		```
		Data masukan: 2.5 jam 30 menit 1 hari
		Satuan luaran: detik
		2.5 jam 30 menit 1 hari = 97200.0 detik
		```