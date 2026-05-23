import random


def get_winner(user, computer):
    if user == computer:
        return "draw"

    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    return "user" if rules[user] == computer else "computer"


def main():

    choices = ["rock", "paper", "scissors"]

    user_score = 0
    computer_score = 0

    print("\nWELCOME TO ROCK PAPER SCISSORS\n")

    while True:

        print("[1] Rock")
        print("[2] Paper")
        print("[3] Scissors")
        print("[4] Quit")

        user_input = input("\nChoose: ").strip()

        if user_input == "4":
            print("\nFinal Score")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!\n")
            break

        if user_input not in ["1", "2", "3"]:
            print("Invalid input. Try again.\n")
            continue

        user_choice = choices[int(user_input) - 1]
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        result = get_winner(user_choice, computer_choice)

        if result == "draw":
            print("Result: Draw")
        elif result == "user":
            print("Result: You Win")
            user_score += 1
        else:
            print("Result: Computer Wins")

        print(f"Score → You: {user_score} | Computer: {computer_score}\n")


if __name__ == "__main__":
    main()