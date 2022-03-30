#There is a stack of pancakes each of different flavors
pancakes = ['strawberries', 'blueberries', 'raspberries', 'cranberries', 'chocolate', 'buttermilk', 'banana']
# Tommy favorite pancake flavors are chocolate, banana and blueberries, please create a stack of new pancakes for Tommy from the stack of pancakes given,
# you should use pop() and append() "push" to create the new stack of pancakes. 
tommyPancakes = [] 

chocolate = pancakes.pop(4)
tommyPancakes.append(chocolate)
banana = pancakes.pop() # default is the last one
tommyPancakes.append(banana)
blueberries = pancakes.pop(1)
tommyPancakes.append(blueberries)

print(tommyPancakes) #chocolate, banana, blueberries









