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
