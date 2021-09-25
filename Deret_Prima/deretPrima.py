#-------------------------------
# Cek dan Daftar Bilangan Prima
# By Galih Hermawan
# https://galih.eu
#
# Cara penggunaan:
# 1. Satu argumen untuk pengecekan bilangan prima
#       python argPrima.py 5
# 2. Dua argumen untuk menampilkan daftar bilangan prima antara dua bilangan
#       python argPrima.py 5 20

import sys

class Prima:
    #def __init__(self, batasBawah, batasAtas):
    #    self.batasBawah = batasBawah
    #    self.batasAtas = batasAtas
    
    def CekPrima(self, bilangan):
        prima = True
        for i in range(2, bilangan):
            if (bilangan % i == 0):
                prima = False
                break
        return prima
    
    def BilPrima(self, bilangan):
        cek = self.CekPrima(bilangan)
        if cek:
            print("%s adalah bilangan prima" % bilangan)
        else:
            print("%s adalah bukan bilangan prima" % bilangan)
            
    def DaftarPrima(self, batasBawah, batasAtas):
        jml = 0
        print("\nBilangan prima antara %s dan %s adalah: " % (batasBawah, batasAtas))
        for bil in range(batasBawah, batasAtas+1):
            if self.CekPrima(bil):
                print(bil, end=" ")
                jml += 1
        if jml==0: print("bilangan prima tidak ditemukan")
        #print("\n")

if len(sys.argv) == 1:
    print("Tambahkan 1 angka untuk cek sebuah bilangan prima, atau 2 angka dengan urutan batas bawah dan batas atas.")
elif len(sys.argv) == 2:
    p = Prima()
    try:
        bil = int(sys.argv[1])
        p.BilPrima(bil)
    except ValueError:
        print("Parameter argumen harus berupa bilangan bulat")
    
elif len(sys.argv) == 3:
    
    try:
        b1 = int(sys.argv[1])
        b2 = int(sys.argv[2])
    
        assert b1 < b2, "Nilai batas bawah harus lebih kecil dari batas atas"
        p = Prima()
        p.DaftarPrima(int(sys.argv[1]), int(sys.argv[2]))
    except ValueError:
        print("Parameter argumen harus berupa bilangan bulat")
