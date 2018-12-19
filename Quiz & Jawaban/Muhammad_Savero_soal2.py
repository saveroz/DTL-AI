# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 20:27:53 2018

@author: OREVAS
"""
def soal2():
    kalimat=input("")
    list_kalimat=kalimat.split(" ") #buat list dari kata-kata yang diinputkan
    x={} #inialisasi dictionary
    print("--------")
    for i in list_kalimat:
        if i in x: 
            x[i]+=1
        else:  
            x[i]=1
    for a in x:
        if x[a]>1: #jika jumlah kata melebihi satu, maka print kata tersebut
            print(a)
if __name__=='__main__':
    soal2()