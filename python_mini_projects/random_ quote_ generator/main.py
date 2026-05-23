import random

QUOTES = {
    "Motivation": [
        ("The only way to do great work is to love what you do.", "Steve Jobs"),
        ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
        ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
        ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
        ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ],
    "Life": [
        ("Life is what happens when you're busy making other plans.", "John Lennon"),
        ("In the end, it's not the years in your life that count. It's the life in your years.", "Abraham Lincoln"),
        ("Life is either a daring adventure or nothing at all.", "Helen Keller"),
        ("You only live once, but if you do it right, once is enough.", "Mae West"),
        ("The purpose of our lives is to be happy.", "Dalai Lama"),
    ],
    "Wisdom": [
        ("The only true wisdom is in knowing you know nothing.", "Socrates"),
        ("Turn your wounds into wisdom.", "Oprah Winfrey"),
        ("The journey of a thousand miles begins with one step.", "Lao Tzu"),
        ("Knowing yourself is the beginning of all wisdom.", "Aristotle"),
    ],
    "Success": [
        ("Success usually comes to those who are too busy to be looking for it.", "Henry David Thoreau"),
        ("Opportunities don't happen. You create them.", "Chris Grosser"),
        ("Don't be afraid to give up the good to go for the great.", "John D. Rockefeller"),
    ],
    "Courage": [
        ("Courage is not the absence of fear, but the triumph over it.", "Nelson Mandela"),
        ("Be brave. Take risks. Nothing can substitute experience.", "Paulo Coelho"),
        ("Courage is one step ahead of fear.", "Coleman Young"),
    ],
}


def display_quote(quote, author, category):
    print("\n" + "-" * 50)
    print(f"Category: {category}")
    print(f'\n"{quote}"')
    print(f"\n        — {author}")
    print("-" * 50 + "\n")


def get_random_quote(category=None):
    if category and category in QUOTES:
        quote, author = random.choice(QUOTES[category])
        return quote, author, category
    else:
        cat = random.choice(list(QUOTES.keys()))
        quote, author = random.choice(QUOTES[cat])
        return quote, author, cat


def main():
    print("\nPYTHON RANDOM QUOTE GENERATOR")

    while True:
        print("\n[1] Random Quote")
        print("[2] Quote by Category")
        print("[3] Quit")

        choice = input("Choose an option: ").strip()

        if choice == "3":
            print("\nGoodbye! Stay inspired ✨\n")
            break

        elif choice == "1":
            quote, author, category = get_random_quote()
            display_quote(quote, author, category)

        elif choice == "2":
            categories = list(QUOTES.keys())

            print("\nAvailable Categories:")
            for i, cat in enumerate(categories, 1):
                print(f"{i}. {cat}")

            cat_choice = input("Choose category number: ").strip()

            if cat_choice.isdigit():
                index = int(cat_choice) - 1
                if 0 <= index < len(categories):
                    selected = categories[index]
                    quote, author, category = get_random_quote(selected)
                    display_quote(quote, author, category)
                else:
                    print("Invalid category choice.")
            else:
                print("Please enter a number.")

        else:
            print("Please choose 1, 2 or 3.")

        again = input("Get another quote? (y/n): ").strip().lower()
        if again != "y":
            print("\nGoodbye! Stay inspired ✨\n")
            break


if __name__ == "__main__":
    main()