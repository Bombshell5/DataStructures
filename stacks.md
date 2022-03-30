# Stacks
## Introduction and explanation 
  We are going to be learning about stacks. Stacks are a really useful type of data structure since they offer order by implemeteting LIFO (Last-In-First-Out). As described the first item that goes in a stack is the one that will come out last.  
  The main operations of this data structure is ***push*** and ***pop***. Push(*data*) as it sounds will add *data* to the top of the stack, in Python push() is used as append(). Pop() will remove the element from the top of the stack. Pop() can also be used with an index, meaning if you put pop(0), it will delete the first item, when using it without a number the default is to delete the last one. For a better representation look at the image below
  
  ![Stacks](https://www.tutorialspoint.com/data_structures_algorithms/images/stack_representation.jpg)
  
  
  ## Example Problem #1 
  ```python
  #There is a stack of pancakes each of different flavors
pancakes = ['strawberries', 'blueberries', 'raspberries', 'cranberries', 'chocolate', 'buttermilk', 'banana']
# Tommy favorite pancake flavors are chocolate, banana and blueberries, please create a stack of new pancakes for Tommy from the stack of pancakes given,
# you should use pop() and append() "push" to create the new stack of pancakes. 
tommyPancakes = [] 
#Your code goes here

print(tommyPancakes)  #[chocolate, banana, blueberries]

  ```
  The solution for this problem can be found [here](https://github.com/Bombshell5/DataStructures/blob/main/stacks01_solution.py)
  
  ## Example Problem #2
  ```python
  #Palindrome is a word, phrase, or sequence that reads the same backward as forward, using stacks
    #we want to determine if the word, phrease or sequence is a palindrome.
    
    def isPalindrome(string):
    #This function will determine if the string inserted is a palindrome. The function will return true or false
    #depending if it is a palindrome (True) or if it's not (False).
    #Your code goes here
      return

    print(isPalindrome('civic')) # True
    print(isPalindrome('banana')) # False
    print(isPalindrome('saippuakivikauppias')) #True
    print(isPalindrome(16461)) #True
    
  ```
  The solution for this problem can be found [here](https://github.com/Bombshell5/DataStructures/blob/main/Stacks02_solution.py)
  
  
    
  
