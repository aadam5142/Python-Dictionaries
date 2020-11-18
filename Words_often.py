# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:30:22 2020

@author: anwar
"""

# Leveraging Dicitonary Properties

def words_often(freqs, minTimes):
    result = []
    done = false
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del (freqs[w])
                
        else:
            done = True
    return result

print(words_often)