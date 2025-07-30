def score_to_letter():
    y = input("What is your name? ")
    print("Hello", y)
    x = int(input("What did you get on your last test "))
    if x >= 97 :
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
    elif x < 60:
        return "F"
print("You got a", score_to_letter())