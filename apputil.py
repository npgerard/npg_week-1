

# Neville Gerard
# Week 1 Exercises - Utility functions for palindrome and balanced parentheses checks

## includes
import re # Regular expression module


## function definitions

# my intention here was to create a function for cleaning the string in case we need to call it from other functions
# as opposed to writing the code multiple times in each function
def clean_string(input_string: str) -> str:
    '''Cleans the input string by removing non-alphabetic characters and converting to lowercase.'''
    return re.sub(r'[^a-z]', '', input_string.lower())



def is_palindrome(input_string: str) -> bool:
    '''Check if the input string is a palindrome.'''
    #clean the string before checking if it's a palindrome; 
    cleaned_string = clean_string(input_string)

    # Check if the cleaned string is equal to its reverse; [::-1] is a slicing technique to reverse a string
    return cleaned_string == cleaned_string[::-1]

## test cases with formatted output
test_string = "taco cat"
print("Input: '{}' -> Is Palindrome?: {}".format(test_string, is_palindrome(test_string)))

## test cases
test_string = "this should be fun!"
print("Input: '{}' -> Is Palindrome?: {}".format(test_string, is_palindrome(test_string)))

## test cases
test_string = "sit on a potato pan otis"
print("Input: '{}' -> Is Palindrome?: {}".format(test_string, is_palindrome(test_string)))


# for the () one, let's first check to see if the number of opening and closing parentheses are the same;
# then, strip out all of the characters except for open and close parentheses, then make sure the first is an open and the last is a close
# then, we can loop through the string and keep a counter that increments for every open paren and decrements for every close paren
#note that this is not just checking for a palindrome of parentheses character 

def balanced_parentheses(input_string: str) -> bool:
    '''Check if the parentheses in the input string are balanced.'''

    # First, check if the number of opening and closing parentheses are the same
    if input_string.count('(') != input_string.count(')'):
        return False

    # Strip out all characters except for parentheses using regex
    parentheses_only = re.sub(r'[^()]', '', input_string)
    # Check if the first character is '(' and the last character is ')'
    if parentheses_only and (parentheses_only[0] != '(' or parentheses_only[-1] != ')'):
        return False
    
    # if the above two conditions pass, then we check the balance of parentheses
    # Initialize a counter for open parentheses
    balance = 0
    # Loop through each character in the string
    for char in input_string:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0: # A closing parenthesis without a matching opening one
            break

    if balance != 0:
        return False
    else:
        return True


## test cases with formatted output
test_string = "(code))))((code))"
print("Input: '{}' -> Balance: {}".format(test_string, balanced_parentheses(test_string)))

test_string = "(code(code(code(code(code)))))"
print("Input: '{}' -> Balance: {}".format(test_string, balanced_parentheses(test_string)))

test_string = "(())()()((()))"
print("Input: '{}' -> Balance: {}".format(test_string, balanced_parentheses(test_string))) 