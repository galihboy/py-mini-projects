## Deret Prima.
###### Developed by [Galih Hermawan](https://galih.eu).
---

Tutorial tersedia dalam [Blog Medium](https://masgalih.medium.com/deret-bilangan-prima-dalam-python-8a343084ad6f).

Demo online ada di sini: https://galihboy.github.io/mini_projects/.

1. deretPrima.py
	- aplikasi ini dapat digunakan untuk memeriksa apakah sebuah bilangan termasuk dalam bilangan prima, serta dapat menampilkan deret bilangan prima di antara dua buah bilangan.
	- untuk pemeriksaan bilangan prima, diperlukan 1 argumen berupa numerik
        > python deretPrima.py 4
        ```
        4 adalah bukan bilangan prima
        ```
        
        > python deretPrima.py 5
        ```
        5 adalah bilangan prima
        ```
        
    - untuk menampilkan deret bilangan prima, diperlukan 2 argumen berupa numerik
        > python deretPrima.py 2 20
        ```
        Bilangan prima antara 2 dan 20 adalah:
        2 3 5 7 11 13 17 19
        ```
        
        > python deretPrima.py 100 150
        ```
        Bilangan prima antara 100 dan 150 adalah:
        101 103 107 109 113 127 131 137 139 149
        ```
2. gui_cek_prima.py
	- Aplikasi berbasis GUI untuk memeriksa apakah sebuah bilangan termasuk bilangan prima
3. gui_deret_prima.py
	- Aplikasi berbasis GUI untuk menghasilkan deret bilangan prima
	
	![GUI Deret Prima](/Deret_Prima/gui_deret_prima.jpg)
	
**Catatan:**
Aplikasi GUI dalam hal ini menggunakan library [PyQT5](https://pypi.org/project/PyQt5/), silakan install jika ingin menjalankan. Untuk yang menggunakan environment anaconda silakan menyesuaikan.
