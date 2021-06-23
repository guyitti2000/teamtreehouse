slice
count
del
append
insert
pop
remove
reverse








variable.count("string") 
#can find how many times a certain string is here

variable.index("string")
#will tell you where a string is located (index)



my_pets = ('dog', 'cat', 'cat', 'chicken', 'dog')

my_pets.index('dog') # 0
my_pets.index('chicken') # 3
my_pets.index('lizard') # ValueError: 'lizard' is not in list



nums = range(1, 10, 2)

nums.index(5) # 2
nums.index(10) # ValueError: 10 is not in list
nums.index(1) # 0





Sequence Operations Common to All Types
Concatenate
Attaches one sequence to the end of another

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

nums3 = nums1 + nums2 # [1, 2, 3, 4, 5, 6]
Count
Returns the number of times an item appears in a sequence

student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas.count(4.0) # 2
In
Returns boolean indicating whether item is in sequence

student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

3.2 in student_gpas # True
Index
Returns index of first occuring passed item

student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas.index(4.0) # 1
Len
Returns number of items in the sequence

my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash']

len(my_pets) # 4
Max
Returns largest item in sequence

student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

max(student_gpas) # 4.0
Min
Returns smallest item in sequence

student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

min(student_gpas) # 1.5
Multiply
Attaches a sequence to itself n number of times

nums1 = [1, 2, 3]

nums1 * 2 # [1, 2, 3, 1, 2, 3]
Not in
Returns a boolean indicating whether an item is not in a sequence

my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash']

'Jellybean' not in my_pets # True
Slice
Returns a portion of the original sequence

student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas[1:3] # [4.0, 3.2]
Mutable Sequence Only Operations
Append
Adds an item to the end of a sequence

my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash']

my_pets.append('Vera') # ['Scofield', 'Edel', 'Ernie', 'Squash', 'Vera']
Del
Deletes a slice from a sequence

my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash', 'Vera']

del my_pets[0:2] # ['Ernie', 'Squash', 'Vera']
Insert
Inserts an item into a sequence at the provided index

fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']

fruits.insert(2, 'kiwi') # ['apple', 'banana', 'kiwi', 'orange', 'pear', 'strawberry']
Pop
Removes item from sequence, but also retrieves it

fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']

apple = fruits.pop(0) # ['banana', 'orange', 'pear', 'strawberry'], apple = 'apple'
Remove
Removes item first occurrence of item from sequence

student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas.remove(4.0) # [2.5, 3.2, 2.9, 3.7, 1.5, 4.0]
Reverse
Reverses sequence in place

my_pets = ['Ernie', 'Squash', 'Vera']

my_pets.reverse() # ['Vera', 'Squash', 'Ernie']
