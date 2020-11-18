# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 00:30:59 2020

@author: anwar
"""

# Python Dictionary
# Stores pairs of data
# keys & values

my_dict = {}
grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}

# To add a new pair of data in the grades dictionary

grades['Sylvan'] = 'A'

# Testing if a value is present in dictionary

'John' in grades
# returns true

'Daniel' in grades
# returns false

# To delete an entry
del[grades['Ana']]
grades

# To get a set of keys in the grades dicitonary
grades.keys()

# To get a set of all the values 
grades.values()

