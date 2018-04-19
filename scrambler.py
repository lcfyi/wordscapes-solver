import argparse
import random
import enchant

dictionary = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
random.seed()
parser = argparse.ArgumentParser()
parser.add_argument("letters")
parser.add_argument("--loc")
args = parser.parse_args()
letters = list(args.letters)
loc = args.loc
count = 0

found_words = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}

with open("english.txt", "r") as word:
    temp = word.read().splitlines()
    for a in temp:
        if loc is not None:
            if len(a) == len(loc):
                is_valid = False
                for idx, b in enumerate(loc):
                    if b is not "?":
                        if a[idx] is b:
                            is_valid = True
                        else:
                            is_valid = False
                if is_valid:
                    dictionary[len(a)].append(a)
        elif len(a) <= 6:
            dictionary[len(a)].append(a)

def check(dictionary, word):
    if word in dictionary:
        return True
    else:
        return False

for a in letters:
    if check(dictionary, a):
        if a not in found_words[1]:
            found_words[1].append(a)
    letters2 = letters.copy()
    letters2.remove(a)
    for b in letters2:
        two_word = a + b
        if check(dictionary[2], two_word):
            if two_word not in found_words[2]:
                found_words[2].append(two_word)
        letters3 = letters2.copy()
        letters3.remove(b)
        for c in letters3:
            three_word = a + b + c
            if check(dictionary[3], three_word):
                if three_word not in found_words[3]:
                    found_words[3].append(three_word)
            letters4 = letters3.copy()
            letters4.remove(c)
            for d in letters4:
                four_word = a + b + c + d
                if check(dictionary[4], four_word):
                    if four_word not in found_words[4]:
                        found_words[4].append(four_word)
                letters5 = letters4.copy()
                letters5.remove(d)
                for e in letters5:
                    five_word = a + b + c + d + e 
                    if check(dictionary[5], five_word):
                        if five_word not in found_words[5]:
                            found_words[5].append(five_word)
                    letters6 = letters5.copy()
                    letters6.remove(e)
                    for f in letters6:
                        six_word = a + b + c + d + e + f 
                        if check(dictionary[6], six_word):
                            if six_word not in found_words[6]:
                                found_words[6].append(six_word)

for idx in range(1,7):
    if len(found_words[idx]) is not 0:
        print("{0} lettered words are:".format(idx))
        print(found_words[idx])