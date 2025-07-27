## It inserts the element inside the end of the array
arr = []
arr.append(5*8)

print(arr)

## It clears all the items inside the array
cool = [5,6,7,8]
cool.clear()
print(cool)

## Copy and pastes all the elements into line 14
hello2 = [3,6,8,5,"hi",5]
copyhello = hello2.copy()
print(copyhello)

## Counts how much "hi" is inside the peas bracket
peas = ["hi","cool","sad"]
x = peas.count("hi")
print(x)

## Extends the line of num2 and adds num1 on it
num1 = [4,6,8,9,88]
num2 = [44,6,6,76,5,6,7,6,6,8,75]

num2.extend(num1)
print(num2)

## Prints the position of cow
ani = ["pig","cow","lamb","dog","cat"]
index = ani.index("cow")
print(index)


## adds the number 5 in position 4
numb = [1,2,3,4,6,7,8,9,10]
numb.insert(4, 5)
print('List:', numb)


##removes the 9
pn = [2,3,9,5,7,9]
remove_element = pn.pop()
print('Updated List:', pn)

##removes the first line it meets in the array
pn2 = [9,2,3,5,7,9,9,9]
pn2.remove(9)
print('Updated List:__----__+HI', pn2)
