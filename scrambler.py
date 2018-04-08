import argparse
import random
import enchant

dictionary = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
random.seed()
parser = argparse.ArgumentParser()
parser.add_argument("letters")
args = parser.parse_args()
letters = list(args.letters)
count = 0

one = []
two = []
three = []
four = []
five = []
six = []

with open("english.txt", "r") as word:
    temp = word.read().splitlines()
    for a in temp:
        if len(a) <= 6:
            dictionary[len(a)].append(a)

def check(dictionary, word):
    if word in dictionary:
        return True
    else:
        return False

for a in letters:
    if check(dictionary, a):
        one.append(a)
    letters2 = letters.copy()
    letters2.remove(a)
    for b in letters2:
        two_word = a + b
        if check(dictionary[2], two_word):
            two.append(two_word)
        letters3 = letters2.copy()
        letters3.remove(b)
        for c in letters3:
            three_word = a + b + c
            if check(dictionary[3], three_word):
                three.append(three_word)
            letters4 = letters3.copy()
            letters4.remove(c)
            for d in letters4:
                four_word = a + b + c + d
                if check(dictionary[4], four_word):
                    four.append(four_word)
                letters5 = letters4.copy()
                letters5.remove(d)
                for e in letters5:
                    five_word = a + b + c + d + e 
                    if check(dictionary[5], five_word):
                        five.append(five_word)
                    letters6 = letters5.copy()
                    letters6.remove(e)
                    for f in letters6:
                        six_word = a + b + c + d + e + f 
                        if check(dictionary[6], six_word):
                            six.append(six_word)

print("One lettered words are:")
print(one)
print("Two lettered words are:")
print(two)
print("Three lettered words are:")
print(three)
print("Four lettered words are:")
print(four)
print("Five lettered words are:")
print(five)
print("Six lettered words are:")
print(six)