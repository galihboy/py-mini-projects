# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:52:06 2021

@author: galih-hermawan
Repository: https://github.com/galihboy/py-mini-projects/tree/main/Satuan_Waktu
Web: https://galih.eu
"""

class Graph:
    def __init__(self, data):
        # membuat kamus data berdasarkan satuan
        self.data = data
        self.kamus = {}
        for kiri, kanan, nilai in data:
            # nilai satuan sesuai masukan di awal (dalam kamus)
            if kiri in self.kamus:
                self.kamus[kiri].append([kanan, nilai])
            else:
                self.kamus[kiri] = [[kanan, nilai]]
            # nilai satuan kebalikan
            if kanan in self.kamus:
                nilai = 1/nilai
                self.kamus[kanan].append([kiri, nilai])
            else:
                nilai = 1/nilai
                self.kamus[kanan] = [[kiri, nilai]]
    
    # mengambil semua jalur satuan-satuan yang terlibat
    def Jalur_Terhubung(self, kiri, kanan, jalur=[]):
            jalur = jalur + [kiri]
            
            if kiri == kanan:
                return [jalur]
    
            if kiri not in self.kamus:
                return []
    
            daftar_jalur = []
            for node in self.kamus[kiri]:
                if node[0] not in jalur:
                    daftar_jalur_baru = self.Jalur_Terhubung(node[0], kanan, jalur)
                    for p in daftar_jalur_baru:
                        daftar_jalur.append(p)
    
            return daftar_jalur
    
    # menentukan satuan yang terlibat adalah yang terpendek
    def Rute_Terpendek(self, listJalur):
        if len(listJalur)==0:
            return []
        
        terpendek = listJalur[0]
        for i in listJalur:
            if len(i) < len(terpendek):
                terpendek=i
        return terpendek
    
    # menghitung total nilai satuan
    def Hitung(self, nilai, jalur):
        if len(jalur) > 1:
            jmlTotal = 1
            satAwal = jalur[0]
            for i in range(1,len(jalur)):
                for x in self.kamus[satAwal]:
                    if x[0]== jalur[i]:
                        jmlTotal = jmlTotal * x[1]
                        satAwal = x[0]
                        
            return nilai * jmlTotal
        else:
            return nilai

if __name__ == '__main__':
    
    # kamus satuan berat
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
    
    # kamus satuan waktu
    satuanWaktu = [
            ('abad', 'tahun', 100),
            ('milenium', 'tahun', 1000),
            ('dasawarsa', 'tahun', 10),
            ('dekade', 'tahun', 10),
            ('windu', 'tahun', 8),
            ('lustrum', 'tahun', 5),
            ('tahun', 'bulan', 12),
            ('tahun', 'hari', 365),
            ('bulan', 'minggu', 4),
            ('bulan', 'hari', 30),
            ('minggu', 'hari', 7),
            ('hari', 'jam', 24),
            ('jam', 'menit', 60),
            ('menit', 'detik', 60)
        ]
    
    # inisialisasi class/object
    g = Graph(satuanWaktu)
    
    jml = 1 # nilai
    satAwal = "tahun" # satuan awal
    satTarget = "minggu" # satuan target
    jmlD = 0 # jumlah angka (desimal) di belakang koma
    
    #satTarget = "tahun" # satuan awal
    #satAwal = "minggu" # satuan target
    
    # menentukan jalur satuan yang terlibat di antara satAwal dan satTarget
    jalurLengkap = g.Jalur_Terhubung(satAwal, satTarget)
    # jika ada lebih dari satu jalur, diambil yang paling pendek
    jalur = g.Rute_Terpendek(jalurLengkap)
    # menghitung total nilai sesuai satuan yang dilewati dikali jml (nilai) masukan
    Total = g.Hitung(jml, jalur)
    print(f"{jml} {satAwal} = {Total:.{jmlD}f} {satTarget}")