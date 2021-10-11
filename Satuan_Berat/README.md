## Satuan Berat.
###### Developed by [Galih Hermawan](https://galih.eu) | [Blog Medium](https://masgalih.medium.com).
---

Menghitung konversi nilai dari satuan berat satu ke yang lain.
Satuan berat dengan penghitungan normal (simple), meliputi: ton, kuintal, kilogram (kg), hektogram (hg), dekagram (dag), gram (g), desigram (dg), sentigram (cg), miligram (mg).

Rujukan: [Tesaurus Kemdikbud](http://tesaurus.kemdikbud.go.id/tematis/lema/satuan%2Bberat) dan [Yuksinau.ID](https://www.yuksinau.id/satuan-berat/)

1. 01_satuan_berat_versi_simple.py
	- konversi sederhana terhadap sebuah nilai dari sebuah satuan ke satuan lain
	- contoh luaran:
        ```
        1.5 kuintal = 150.00 kg
		2 ton = 2000.00 kg
		250 mg = 0.25 g
        ```
        
2. G2_satuan_berat_graph.py
	- dikarenakan kenaikan/penurunan satuan tidak linier atau seragam nilainya, untuk kasus seperti ini lebih cocok menggunakan metode struktur data Graph
	- konsep Graph disesuaikan berdasarkan [Graph Galih](https://github.com/galihboy/py-mini-projects/tree/main/Struktur_Data)
	- kamus data yang telah disesuaikan: 
		```
		satuan = [
					('ton','kuintal',10), 
					('kuintal','kg',100), 
					('kg','hg',10), 
					('hg','dag',10),
					('dag','g',10), 
					('g','dg', 10), 
					('dg','cg',10), 
					('cg','mg',10),
					('kg','pound',2.20462), 
					('ons','hg',1), 
					('pon','ons',5), 
					('lbs','pound',1)
				]
		```
3. 03_multi_masukan.py
	- menerima masukan berupa kalimat yang berisi banyak nilai dan satuan
	- menggunakan class (library) di file **"G2_satuan_berat_graph"** sebelumnya
	- terdapat validasi untuk data masukan dan satuan luaran
	- contoh hasil eksekusi program:
		```
		Data masukan: 1 ton 2.5 kuintal
		Satuan luaran: kg
		1 ton 2.5 kuintal = 1250.0 kg
		```
		
		```
		Data masukan: 1000 mg 1.5 kg 2 ons
		Satuan luaran: g
		1000 mg 1.5 kg 2 ons = 1701.0 g
		```