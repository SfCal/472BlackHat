import numpy as np
import string
from itertools import *

key = [0, 0, 0, 0]
ct = 'thisisplaceholder'

def letter_to_number(ct):
    ct_num = []
    for letter in ct:
        ct_num.append(str(string.lowercase.find(letter)))
    num_mat = [] #splits big array with letter_to_num into 2x1 matrices 
    for i, j in zip(*[iter(ct_num)]*2):
        num_mat.append([i, j])
    return num_mat

def matrix_mult(bigrams, key):
    multiplied_mat = []
    key = np.array(key,dtype=int) #wont multiply matrix unless numpy array
    bigrams = np.array(bigrams,dtype=int)

    for bigram in bigrams:
        multiplied_mat.append(np.dot(key, bigram)) #multiplies matrix and appends
    for bigram in multiplied_mat:
        for idx, i in enumerate(bigram): #takes mod 26 of each output
            bigram[idx] = i % 26
    return multiplied_mat

def number_to_letter(multiplied_mat):
    converted_str = ''
    for bigram in multiplied_mat:
        for i in bigram:
            converted_str+=(chr(i + 97)) #ascii value of numbers for chr()
    return converted_str

def fitness(ct, wordlist):
    score = 0
    wordlist.seek(0) #start from 0 in list
    for word in wordlist.read().replace('\n', ' '):
        if word in ct:
            score += 1
    return score

def split_mat(mat):
    i=0
    new_list=[]
    while i<len(mat):
        new_list.append(mat[i:i+2]) 
        i+=2
    return new_list

def perms(key):
    perm_super = []
    for i in range(4):
        key[i] += 1
        perms = set(permutations(key))
        perm_super.append(perms) #the "super set" all permutations in a list
    return perm_super

#------------------------------------------
def main(key):
    ct_num = letter_to_number(ct)
    mult_ct = matrix_mult(ct_num, key)
    out = number_to_letter(mult_ct)

    return out

wordlist = open("dictionary.txt", "r")

while key[0] < 26:
    best_score = 0
    best_out = ""
    best_key = ""
    perms_super = perms(key)
    for i in perms_super:
        for j in i: #individual matrix, 1x4
            og = np.array(split_mat(j), dtype=int) #splits and turns into np array
            try:
                inv = np.linalg.inv(og) #inverts og matrix and catches singular matrix
            except:
                continue
            dec = main(inv)
            if fitness(dec, wordlist) > best_score:
                best_key = inv
                best_out = dec
                best_score = fitness(dec, wordlist)
    print(best_score, best_out, best_key)

            
