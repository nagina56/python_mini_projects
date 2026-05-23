import random
import time

# Roll dice function
def roll_dice(num_dice=1, sides=6):
    return [random.randint(1, sides) for _ in range(num_dice)]

# Display results function
def display_roll(rolls, sides):
    print("\n🎲 Rolling", end="", flush=True)

    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)

    print()

    print(f"\n Results (d{sides}): {rolls}")

    if len(rolls) > 1:
        print(f" Sum:           {sum(rolls)}")
        print(f" Min Number:    {min(rolls)}")
        print(f" Max Number:    {max(rolls)}")

    # Special messages
    if sides in rolls:
        print(" Wow! You rolled the highest number!")

    if all(r == rolls[0] for r in rolls):
        print("Amazing! All dice matched!")

    print()

# Integer input validation
def get_int(prompt, min_val=1, max_val=100):

    while True:
        try:
            value = int(input(prompt))

            if min_val <= value <= max_val:
                return value

            print(f"⚠️ Please enter a number between {min_val} and {max_val}.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

# Main program
def main():

    COMMON_SIDES = [4, 6, 8, 10, 12, 20, 100]

    total_rolls = 0

    print()
    print("🎲 WELCOME TO THE PYTHON DICE ROLLER 🎲")
    1
    while True:

        print("\nOptions:")
        print("[1] Roll Dice")
        print("[2] Quit")

        choice = input("\nChoose an option: ").strip()

        # Quit program
        if choice == "2":
            print("\nThanks for playing Dice Roller!")
            print(f"🎲 Total Dice Rolls: {total_rolls}\n")
            break

        elif choice != "1":
            print("⚠️ Please enter 1 or 2.")
            continue

        # Number of dice
        num_dice = get_int(
            "\nHow many dice? (1–20): ",
            min_val=1,
            max_val=20
        )

        # Dice sides
        print(f"\nCommon dice types: {', '.join(f'd{s}' for s in COMMON_SIDES)}")

        while True:

            sides_input = input(
                "How many sides per die? (Example: 6 or d6): "
            ).lower().strip()

            # Allow d6 format
            if sides_input.startswith("d"):
                sides_input = sides_input[1:]

            try:
                sides = int(sides_input)

                if 2 <= sides <= 100:
                    break

                else:
                    print("⚠️ Please enter a number between 2 and 100.")

            except ValueError:
                print("Invalid input! Enter a valid number.")

        # Roll dice
        rolls = roll_dice(num_dice, sides)

        total_rolls += 1

        # Display results
        display_roll(rolls, sides)

        # Roll again
        again = input(f"🔁 Roll {num_dice}d{sides} again? (y/n): ").lower().strip()

        while again == "y":

            rolls = roll_dice(num_dice, sides)

            total_rolls += 1

            display_roll(rolls, sides)

            again = input(
                f"🔁 Roll {num_dice}d{sides} again? (y/n): "
            ).lower().strip()

# Start program
if __name__ == "__main__":
    main()