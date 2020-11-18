# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 00:59:56 2020

@author: anwar
"""

# Creating a Dictionary

# Lyric Frequency
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict
