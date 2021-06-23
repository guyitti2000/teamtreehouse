def print_teacher(**kwargs):
    #keyword args AKA var args
    #**kwargs will pack variable arguments into a dictionary, not a tuple! Packing positional arguments into a tuple is denoted by *args.
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_teacher(name='Ashley', job='Instructor', topic='Python', second_topic='JavaScript')
# passing multiple variable arguments and passing them into a dictionary, unlike positional args, the order doesn't matter and also var args are named
