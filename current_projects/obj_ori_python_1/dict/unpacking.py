teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}

def print_teacher(dict):
    for key in dict: 
       print("key:", key, ", Value:", dict[key]) 



print_teacher(teacher) 
#this will get both keys and values returned


teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}

def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)


# when you pass the keyword (**"dic name")to a function, it unpack the dic to (key, value )
#like ('name':'Ashley') and assign it to the function parameter.
print_teacher(**teacher)
#this just returns the values
