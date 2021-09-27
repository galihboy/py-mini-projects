# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:20:18 2020

@author: galih-hermawan
Github: https://github.com/galihboy
Web: https://galih.eu
Mail: galih.hermawan@gmail.com
"""

bil1=int(input("Masukkan jumlah menit: "))
#assert 0 <= bil1 < 1000

print (int(bil1/60), "jam dan" , (bil1 % 60), "menit")