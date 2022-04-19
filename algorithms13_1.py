
# Code from:https://rosettacode.org/wiki/Markov_chain_text_generator#Procedural
# Accessed: 12/04/22

"""N0.2
Character based program to generate a new name
"""

import random, sys
import math

from collections import Counter

window_size = int(input("What is your desired window size? ")) # ask User to input desired window size
temperature = float(input("what is your desire temperature? ")) # ask User  to input temperature
length_size = int(input("Enter your desire name length size here>> ")) # ask User for name length

def makeregu(data, ful_context):
    '''Make a regular dict for given data.'''
    regular = {} #empty dict to hold regular pairs
    words = data
    index = ful_context # ful_context is window size idea
    
    # For every Nth char, where N is size ful_context + 1
    for word in words[index:]:
        print("word: ", word) # Inspect what word is (should be one char)
        # key will be the letters before the current element/char
        # No longer joined with space
        
        # Strip to remove the white space for the new line
        key = ''.join(words[index - ful_context:index]).strip()
        
        print("key: ", key) # Inspect key
        if key in regular:
            regular[key].append(word)
        else:
            regular[key] = [word]
        index += 1

    return regular


def countregular(regulars_dict):
    stats = {} #empty stats dict
    for key in regulars_dict.keys():
        #count each list of options per week
        stats[key] = Counter(regulars_dict[key])
    return stats

def highest_choice(counter, temp):
    #sort counter with highest freq choice first
    opt = counter.most_common()
    #return highest freq option [0], only word not count [0]
    return opt[math.floor((len(opt)-1)*temp)][0]

def makeful_string_pred(regular, length, temp):
    '''Use a given regular to make a ful_string.'''
    oldwords = random.choice(list(regular.keys())) #.split(' ')  # random starting words
    ful_string = ' '.join(oldwords)  #+ ' '

    for i in range(length):
        try:
            key = ''.join(oldwords)
            print("key:", key)

            newword = random.choice(regular[key])
            # newword = highest_choice(regular[key], temp)
            ful_string += str(newword) # + ' '
            oldwords = oldwords[1:] + str(newword)

        except KeyError:
            return ful_string
    return ful_string


#consuming the file inside the Brightspace folder and the file is called valid.title
# def all_main():
 
if __name__ == '__main__':
    with open("valid.title", encoding = "utf8") as f:
        data = f.read()
    
    mydata =data.replace("-","")
    regular = makeregu(mydata, window_size)
    # print(regular)
    # print(type(mydata))
    stats = countregular(regular)
    ful_string = makeful_string_pred(stats, length_size, temperature)
    print(ful_string)  
   


