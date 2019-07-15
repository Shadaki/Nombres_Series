#! /usr/bin/env python3
# -*- coding: utf-8 -*-

limiteMin=int(input())
limiteMax=int(input())
n=1
while n**2<limiteMin:
    n+=1
while n**2<=limiteMax:
    print(n**2)
    n+=1