def numb():
    num = 99999999999999999999
    y = str(num)
    res = 0
    for z in y:
        res += int(z)
    print(res)
# numb()

def multy(x):
    string = "Js"
    print(string*x)
# multy(6)

def string(x,y):
    if len(x) < 3:
         print(x*y)
    else:
         print(x[0:3]*y)
 # string("h",3)


def count(s):

    for i in range(len(s)-1):

        if s[i] == "a" and s[i+1] == "a":
            print("True")
            return
    print("false")

# count("apple")
28

def pri(s):
    result=""
    for l in range(0,len(s),2):
        result +=s[l]

    print(result)
# pri("Hello")

# def word(s):
    res=""
    cou = 0
    for l in range(1,len(s)+cou):
        res+=s[:l]
        cou = cou + 1
    print(res)
# word("abc")

def count_aa(s):
    count = 0

    for i in range(len(s)-1):

        if s[i] == "a" and s[i+1] == "a":
            count+=1

    print(count)

# count_aa("aapllepaaa")

def count(s):
    res=""
    cou = 0
    word = s[len(s)-2:]
    for l in range(len(s)-1):
        if s[l:l+2] == word:
            cou+=1
    print(cou-1)
# count("abcdsab")
31

def check(s):
    a = [6,7,7,6,5,43,22,3,4]
    for x in range(len(a)):
        if s == a[x]:
            print(True)
            return
    print("False")
# check(6)
32

def check(s):
    a = [6,7,5,4,5,4,3,4455643,6,6,4,43,4,5,5,4,43,2,23456,54,567898,7654]
    for x in range(0,4):
        if s == a[x]:
            print(True)
            return
    print("False")
# check(6)
33

def check():
    a = [1,2,4,5,8,5,24,4,4,4,3,2,1,2,3]
    for y in range(len(a)-2):
        if a[y] == 1 and a[y+1] == 2 and a[y+2] == 3:
            print("True")
            return
    print("False")
# check()
34

def com():
    a = "abdggdgjjkuiyyhjhfkl"
    b = "abffefgfdkuhgfddhgfd"
    count = 0
    for x in range(len(a)-1):
        if a[x] == b[x] and a[x+1] == b[x+1]:
            count+=1
    print(count)
# com()
35

def remove_char_except_ends(s, ch):
    if len(s) <= 2:
        return s  # nothing inside to remove

    middle = s[1:-1].replace(ch, "")
    return s[0] + middle + s[-1]
# print(remove_char_except_ends("asdfghytrsdfgtresdfgtasaadsfdaadsaawaawaaw","a"))

def range(a,b):
    if a < 10 and a > -10 and b < 10 and b > -10:
        print(True)
    else:
        print(False)
# range(-5,7)
#36
def remove37(s):
    if s[1] == "h" and s[2] == "p":
       print(s[0] + s[3:])
# remove37("phpfacts")

def sumrange(a,b):
    if a + b <= 20 and a + b >= 10:
        print(30)
    else:
        print(a+b)
# sumrange(19,7)
40
def five(a,b):
    if a == 5 or b == 5:
        print(True)
    if a + b == 5 or a - b == 5 or b - a == 5:
        print(True)
    else:
        print(False)
# five(4,11)
41
def onemore(a):
    if a % 13 == 0 or a % 13 == 1:
        print(True)
    else:
        print(False)
# onemore(9)
#42
def check37(a):
    if a % 7 == 0 and a % 7 == 0:
        print(False)
    elif a % 7 == 0:
        print(True)
    elif a % 3 == 0:
        print(True)
    else:
        print(False)
# check37(45)
43
def check102(a):
    if a % 10 == -2 or a % 10 == -1 or a % 10 == 0 or a % 10 == 1 or a % 10 == 2:
        print(True)
    else:
        print(False)
# check102(22)
44
def check18(a,b):
    if a < 20 and a > 10 or b < 20 and b > 10:
        print(18)
    else:
        print(a+b)
# check18(6,13)
45
#Skip 46
def add(a,b,x):
    if a + b == x:
        print(True)
    else:
        print(False)
# add(1,2,5)
47
def gr(a,b,x):
    if a < b and b < x:
        print(True)
    else:
        print(False)
# gr(1,7,3)
#48
def strict(a,b,c,y):
    if y == "True" and a <= b and b <= c:
        print(True)
    elif y == "False" and a < b and b < c:
        print(True)
    else:
        print(False)
# strict(1,6,6,False)
49
def check(a,b,c):
    if a > 0 and b > 0 and c > 0:
        if a % 10 == b % 10:
            print(True)
        elif a % 10 == c % 10:
            print(True)
        elif b % 10 == c % 10:
            print(True)
        else:
            print(False)
    else:
        print(False)
# check(2456787654,2345678765432,1456789876543234)
50
def check(a,b,c):
    if a-20 <= b:
        print(True)
    elif b-20 <= a:
        print(True)
    elif a-20 <= c:
        print(True)
    elif c-20 <= a:
        print(True)
    elif b - 20 <= c:
        print(True)
    elif c-20 <= b:
        print(True)
    else:
        print(False)
# check(6,4,25)
51
def seven(a,b):
    if a == b:
        print(0)
    elif a % 7 == 0 and b % 7 == 0:
        if a > b:
            print(b)
        else:
            print(a)
    else:
        if a > b:
            print(a)
        else:
            print(b)
# seven(21,36)
52
def same(a,b):
    if a >= 10 and a <= 90 and b >=10 and b <=90:
        if a // 10 == b // 10:
            print(True)
        elif a// 10 == b % 10:
            print(True)
        elif a % 10 == b // 10:
            print(True)
        elif a % 10 == b % 10:
            print(True)
        else:
            print(False)
    else:
        print(False)
# same(68,42)
53
def add(x,y):
    if x > 0 and y > 0:
        if x // 10 == x+y //10:
            print(True)
        else:
            print(False)
# add(6,5)
#54
def check(a,b,c):
    if a == b:
        print(c)
    else:
        print(a+b+c)
# check(6,7,8)
55
