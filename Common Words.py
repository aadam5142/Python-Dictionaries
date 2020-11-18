# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 01:58:59 2020

@author: anwar
"""

# Finding common words in a text

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k]== best:
            words.append(k)
    return (words, best)
    