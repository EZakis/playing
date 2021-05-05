import random

print("~Rules of the game is bellow~ \n"
      + "Rock vs paper->Paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "Paper vs scissor->Scissor wins \n")
print("LET THE GAMES BEGIN.  \n "
      + "1 is for Rock, 2 is for Paper, 3 is for Scissors: \n")

while True:
    choice = int(input("Enter your turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    print("your input was: " + choice_name)
    print("\nNow its computer turn... %%%....")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print("Computer choice was: " + comp_choice_name)

    print(choice_name + "_==> <==_" + comp_choice_name)

    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("paper wins ==> ", end="")
        result = "paper"

    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("Rock wins ==>", end="")
        result = "Rock"
    else:
        print("scissor wins ==>", end="")
        result = "scissor"

    if result == choice_name:
        print("<== You win! ==>")
    else:
        print("<== Computer win! ==>")

    print("Replay? hit (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break

print("Thank you!")


def repeat(f, n, x):
    if choice_name == 0:
        return f(x)
    else:
        return repeat(f, n - 1, x)