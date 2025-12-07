# def numw(x,y):
#     print(x*y)
#
# numw("he",3)


z = []

for y in range(1,6):
    x = input("Give 5 words")
    z.append(x)
print(y)

longest = z[0]
shortest = z[0]

for y in z:
    if len(y) > len(longest):
        longest = y

print(longest)

for y in z:
    if len(y) < len(shortest):
        shortest = y
print(shortest)



