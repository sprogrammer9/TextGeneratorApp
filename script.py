#import statements here random and string libraries 
import random, string 

 #variable vowels created 
vowels = 'aeiou'

# variables consonant
consonants = 'bcdfghjklmnpqrstvwxyz'

# variable letters contains all the letters of the ascii alphabets in lowercase
letters = string.ascii_lowercase

# this print statement prompts the user to select the combination of the words they want (vowels, consonants or letter)
letterInputOne = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ") 
letterInputTwo = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ")
letterInputThree = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ")

# the generator function to generate the words
def generator():
    # conditional statement for the first letter
    if letterInputOne == 'v':
        letter1 = random.choice(vowels)
    elif letterInputOne == 'c':
        letter1 = random.choice(consonants)
    elif letterInputOne == 'l':
        letter1 = random.choice(letters)
    else:
        letter1 = letterInputOne

    # conditional statement for the second letter
    if letterInputTwo == 'v':
        letter2 = random.choice(vowels)
    elif letterInputTwo == 'c':
        letter2 = random.choice(consonants)
    elif letterInputTwo == 'l':
        letter2 = random.choice(letters)
    else:
        letter2 = letterInputTwo

    # conditional statement for the third letter
    if letterInputThree == 'v':
        letter3 = random.choice(vowels)
    elif letterInputThree == 'c':
        letter3 = random.choice(consonants)
    elif letterInputThree == 'l':
        letter3 = random.choice(letters)
    else:
        letter3 = letterInputThree

#name is the addition of all the generated letters
    name = letter1 + letter2 + letter3 
# the variable name is then returned from the function here
    return(name) 

# this is a loop that prints the generated words 20 times
for i in range(20): 
    print(generator()) # the function 'generator' is printed here