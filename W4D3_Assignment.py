# For homework please revisit 3 codewars problems and refactor your solution to improve their time complexity. 

# Please write out in a comment what the time and space complexity of each solution
# is based on what we talked about in class today.

#Exercise 1:

# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for vowel in sentence:
        if vowel in vowels:
            count += 1
    return count


input_string = "rangers"
result = get_count(input_string)
print(result)  

# This function has a timpe space complex of linear beacuse theres a single for loop and it 
# iterates through each letter of the string 

# Exercise 2: 

# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    vowels = "aeiouAEIOU"
    solution = ""
    for letter in string_:
        if letter not in vowels:
            solution += letter
    return solution
    
string_ = "This website is for losers LOL!"
print(disemvowel(string_))

# This function iterates through each carather of the string, for this reason is linear.

# Exercise 3:

def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and b + c > a and c + a > b:
            return True
    return False

triangle1 = is_triangle(3,4,5)
triangle2 = is_triangle(5,3,6)

print(triangle1)
print(triangle2)

# This function is Constant due to the fact that theres no For loop and also the values are just being compared ragarding of the values.

