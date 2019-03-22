"""
Exam 1, problem 3. 35 Points Total

Modified by Dr. Brackin,
There are several parts of this problem that are straightforward.
I suggest that you start with those elements and add the more
difficult elements as time permits.
Every student should be able to print the string and the
length of the string.  If you don't remember how, LOOK at
your programming sessions!!!   
OMAR A. FAYOUMI.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2()


def reverseString(string):
    """
    Reverses the string that is passed to it as input argument
    and returns the reversed string.

    for example, the call reverseString('abc') will return 'cba'
    for example, the call reverseString('EYE') will return 'EYE'
    for example, the call reverseString('Python') will return
    'nohtyP'
    For full credit on this problem, you may NOT use this function.
    For full credit on this problem, you must write your own function.
    Remember, do NOT give your function the same name.
    """
    string = string[::-1]
    return string


def test_problem2():
    """
    Read the description of problem3 below.  One test case is provided for you below.
    You are to write 3 more test cases that are reasonable tests for the function.
    Remember, if you cannot write the reverse string code, you may use the one above.
    Remember, if you do write your own reverse string code, use a function name that
    is different than the one given above
    """
    #  Test case 1
    #  The given string is civic
    print('*********************************************')
    print('Test case 1 Expected: ')
    print('*********************************************')
    string_of_characters = 'civic'
    print('String entered: ',string_of_characters)
    print('Length of string: ',5)
    print('Number of alphabetic characters: ',5)
    print('Number of digits: ', 0)
    print('Reversed string is: civic')
    print('The user entered a palindrome')
    print()
    print('*********************************************')
    print('Test case 1 Actual: ')
    problem3(string_of_characters)
    print('*********************************************')
    # DONE: 2. Write at least three reasonable test cases below.
    #         Three excellent test cases are worth 10 points

    print('*********************************************')
    print('Test case 2 Expected: ')
    print('*********************************************')
    string_of_characters = 'l00lio'
    print('String entered: ', string_of_characters)
    print('Length of string: ', 6)
    print('Number of alphabetic characters: ', 4)
    print('Number of digits: ', 2)
    print('Reversed string is: oil00l')
    print('The user entered a normal string')
    print()
    print('*********************************************')
    print('Test case 2 Actual: ')
    problem3(string_of_characters)
    print('*********************************************')


    print('*********************************************')
    print('Test case 3 Expected: ')
    print('*********************************************')
    string_of_characters = '10LamaL01'
    print('String entered: ', string_of_characters)
    print('Length of string: ', 9)
    print('Number of alphabetic characters: ', 5)
    print('Number of digits: ', 4)
    print('Reversed string is: 10LamaL01')
    print('The user entered a palindrome')
    print()
    print('*********************************************')
    print('Test case 3 Actual: ')
    problem3(string_of_characters)
    print('*********************************************')


    print('*********************************************')
    print('Test case 4 Expected: ')
    print('*********************************************')
    string_of_characters = 'OmarAFayoumi00101'
    print('String entered: ', string_of_characters)
    print('Length of string: ', 17)
    print('Number of alphabetic characters: ', 12)
    print('Number of digits: ', 5)
    print('Reversed string is: 10100imuoyaFAramO')
    print('The user entered a normal string')
    print()
    print('*********************************************')
    print('Test case 4 Actual: ')
    problem3(string_of_characters)
    print('*********************************************')

    print('*********************************************')
    print('Test case 5 Expected: (EMPTY STRING) ')
    print('*********************************************')
    string_of_characters = ''
    print('String entered: ', string_of_characters)
    print('Length of string: ', 0)
    print('Number of alphabetic characters: ', 0)
    print('Number of digits: ', 0)
    print('Reversed string is: ')
    print('The user entered a palindrome')
    print()
    print('*********************************************')
    print('Test case 2 Actual: ')
    problem3(string_of_characters)
    print('*********************************************')




def problem3(string_of_characters):
    """
    What comes in:
          -- a string of characters that contains letters of the alphabet and/or numbers
        What goes out:
          Nothing
        Side effects:
        Prints, in this order, on separate lines,
      -- The string entered by the user
      -- The length of the string entered by the user
      -- The number of alphabetic characters in the string
      -- The number of digits (integers 0-9) in the string
      -- The reverse string entered by the user
      -- If the string is a palindrome - it prints, the user entered a
      -- palindrome
      -- If the string is not a palindrome - it prints, the user entered a
      -- normal string
      Nothing else should be printed.

        Examples:
          See the TEST cases for examples.
        Type hints:
          :type string_of_characters: string

    A palindrome is a phrase that reads the same backwards. For example,
    the words eye, madam are palindromes because they read the same
    backwards.

    To implement this function, you need to reverse a string. If you write
    your own method to reverse a string and solve the entire problem, you
    will get 35 points. If you use the provided method
    reverseString(string), you will get 30 points

    Here are some examples:
       string_of_characters = 'eye'
       String entered: eye
       Length of string: 3
       Number of alphabetic characters: 3
       Number of digits: 0
       Reversed string: eye
       The user entered a palindrome

       string_of_characters = 'abc1cba'
       String entered: abc1cba
       Length of string: 7
       Number of alphabetic characters: 6
       Number of digits: 1
       Reversed string: abc1cba
       The user entered a palindrome

       string_of_characters = 'a12b'
       String entered: a12b
       Length of string: 4
       Number of alphabetic characters: 2
       Number of digits: 2
       Reversed string: b21a
       The user entered a normal string
    """
    # DONE: 3. Implement this function.
    # To implement this function, you need to reverse a string.
    # If you write your own method to reverse a string and solve
    # the entire problem, you will get 25 points. If you use the
    # provided method reverseString(string),you will get 20 points
    print(string_of_characters)

    print(len(string_of_characters))


    numOfAlpha = 0
    for k in range(len(string_of_characters)):
        if string_of_characters[k].isalpha():
            numOfAlpha = numOfAlpha + 1
    print(numOfAlpha)


    numOfDig = 0
    for k in range(len(string_of_characters)):
        if string_of_characters[k].isdigit():
            numOfDig = numOfDig + 1
    print(numOfDig)


    ourRevString = ''
    for k in range(len(string_of_characters) - 1, -1, -1):
        ourRevString = ourRevString + string_of_characters[k]
    print(ourRevString)

    if ourRevString == string_of_characters:
        print('The user entered a palindrome')
    else:
        print('The user entered a normal string')




# -----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# -----------------------------------------------------------------------


if __name__ == '__main__':
    main()


