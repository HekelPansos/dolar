#coding: UTF-8
#BY : DarkViper & Keisya
import os
import sys
import time
import random
def viper(s):
	for c in s+'\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(random.random()*0.1)
hijau = '\x1b[1;92m'
cyan = '\x1b[1;96m'
kuning = '\x1b[1;93m'
ungu = '\x1b[1;95m'
putih = '\x1b[1;97m'
biru = '\x1b[1;94m'
merah = '\x1b[1;91m'
os.system('clear')
print
print
print '\x1b[1;94m'
logo = """
   _______         __            __  ______                                    
  |   |   |.-----.|  |--..-----.|  ||   __ \.---.-..-----..-----..-----..-----.
  |       ||  -__||    < |  -__||  ||    __/|  _  ||     ||__ --||  _  ||__ --|
  |___|___||_____||__|__||_____||__||___|   |___._||__|__||_____||_____||_____|"""
print(logo)
print
print
viper("\x1b[1;93m              Program Rupiah ke US Dolar                                ")
print("\x1b[1;91m===========================================================")
viper("\x1b[1;95m[+]Author  : ./Dark<<Viper>>")
viper("[+]Support : MR.HYPER || Risky ID")
viper("[+]Github  : https://github.com/HekelPansos")
viper("[+]Team    : InfectSecurity || Termux Community Indonesia ")
print("\x1b[1;91m===========================================================")
print
print
time.sleep(2)
kurs_rupiah = 15000
rupiah = input("\x1b[1;93mMasukkan Rupiah : ")
konversi = int(rupiah)/kurs_rupiah
time.sleep(2)
print
viper("\x1b[1;92m======================================")
print
time.sleep(1)
print"\x1b[1;93mHasilnya : ",konversi, "USD"
print'\x1b[1;97m'