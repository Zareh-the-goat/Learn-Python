def score_to_letter(x):
    if x >= 97 and x < 110 :
        return "A+"
    elif x >= 92 and x < 97:
        return "A"
    elif x > 92 and x <= 90:
        return "A-"
    elif x >= 86 and x < 90:
        return "B+"
    elif x > 86 and x <= 83:
        return "B"
    elif x >= 80 and x < 83:
        return "B-"
    elif x > 80 and x <= 77:
        return "C+"
    elif x >= 73 and x < 77:
        return "C"
    elif x > 73 and x <= 70:
        return "C-"
    elif x >= 67 and x < 70:
        return "D+"
    elif x > 67 and x <= 63:
        return "D"
    elif x >= 60 and x < 63:
        return "D-"
    elif x < 60 and x >= 0:
        return "Sorry you have a F"
    else:
        return "Invalid input"
# print(score_to_letter(82))
# score = score_to_letter(36)
# print(score)


def greet():
    a = int(input("What grade are you in? "))
    if a == 9:
        return"Welcome Freshmen have a nice year in your new school."
    elif a == 10:
        return"Hello Sophomore hope you loved you first year of high school."
    elif a == 11:
        return"Hello Junior! hope that this is the best year that you will ever have."
    elif a == 12:
        return"later Senior! We will miss you very much."
    else:
        return"There is no such name for that grade"

print(greet())
l = int(input("What grade did you get on your last exam? "))
print("So your letter grade is", score_to_letter(l))

