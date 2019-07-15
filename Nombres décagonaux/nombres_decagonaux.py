#! /usr/bin/env python3
# -*- coding: utf-8 -*-

limiteMin=int(input())
limiteMax=int(input())
n=0
while n*(4*n-3)<limiteMin:
    n+=1
while n*(4*n-3)<limiteMax:
    print(int(n*(4*n-3)))
    n+=1