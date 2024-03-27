import random
def guessingGame():
    score = 0
    print("Athan")
    return score

def addie():
    score = 0
    nam = input("What's your name: ")
    print(f"Hi {nam} Welcome to Addy")
    input("Say YES to play: ")
    end = False
    while not end:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        ans = num1 + num2
        userAns = (input(f'What is {num1} plus {num2}? '))
        if userAns != "":
            userAns = int(userAns)
            if userAns == ans:
                print(f"CORRECT, LETS GO AGAIN {nam}")
                score = score + 1
            else:
                print("WRONG, TRY AGAIN")
        else:
            end = True
    return score


def subbie():
    score = 0
    print("Lalita")
    return score

def multi():
    score = 0
    print("Bori")
    return score

def divvi():
    score = 0
    print("This is a game to help you learn division!")
    print("Type your answer to 2 decimal places")
    end = False
    while not end:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        ans = round(num1/num2,2)
        userAns = input(f"What is {num1} divided by {num2}? ")
        if userAns != "":
            userAns = float(userAns)
            if userAns == ans:
                score += 1
                print("Correct!")
            else:
                print("Incorrect, try again!")
        else:
            end = True


    return score

def noughtsAndCrosses():
    score = 0
    print("Jake")
    return score


total = 0
choice = "a"
while choice != "":
    print("Welcome to Cooler Math Games!")
    print("Please choose from the following\n1. Guessing Game\n2. Addition\n3. Subtraction\n4. Multiplication\n5. Division\n6. Noughts and Crosses")
    choice = input("What's your choice? Type a number 1-6. Type nothing to exit: ")
    if "1" in choice:
        total = total + guessingGame()
    elif "2" in choice:
        total = total + addie()
    elif "3" in choice:
        total = total + subbie()
    elif "4" in choice:
        total = total + multi()
    elif "5" in choice:
        total = total + divvi()
    elif "6" in choice:
        total = total + noughtsAndCrosses()
    print(f"Your current score is {total}")

print("Thanks for playing! See you next time")