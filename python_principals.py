# Python Priciples
# https://pythonprinciples.com/challenges

'''
Capital indexes
Difficulty 2/10
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

'''
Middle letter
Difficulty 2/10
Write a function named mid that takes a string as its parameter.
Your function should extract and return the middle letter.
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''
def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]

'''
Online status
Difficulty 2/10
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

'''
Randomness
Difficulty 2/10
Define a function, random_number, that takes no parameters. 
The function must generate a random integer between 1 and 100, both inclusive, and return it.
Calling the function multiple times should (usually) return different numbers.

For example, calling random_number() some times might first return 42, then 63, then 1.
'''
import random

def random_number():
    return random.randint(1,100)

'''
Type check
Difficulty 2/10
Write a function named only_ints that takes two parameters. 
Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
'''
def only_ints(a,b):
    return type(a) == int and type(b) == int

'''
Double letters
Difficulty 3/10
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

'''
Adding and removing dots
Difficulty 3/10
Write a function named add_dots that takes a string and adds "." in between each letter. 
For example, calling add_dots("test") should return the string "t.e.s.t".
Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. 

For example, calling remove_dots("t.e.s.t") should return "test".
If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.
'''
def add_dots(string):
    return ".".join(string)

def remove_dots(string):
    return string.replace(".", "")

'''
Counting syllables
Difficulty 3/10
Define a function named count that takes a single parameter. 
The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.
'''
def count(string):
    return string.count("-") + 1

'''
Anagrams
Difficulty 3/10
Two strings are anagrams if you can make one from the other by rearranging the letters.
Write a function named is_anagram that takes two strings as its parameters. 
Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
'''
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

'''
Flatten a list
Difficulty 3/10
Write a function that takes a list of lists and flattens it into a one-dimensional list.
Name your function flatten. It should take a single parameter and return a list.

For example, calling:flatten([[1, 2], [3, 4]])
Should return the list: [1, 2, 3, 4]
'''
def flatten(lst):
    result = []
    for each in lst:
        result += each
    return result

'''
Min-maxing
Difficulty 3/10
Define a function named largest_difference that takes a list of numbers as its only parameter.
Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.
You may assume that no numbers are smaller or larger than -100 and 100.
'''
def largest_difference(num_list):
    return max(num_list) - min(num_list)

'''
Divisible by 3
Difficulty 3/10
Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.

For example, div_3(6) is True because 6/3 does not leave any remainder. However div_3(5) is False because 5/3 leaves 2 as a remainder.
'''
def div_3(num):
    return num % 3 == 0

'''
Tic tac toe input
Difficulty 4/10
Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:

1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |

    A   B  C
The board is represented as a 2D list:

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]
Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. 
To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].

Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). 
Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.
'''
def get_row_col(choice):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = choice[0]
    number = choice[1]
    row = int(number) - 1
    column = translate[letter]
    return (row, column)

'''
Palindrome
Difficulty 4/10
A string is a palindrome when it is the same when read backwards.
For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".

Write a function named palindrome that takes a single string as its parameter. 
Your function should return True if the string is a palindrome, and False otherwise.
'''
def palindrome(string):
    return string == string[::-1]

'''
Up and down
Difficulty 4/10
Define a function named up_down that takes a single number as its parameter. 
Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.

For example, calling up_down(5) should return (4, 6).
'''
def up_down(num):
    return (num-1, num+1)
print(up_down(5))

'''
Consecutive zeros
Difficulty 4/10
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.
'''

def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result

'''
All equal
Difficulty 4/10
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
'''
def all_equal(l):
    for char in l:
        if l[0] != char:
            return False
    return True

'''
Boolean and
Difficulty 4/10
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
'''

def triple_and(a, b, c):
    return a and b and c

'''
Writing short code
Difficulty 5/10
Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.

For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

What makes this tricky is that your function body must only contain a single line of code.
'''
def convert(lst):
    return [ str(each) for each in lst ]

'''
Custom zip
Difficulty 5/10
Define a function named zap. 
The function takes two parameters, a and b. These are lists.
Your function should return a list of tuples. 
Each tuple should contain one item from the a list and one from b.
'''
zaps = (
    [0, 1, 2, 3],
    [5, 6, 7, 8]
)

def zap(a,b):
    zap_list = []
    for i in range(len(a)):
        zap_list.append((a[i], b[i]))
    return zap_list

'''
Solution validation
Difficulty 5/10
The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

the code must contain the def keyword
otherwise return "missing def"
the code must contain the : symbol
otherwise return "missing :"
the code must contain ( and ) for the parameter list
otherwise return "missing paren"
the code must not contain ()
otherwise return "missing param"
the code must contain four spaces for indentation
otherwise return "missing indent"
the code must contain validate
otherwise return "wrong name"
the code must contain a return statement
otherwise return "missing return"
If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.
'''
def validate(string):
    if 'def' not in string:
        return "missing def"
    if ':' not in string:
        return "missing :"
    if '('+')' in string:
        return "missing param"
    if '(' not in string or ')' not in string:
        return "missing paren"
    if '    ' not in string:
        return "missing indent"
    if 'validate' not in string:
        return "wrong name"
    if 'return' not in string:
        return "missing return"
    return True

'''
List xor
Difficulty 5/10
Define a function named list_xor. 
Your function should take three parameters: n, list1 and list2.
Your function must return whether n is exclusively in list1 or list2.

In other words, if n is in both lists or in none of the lists, return False. 
If n is in only one of the lists, return True.

For example:
list_xor(1, [1, 2, 3], [4, 5, 6]) == True
list_xor(1, [0, 2, 3], [1, 5, 6]) == True
list_xor(1, [1, 2, 3], [1, 5, 6]) == False
list_xor(1, [0, 0, 0], [4, 5, 6]) == False
'''
def list_xor(n, list1, list2):
    if n not in list1 and n not in list2:
        return False
    if n in list1 and n in list2:
        return False
    return True
