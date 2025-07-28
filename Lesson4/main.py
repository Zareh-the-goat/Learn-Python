def sum(a, b):
    print("Starting your calculation")
    h = a + b
    print("The calculation of", a , "+", b, "Has ended" )
    return h

print(sum(2,3))


def num(i,d):
    while i < d:
        print(i)
        i=i+1

num(50,100)

def name(a):
    print("Hello", a, "how are you?")

name("Zareh")

def even(x):
    if x % 2 == 0:
        print("It is even!!!")
        return x
    else:
        print("False it is odd")
        return -1

result = even(0)
result2 = even(3)
result3 = even(8)
print(result)
print(result2)
print(result3)


def big(y,z,l):
    if y > z and y > l:
        print(y, "is the largest number")
    elif z > y and z > l:
        print(z, "Is the largest number")
    elif l > y and l > z:
        print(l, "Is the largest number")
    else:
        print("I do not know")


big(3,5,4)