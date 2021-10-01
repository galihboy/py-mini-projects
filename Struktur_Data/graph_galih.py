# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:12:26 2021

@author: galih-hermawan
Repository: https://github.com/galihboy/py-mini-projects/tree/main/Struktur_Data
Web: https://galih.eu
"""


class Graph:
    # inisialisasi kamus kota dari dua arah (kota)
    def __init__(self, data):
        self.data = data
        self.kamus = {}
        for kiri, kanan in data:
            # kota di kiri jadi kunci
            if kiri in self.kamus:
                self.kamus[kiri].append(kanan)
            else:
                self.kamus[kiri] = [kanan]
        	# kota di kanan jadi kunci	
            if kanan in self.kamus:
                self.kamus[kanan].append(kiri)
            else:
                self.kamus[kanan] = [kiri]

    # melihat kamus                
    def Lihat_Kamus(self):
        print(self.kamus)
    
    # menampilkan list jalur terhubung dari kedua kota di setiap kemungkinan
    def Jalur_Terhubung(self, kiri, kanan, jalur=[]):
            jalur = jalur + [kiri]
           
            if kiri == kanan:
                return [jalur]
    
            if kiri not in self.kamus:
                return []
    
            daftar_jalur = []
            for node in self.kamus[kiri]:
                if node not in jalur:
                    daftar_jalur_baru = self.Jalur_Terhubung(node, kanan, jalur)
                    for p in daftar_jalur_baru:
                        daftar_jalur.append(p)
    
            return daftar_jalur
    
    # mirip dengan metode Jalur_Terhubung, hanya saja ditambah penghitungan
    # jumlah node (kota) yang dilalui dari setiap jalur. Yang paling pendek dikembalikan
    def Rute_Terpendek_Asli(self, kiri, kanan, jalur=[]):
            jalur = jalur + [kiri]
            
            if kiri == kanan:
                return jalur
    
            if kiri not in self.kamus:
                return None
    
            jalur_terpendek = None
            for node in self.kamus[kiri]:
                if node not in jalur:
                    sp = self.Rute_Terpendek_Asli(node, kanan, jalur)
                    if sp:
                        # tahap penentuan jalur terpendek - jml kota paling sedikit
                        if jalur_terpendek is None or len(sp) < len(jalur_terpendek):
                            jalur_terpendek = sp
    
            return jalur_terpendek 
    
    # penentuan jalur terpendek dengan cara menghitung dari list jalur
    # yang memiliki jumlah kota paling sedikit
    def Rute_Terpendek_Simple(self, listJalur):
        if len(listJalur)==0:
            return []
        
        terpendek = listJalur[0]
        for i in listJalur:
            if len(i) < len(terpendek):
                terpendek=i
        return terpendek

if __name__ == '__main__':
        
    kota = [
            ("Bandung","Subang"),
            ("Bandung", "Bogor"),
            ("Subang", "Tasikmalaya"),
            ("Tasikmalaya","Bogor"),
            ("Bogor","Bekasi"),
            ("Bogor","Jakarta"),
            ("Bekasi", "Jakarta"),
            ("Malang", "Surabaya"),
            ("Surabaya", "Semarang"),
            ("Surabaya", "Solo"),
            ("Solo", "Cirebon"),
            ("Cirebon", "Jakarta"),
            ("Cirebon", "Tangerang"),
            ("Solo", "Jogjakarta"),
            ("Jogja", "Cirebon"),
            ("Malang", "Solo"),
            ("Semarang", "Bekasi")
        ]
    
    g = Graph(kota)
    
    awal = "Malang"
    tujuan = "Cirebon"
    
    #tujuan = "Malang"
    #awal = "Cirebon"
    
    print("Kamus.\n----------")
    g.Lihat_Kamus()
    jalur = g.Jalur_Terhubung(awal, tujuan)
    jalurPendek = g.Rute_Terpendek_Simple(jalur)
    print(f"\nJalur tersedia.\n{jalur}")
    print(f"\nJalur terpendek.\n{jalurPendek}")
    
    # versi ori jalur terpendek
    print(g.Rute_Terpendek_Asli(awal, tujuan))