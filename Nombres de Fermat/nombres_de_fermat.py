#! /usr/bin/env python3
# -*- coding: utf-8 -*-

limiteMin=int(input())
limiteMax=int(input())
n=1
while 2**2**n+1<limiteMin:
    n+=1
while 2**2**n+1<=limiteMax:
    print(2**2**n+1)
    n+=1