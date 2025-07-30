# def av_grade():
#
#     grades = 0
#
#     i = 0
#     while i < 10:
#         grades += int(input("What is you last ten grades?"))
#
#         i=i+1
#
#
#     print(grades / 10)
#
# av_grade()

def sum():
    x = int(input("Enter 2 numbers"))
    y = int(input("Enter 2 numbers"))

    if x == y:
        return 3*(x+y)
    else:
        return x+y

# print(sum())

def num_eq_thi():
    a = int(input("Enter 2 numbers"))
    b = int(input("Enter 2 numbers"))

    if a + b == 30 or a == 30 or b == 30:
        return "True"
    else:
        return "False"
#
# print(num_eq_thi())


def num_ten():
    j = int(input("Enter a number"))

    if j <= 110 and j >= 90 or j <= 210 and j > 190:
        return "True"
    else:
        return "False"

# print(num_ten())


for r in range(0,100):
    print(r)
