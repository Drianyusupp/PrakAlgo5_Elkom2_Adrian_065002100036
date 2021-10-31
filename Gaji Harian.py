# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 16:18:41 2021

@author: User
"""

print("======== MENGHITUNG GAJI KARYAWAN ========")
sif_kerja = float(input("Jam Masuk Kerja : "))
if sif_kerja < 12.00 :
    print("Selamat Pagi !")
else :
    print("Selamat Siang !")  
pul_kerja = float(input("Jam Keluar Kerja : "))
if pul_kerja > 16.00 :
    print("Selamat Sore !")
    
jml_jam = pul_kerja - sif_kerja
gaji = 175000
    
if jml_jam == 9 :
    total = gaji + 15000
elif jml_jam == 10 :
    total = gaji + 30000
elif jml_jam == 11 :
    total = gaji + 45000
elif jml_jam == 12 :
    total = gaji + 60000
elif jml_jam == 13 :
    total = gaji + 75000
elif jml_jam == 14 :
    total = gaji + 90000
        

print("====== Rincian Gaji ======")
print("Waktu Kerja :  ",jml_jam) 
print("Gaji Per Hari : Rp",gaji)
print("Lembur : Rp")
print("Total Gaji : Rp",total)