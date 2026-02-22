questions = ["What is 42*87?",
        "What is the capital of Maine?",
        "What is the human species that was just like us and is the shortest human?",
        "What is 375*786?"]

options = [["a. 2657" , "b. 3654", "c.4345"],
           ["a. Agust", "b. Augusta" , "c. Maryland" ],
           ["a.Homo sapians","b.Homo erectus","c.Neanderthal "],
           ["a.29750","b.26054","c.29940"]]
answers = ["b","b","c","a"]

score = 0

for x in range (len(questions)):
    print(f"question {x+1}:{questions[x]}")
    for option in options[x]:
        print(option)
    y = (input("Type here "))

    if y == answers[x]:
            print("Correct!")
            # score += 1
    else:
        print("Sorry you are incorrect :(")

# print("Your score is", score, "out of 4")