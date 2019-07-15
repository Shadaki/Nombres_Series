#! /usr/bin/env python3
# -*- coding: utf-8 -*-

limiteMin=int(input())
limiteMax=int(input())
for n in range(limiteMin,limiteMax+1):
    if n%10 in [0,1,5,6]:
        if int(str(n**2)[-len(str(n)):])==n:
            print(n)