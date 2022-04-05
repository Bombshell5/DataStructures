# Sets
## Introduction and Explanation 
  Sets are a very interesting data structure, sets are very similar to stacks or queues but the main difference is that sets don't care about order and you cannot repeat items. Meaning that in a set you will not find 2 of the same value. To declare a an empty set in python you do the following:
```python
empty_set= set()
``` 
However when declaring a set with objects you declare it with {} as shown:
```python
number_set = {1,2,3,4}
```
The main operations for sets are **add(data)** as the name describes it adds data to the set, **remove(data)** as the name describes it removes data from the set, there is a similar one called **discard()**, the main difference between discard() and remove(), is that when trying to use remove(data) when data is not in the set you will get an error, but when using discard() it simply ignores it and leaves it as it was.   
There are more operations using **| or union()**, **^ or symmetric_difference()**, **& or intersection()**, **- or difference()**.   

The beauty of sets is that the big O notation for any operation performed in a set is O(1), this is possible with a technique called "hashing", this technique allows us to obtain the value of an object, this is very useful when dealing with the index since there are objects that have similar hashing values.
![setsinPython](https://pynative.com/wp-content/uploads/2021/03/python-sets.jpg)

## Example 
```python
#Each student has a code containing three numbers, however there were two students that came an observe classes, when asked for their code, they made up one.
#the code is used to grade attendace and also for grading, please find out which were the codes that were made up....

english = {343, 674, 989, 766, 454, 376, 289, 274, 777, 301, 112, 778, 245, 477, 657}
math = {343, 674, 989, 766, 454, 376, 274, 301, 112, 778, 245, 477, 657, 289, 656}

#Answer 
print(f"The invented code are {english.symmetric_difference(math)}")

#or 
print(f"The invented codes are {english ^ math}")

```
## Problem #2 
```python
#Oh no! Somebody sneak into a movie they didn't pay for!! Apparently this person payed to go to Shrek but also enter to Men in Black that was
#right next to shrek. The number of the tickets are given please find the number of the ticket that is repeated for both movies. 

shrek = {3878, 9896, 1726, 6547, 5467, 1098, 7648, 8835, 2846, 4875, 6382, 1164, 8366, 8367, 9843, 9083, 1174, 7574, 6374, 3452, 9876, 5648, 5552}
menInBlack = {2384, 7623, 1379, 3278, 1983, 2945, 1239, 9834, 1093, 1058, 8923, 9543, 4023, 7835, 7823, 7648, 2942, 2553, 1240, 3578, 3848, 7569}

#Code goes here:

```
The answer of the solution is [here](https://github.com/Bombshell5/DataStructures/blob/main/solution_sets.py)

**Please make sure that you try to solve it first before looking at the answer.**

