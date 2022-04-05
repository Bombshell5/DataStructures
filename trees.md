# Trees
## Introduction and explanation
Before we start talking about trees, we need to talk about recursion. Recursion is a technique in which a function calls itself, if used improperly it could make a program go forever and break the program.
```python
def forever():
  print("forever")
  forever()
```
Let's proceed with trees!! We will talk about Binary Trees and Binary Search Trees. But first what is a tree? Trees are composed of nodes that are connected to each other by pointers. A tree can connect multiple nodes (more than 2) together. 
Trees are very useful when data becomes more complicated, because, when working with arrays and other linear data it becomes more complex as the data increases. However the structure of the tree helps the data be organized hierarchically therefore the process is not so complex. 
### Binary Tree 
As the name implies, it connects no more than two nodes.   

![trees](https://shunsvineyard.info/wp-content/uploads/2021/03/binary_tree_traversal-inorder.png)   
The top node is called root and a node that is connected to other nodes is called a **parent** node. The nodes that are connected to a parent node are called **child** nodes. And the nodes that don't connect any other nodes are called **leaf** nodes (just like a normal tree). 
### Binary Search Tree
A binay search tree (BST) is just like a binary tree but when adding data is follows a set of rules, these are by adding lower values to the left and bigger values to the right. Therefore it is neccesary to compare each node in order to know where to add. That way it becomes a sorted tree. 
The common operations for BST are insert(value) --> O(log n), remove(value) --> O(log n), contains(value)--> O(log n) or size() --> O(1). 
In the following example we are going to learn how to add values into our tree. 
## Example #1
```python
class Tree:

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Tree.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # empty spot
                node.left = Tree.Node(data)
            else:
                # Need to keep looking.
                self._insert(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = Tree.Node(data)
            else:
                # Need to keep looking.
                self._insert(data, node.right)
        elif data == node.data:
            print(f"{data} is already in the tree")
```
For the following problem, we are going to use the same tree we created for the insert function, please do not worry about the other functions, they are there for functionability, if you wish to know more about them please contact me. Contact info is [here](https://github.com/Bombshell5/DataStructures/blob/main/welcome.md)


## Problem #1 
```python
#Peter created a Binary Search Tree and wanted to number each of the leaves, however he got ditracted and lost count, please add to the contains function
# so Peter can check if he already set a leave as a certain number
class BST:
    """
    This is a BST (Binary Search Tree)
    """

    class Node:
        """
        Each node on the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # Empty spot
                node.left = BST.Node(data)
            else:
                # Keep looking
                self._insert(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                # Empty spot
                node.right = BST.Node(data)
            else:
                # Keep looking.  
                self._insert(data, node.right)
        elif data == node.data:
            print(f"{data} is already in the tree")
    

    def __contains__(self, data):
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        #Add code here
        pass

    def __iter__(self):

        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):  
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
  
        if node is not None:
            yield from self._traverse_backward(node.right) # It will start at right giving the biggest values first
            yield node.data
            yield from self._traverse_backward(node.left)


    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root
    
    def maximum(self, num1, num2):
        if num1 > num2:
            return num1 + 1
        else:
            return num2 + 1


# Test 
tree = BST()
tree.insert(6)
tree.insert(4)
tree.insert(3)
tree.insert(14)  
tree.insert(9)
tree.insert(10)
tree.insert(21)
tree.insert(6)
for number in tree:
    print(number)  # 3, 4, 6, 9, 10, 14, 21

print("The following numbers are the ones Peter wants to check")
print(3 in tree) # True
print(2 in tree) # False
print(9 in tree) # True
print(16 in tree) # False
print(9 in tree) # True
```
The solution is [here]()

