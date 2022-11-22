# Task 1 - hangman game

puzzle = "computer science"
my_solution = "******** *******"
life = 10
correct_letters = []
incorrect_letters = []
while life > 0 and puzzle != my_solution:
    print(my_solution)
    tip = input("Tip a new letter:\n")
    if len(tip) == len(puzzle):
        temp = my_solution
        my_solution = tip
        print("You try to guess the solution...and your guess is...")
        if my_solution == puzzle:
            print("Correct.")
        else:
            print("Not correct.")
            life -= 1
            print("This isn't in the puzzle. " + str(life) + " lives left.")
            my_solution = temp
    else:
        found_something = False
        for i in range(len(puzzle)):
            if puzzle[i] == tip:
                my_solution_list = list(my_solution)
                my_solution_list[i] = tip
                my_solution = "".join(my_solution_list)
                found_something = True
        if not found_something:
            incorrect_letters.append(tip)
            life -= 1
            print("This isn't in the puzzle. " + str(life) + " lives left.")
        else:
            correct_letters.append(tip)
        print("List of correct letters: " + str(correct_letters))
        print("List of incorrect letters: " + str(incorrect_letters))
if life > 0:
    print("Congratulations!")
else:
    print("Maybe next time..\n")