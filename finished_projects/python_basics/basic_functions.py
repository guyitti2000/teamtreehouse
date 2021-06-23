def calculate_total(*args):
    total = sum(args) 
    print(total)


def packer(*args):
    for val in args:
        print(val)

def unpacker():
    return ("Hungry", 2, 3)


first, last = input("Enter your full name: \n").split(' ')
print(first)
print(last)
#can now use these variables separately as they are now saved


var1, var2, var3 = unpacker()
print(var1)
print(var2)
print(var3)
print("\n")


calculate_total(20, 50, 30)
packer('Hi', 'there')
