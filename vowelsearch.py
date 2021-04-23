# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 17:42:04 2021

@author: mohammadtaher
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:40:59 2019

@author: Faradars-pc2
"""
def searchforvowels(w:str):
    ''' find vowels in word '''
    #w = input('Yek kalame benevis: ')
    v = set('aeiou')
    '''found = v.intersection(set(w))
    for vowel in found:
        print(vowel)
    return bool(found)'''
    return v.intersection(set(w))

def search_for_letters(letter:str, find:str = 'aeiuo') -> set:
    ''' find words in  your inputed letter'''
    return set(find).intersection(set(letter))
