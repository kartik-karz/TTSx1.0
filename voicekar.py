# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:04:39 2016

@author: KARTIK
"""

import pyttsx
engine= pyttsx.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)

voices = engine.getProperty('voices')

male= voices[1].id                  # getting the required voices stored in System, here from windows voice data
female = voices[0].id
girl = voices[2].id

def Male(strText):
    engine.setProperty('voice',male)
    engine.say(strText)
    engine.runAndWait()

def Female(strText):
    engine.setProperty('voice',female)
    engine.say(strText)
    engine.runAndWait()

def Girl(strText):
    engine.setProperty('voice',girl)
    engine.say(strText)
    engine.runAndWait()    
