groceries = ['roast beef', 'cabbage', 'tomato']

'''
#f string is something we can use to help us print variables inside of strings 
index = 1
#storing a counter number
for item in groceries:
    print(f'{index}. {item}')
    index+=1
'''
#learning enumerate, can do the same thing

for index, item in enumerate(groceries, 1):
    print(f'{index}. {item}')
