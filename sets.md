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

The beauty of sets is that the big O notation for any operation performed in a set is O(1), this is possible with a technique called "hashing", this technique allows us to obtain the value of an object, this is very useful when dealing with the index since there are object that have similar hasing values "Add more about chaining and sparse list" . 
![setsinPython](https://pynative.com/wp-content/uploads/2021/03/python-sets.jpg)

## Example Problem #1
```python

```
## Example Problem #2
```python

```
