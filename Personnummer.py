#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:54:00 2022

@author: brage
"""
import numpy as np
import sys
check = False
føds_num = input("Hva er fødselsnummeret?") #Spør om fødselsnummer
føds_num_liste = [int(x) for x in føds_num] #Lager en liste med nummerene som blir lagt inn


if len(føds_num_liste) != 11: #Sjekker om listen er for lang og kjønn på eier
    
    if len(føds_num_liste) >11:
        print("Dette fødselsnummeret er for langt.")
        sys.exit("lang")                                  #Exceptions kan være en dårlig måte å få programmet til å stoppe på,spør Bjarte.
    else:  
        print("Dette fødselsnummeret er for kort")
        sys.exit("kort")
else: 
        
    if føds_num_liste[-3] %2==0:
        print("Du er en kvinne")
    
    else: print("Du er en mann")


v1 = np.array([0]*11) #Lager en tom array
kontroll_array_v1 = [3, 7, 6, 1, 8, 9, 4, 5, 2, 0, 0] #Lager en array med data
føds_num_array = np.array(føds_num_liste) #Lager en array av en liste
np.multiply(føds_num_liste, kontroll_array_v1, out = v1) #Multipliserer to arrays mot hverandre
np.sum(v1) #Summerer alle verdiene i arrayen
if np.sum(v1) %11 == 0: #Hvis resten er null blir I1 lik 0
    I1 = 0
else: I1 = 11-(np.sum(v1)%11) #Hvis ikke 


if føds_num_liste[-2] == I1:
    check = True

else: 
    check = False

v2 = np.array([0]*11)
kontroll_array_v2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 0]
np.multiply(føds_num_liste, kontroll_array_v2, out = v2)

if check == True:

    if np.sum(v2) %11 == 0:
        I2 = 0
    else: 
        I2 = 11-(np.sum(v2)%11)
if føds_num_liste[-1] == I2 and check == True:
    print("Fødselsnummeret er gyldig.")
else: 
    print("Fødselsnummeret er ikke gyldig")