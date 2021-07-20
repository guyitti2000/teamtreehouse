'''
var.keys() 
# returns the keys
var.values()
# returns the values
sorted(var.keys/values())
#returns in lexigraphical ordering
'''


course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}
#print(course['teacher'])
course['stages'] = 2
#del(course['title'])


'''
for item in course:
    print(item)
    print(course[item])
'''
# these do not get both keys and values out

print(course.items())
# prints a LIST of tuples that have the elements of the key and the value

print('\n')

for item in course.items():
    print(item)
# references the current tuple it iterates through

for key, value in course.items():
    print(key)
    print(value)
# this unpacks the tuple and allows each tuples elements to be assigned a key and a value


