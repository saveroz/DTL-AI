# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 20:57:48 2018

@author: OREVAS
"""

def soal_1():
    jumlah_orang=input(" ") #jumlah orang beserta uangnya
    lists_orang=[]
    lists_duit=[]
    for i in range(int(jumlah_orang)):
        uang=input(" ")
        lists=uang.split(" ")
        lists_orang.append(lists[0])
        lists_duit.append(lists[1])
    jumlah_transaksi=input(" ") #jumlah transaksi yang terjadi
    for a in range(int(jumlah_transaksi)): 
        transaksi=input(" ")
        lists_2=transaksi.split(" ")
        send=lists_2[0] #pengirim uang
        nom=int(lists_2[1]) #nominal uang
        receive=lists_2[2] #penerima uang
        lists_duit[int(lists_orang.index(send))]=int(lists_duit[int(lists_orang.index(send))])-nom #pengurangan uang terhadap pengirim
        lists_duit[int(lists_orang.index(receive))]=int(lists_duit[int(lists_orang.index(receive))])+nom #penambahan uang terhadap penerima
    print("----------------")
    for j in range(int(jumlah_orang)):
        print(lists_orang[j]+" "+str(lists_duit[j]))
    
if __name__=='__main__': #menjalankan program
    soal_1()