"""Rock-Paper-Scissors Game

TASK 4

User Input: Prompt the user to choose rock, paper, or scissors.

Computer Selection: Generate a random choice (rock, paper, or scissors) for

the computer.

Game Logic: Determine the winner based on the user's choice and the

computer's choice.

Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.

Display the result, whether the user wins, loses, or it's a tie.

Score Tracking (Optional): Keep track of the user's and computer's scores for

multiple rounds.

Play Again: Ask the user if they want to play another round.

User Interface: Design a user-friendly interface with clear instructions and

feedback."""


import random

user_score = 0
computer_score = 0

while True:
    print("\n--- Rock-Paper-Scissors Game ---")
    user = input("Choose rock, paper, or scissors: ").lower()
    options = ['rock', 'paper', 'scissors']

    if user not in options:
        print("Invalid input. Try again.")
        continue

    computer = random.choice(options)

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}")

    again = input("Do you want to play again? (yes/no): ").lower()
    if again != 'yes':
        print("Thanks for playing!")
        break

