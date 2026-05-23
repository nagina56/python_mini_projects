import time
import sys

def format_time(seconds):
    """Convert seconds into HH:MM:SS format."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02}"

def countdown(total_seconds):
    """Run the countdown timer."""
    print()
    while total_seconds >= 0:
        time_str = format_time(total_seconds)
        print(f"  ⏳  {time_str}", end="\r", flush=True)
        time.sleep(1)
        total_seconds -= 1

    print(f"  🔔  Time's Up!          ")
    print()

def get_int(prompt, min_val=0, max_val=999):
    """Prompt user for a valid integer."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"  ⚠️  Enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  ⚠️  Invalid input. Please enter a whole number.")

def main():

    print()
    print(" Python Countdown Timer ⏱️")
    print()

    while True:
        print(" [1]  Start Timer")
        print(" [2]  Quit")
        choice = input("\n Choose an option: ").strip()

        if choice == "2":
            print("\n  Goodbye! ⏰\n")
            break
        elif choice != "1":
            print("  ⚠️  Please enter 1 or 2.\n")
            continue

        print()
        hours   = get_int("  Enter hours:   ", 0, 23)
        minutes = get_int("  Enter minutes: ", 0, 59)
        seconds = get_int("  Enter seconds: ", 0, 59)

        total = hours * 3600 + minutes * 60 + seconds

        if total == 0:
            print("\n  ⚠️  Please enter a time greater than 0.\n")
            continue

        print(f"\n  Starting countdown for {format_time(total)} ...")
        print("  (Press Ctrl+C to stop)\n")

        try:
            countdown(total)
        except KeyboardInterrupt:
            print("\n\n  ⛔  Timer stopped.\n")

        again = input("  Start another timer? (y/n): ").strip().lower()
        print()
        if again != "y":
            print("  Goodbye! ⏰\n")
            break

if __name__ == "__main__":
    main()