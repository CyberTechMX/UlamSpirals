#!/usr/bin/env python
#-*- encoding: utf-8 -*-
 
def make_spiral(n):
	if n % 2 == 0:
		n -= 1
    matrix = []
    for x in range(n):
        sm = []
        for y in range(n):
            sm.append(0)
        matrix.append(sm)
    count = 1
    aux = n / 2
    for i in range(aux + 1):
        for j in range(aux + i, aux-(2+i),-1):
            if (count==n*n+1): break
            matrix[aux-i][j] = count
            count += 1
        if count == n*n+1: break
        for j in range(aux-(1+i), aux+i):
            matrix[j+2][aux-(1+i)] = count
            count += 1
        for j in range(aux-(1+i), aux+(1+i)):
            matrix[aux+(1+i)][j+1] = count
            count += 1
        for j in range(aux+i, aux-(1+i), -1):
            matrix[j][aux+(1+i)] = count
            count += 1
    return matrix

#n is a odd number in other case the result is for n - 1
#example make_spiral(7) response:
#[49, 48, 47, 46, 45, 44, 43]
#[26, 25, 24, 23, 22, 21, 42]
#[27, 10, 09, 08, 07, 20, 41]
#[28, 11, 02, 01, 06, 19, 40]
#[29, 12, 03, 04, 05, 18, 39]
#[30, 13, 14, 15, 16, 17, 38]
#[31, 32, 33, 34, 35, 36, 37]
#Note the left zero is not include on the response.