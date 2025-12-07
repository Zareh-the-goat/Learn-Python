cnn = open("hello.txt", "x")
cnn.close()
print("File created!")

cnn = open("hello.txt", "w")
cnn.write("Hello I am 12 Years old")
cnn.close()
print("Text added")

cnn = open("hello.txt" , "r")
print(cnn.readline())
cnn.close()
print("te")

import os
os.remove("hello.txt")
print("This file has been deleted :( ")
