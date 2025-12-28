# x=0
# while x < 100:
#     if x % 2 == 1:
#         print(x)
#     x=x+1
# ## 25
from idlelib.run import MyHandler


# def prime():
# x = 47
#     if x % y == 0

# def numb():
#     num = 99999999999999999999
#     y = str(num)
#     res = 0
#     for z in y:
#         res += int(z)
#     print(res)
# # numb()
#
# s = "The cow is yummy"
# print(s[::-1])

# def multy(x):
#     string = "Js"
#     print(string*x)
# multy(6)

# def string(x,y):
#     if len(x) < 3:
#         print(x*y)
#     else:
#         print(x[0:3]*y)
# string("h",3)



# def count(s):
#
#     for i in range(len(s)-1):
#
#         if s[i] == "a" and s[i+1] == "a":
#             print("True")
#             return
#     print("false")
#
# count("apple")
# #28

# def pri(s):
#     result=""
#     for l in range(0,len(s),2):
#         result +=s[l]
#
#     print(result)
# pri("Hello")

# def word(s):
#     res=""
#     cou = 0
#     for l in range(1,len(s)+cou):
#         res+=s[:l]
#         cou = cou + 1
#     print(res)
# word("abc")
# def count_aa(s):
#     count = 0
#
#     for i in range(len(s)-1):
#
#         if s[i] == "a" and s[i+1] == "a":
#             count+=1
#
#     print(count)
#
# count_aa("aapllepaaa")

# def count(s):
#     res=""
#     cou = 0
#     word = s[len(s)-2:]
#     for l in range(len(s)-1):
#         if s[l:l+2] == word:
#             cou+=1
#     print(cou-1)
# count("abcdsab")
# 31

# def check(s):
#     a = [6,7,7,6,5,43,22,3,4]
#     for x in range(len(a)):
#         if s == a[x]:
#             print(True)
#             return
#     print("False")
# check(6)
# # 32

# def check(s):
#     a = [6,7,5,4,5,4,3,4455643,6,6,4,43,4,5,5,4,43,2,23456,54,567898,7654]
#     for x in range(0,4):
#         if s == a[x]:
#             print(True)
#             return
#     print("False")
# check(6)
# 33
# def check():
#     a = [1,2,4,5,8,5,24,4,4,4,3,2,1,2,3]
#     for y in range(len(a)-2):
#         if a[y] == 1 and a[y+1] == 2 and a[y+2] == 3:
#             print("True")
#             return
#     print("False")
# check()
# 34
# def com():
#     a = "abdggdgjjkuiyyhjhfkl"
#     b = "abffefgfdkuhgfddhgfd"
#     count = 0
#     for x in range(len(a)-1):
#         if a[x] == b[x] and a[x+1] == b[x+1]:
#             count+=1
#     print(count)
# com()
# 35
def remove_char_except_ends(s, ch):
    if len(s) <= 2:
        return s  # nothing inside to remove

    middle = s[1:-1].replace(ch, "")
    return s[0] + middle + s[-1]
print(remove_char_except_ends("asdfghytrsdfgtresdfgtasaadsfdaadsaawaawaaw","a"))















