# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 08:50:04 2018

@author: OREVAS
"""

A=[[1,2],[3,4]]
B=[[5,6],[7,8]]

result = [[0,0],[0,0]]

def perkalian_matrix(X,Y):
    for i in range(len(X)):
       for j in range(len(Y[0])):
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]
    print(result)
if __name__=="__main__":
    perkalian_matrix(A,B)
