# Palindrome is a word, phrase, or sequence that reads the same backward as forward, using stacks
# we want to determine if the word, phrease or sequence is a palindrome.

def isPalindrome(string):
    #This function will determine if the string inserted in a palindrome. The function will return true or false
    #depending if it is a palindrome (True) or if it's not (False).
    #Your code goes here
    stack = []
    string1 = str(string)
    reversedString = ""
    for char in string1:
        stack.append(char)
    while not (len(stack) == 0):
        reversedString += stack.pop()
    if reversedString == string1:
        return True
    else:
        return False


print(isPalindrome('civic')) # True
print(isPalindrome('banana')) # False
print(isPalindrome('saippuakivikauppias')) #True
print(isPalindrome(16461)) #True
