sets = {6,8,3,9,8,4,3,9,3}
set= {4,6,9,2,0,1}
print(sets) #doesn't print repeated values


#set methods
print(sets.pop()) #remove a random value
sets.add(5) #add a new digit
print(sets)
sets.remove(6) #removes a digit
print(sets)
print(sets.union(set))
print(sets.intersection(set))

sets[0] = 1 #sets in immutable & hence this line throws an error

