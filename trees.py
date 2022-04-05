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
        if data == node.data:
            return True
        elif data < node.data:
            # The data may be in the left side
            if node.left is None:
                # We found an empty spot
                return False
            else:
                # Need to keep looking.  Call _contains
                # recursively on the left sub-tree.
                return self._contains(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                return False
            else:
                # Need to keep looking.  Call _contains
                # recursively on the left sub-tree.
                return self._contains(data, node.right)

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

print("\n=========== PROBLEM 2 TESTS ===========")
print(3 in tree) # True
print(2 in tree) # False
print(9 in tree) # True
print(16 in tree) # False
print(9 in tree) # True





