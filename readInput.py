# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 10:36:55 2016

@author: KARTIK
"""

from voicekar import *

n = input('Tell me the string to speak.\n')

typ = input('1.Male\n2.Female\n3.Teen Girl\n')

if int(typ)==1:
    Male(n)
elif int(typ)==2:
    Female(n)
elif int(typ) ==3:
    Girl(n)
else:
    print('error')
    
    