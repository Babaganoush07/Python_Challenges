# Python Priciples
# https://pythonprinciples.com/challenges

'''
Capital indexes
Write a function named capital_indexes.
The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
'''
def capital_indexes(string):
    string = enumerate(string)
    lst = []
    for letter in string:
        if letter[1].isupper():
            lst.append(letter[0])
    return lst
    
print(capital_indexes("HeLlO"))

'''
Middle letter
Write a function named mid that takes a string as its parameter.
Your function should extract and return the middle letter.
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''
def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]

print(mid("abc"))
print(mid("aaaa"))

'''
Online status
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
Write a function named online_count that takes one parameter.
The parameter is a dictionary that maps from strings of names to the string "online" or "offline".
Your function should return the number of people who are online.
'''
def online_count(dictionary):
    online = 0
    for name, status in dictionary.items():
        if status == "online":
            online += 1
    return online
    
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))

'''
Randomness
Define a function, random_number, that takes no parameters. 
The function must generate a random integer between 1 and 100, both inclusive, and return it.
Calling the function multiple times should (usually) return different numbers.

For example, calling random_number() some times might first return 42, then 63, then 1.
'''
import random

def random_number():
    return random.randint(1,100)
    
print(random_number())

'''
Type check
Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
'''
def only_ints(a,b):
    return type(a) == int and type(b) == int
 
print(only_ints(1,'a'))

'''
Double letters
The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. 
For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. 
The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
'''
def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i+1]
        if letter1 == letter2:
            return True
    return False

print(double_letters("hello"))
