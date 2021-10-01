# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:52:06 2021

@author: galih-hermawan
"""

class Graph:
    def __init__(self, data):
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
        
    def Rute_Terpendek(self, listJalur):
        if len(listJalur)==0:
            return []
        
        terpendek = listJalur[0]
        for i in listJalur:
            if len(i) < len(terpendek):
                terpendek=i
        return terpendek
    
    def Hitung(self, nilai, jalur):
        if len(jalur) > 1:
            jmlTotal = 1
            satAwal = jalur[0]
            for i in range(1,len(jalur)):
                for x in self.kamus[satAwal]:
                    if x[0]== jalur[i]:
                        jmlTotal = jmlTotal * x[1]
                        satAwal = x[0]
                        
            return nilai * float(jmlTotal)
        else:
            return nilai

if __name__ == '__main__':
    
    # kamus satuan berat
    # cara baca: 1 ton = 10 kuintal, ..., 1 kg = 2.20462 pound, ..., 1 pon = 5 ons, dst...
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
    
    # inisialisasi class/object
    g = Graph(satuan)
    
    # contoh data: 2.5 ons = 250 gram ?
    jml = 2.5 # nilai
    satAwal = "ons" # satuan awal
    satTarget = "g" # satuan target
    jmlD = 3 # jumlah angka (desimal) di belakang koma
    
    # contoh kalau data dibalik: 2.5 g = 0.025 ons ?
    #satTarget = "ons" # satuan awal
    #satAwal = "g" # satuan target
    
    # menentukan jalur satuan yang terlibat di antara satAwal dan satTarget
    jalurLengkap = g.Jalur_Terhubung(satAwal, satTarget)
    # jika ada lebih dari satu jalur, diambil yang paling pendek
    jalur = g.Rute_Terpendek(jalurLengkap)
    # menghitung total nilai sesuai satuan yang dilewati dikali jml (nilai) masukan
    Total = g.Hitung(jml, jalur)
    print(f"{jml} {satAwal} = {Total:.{jmlD}f} {satTarget}")