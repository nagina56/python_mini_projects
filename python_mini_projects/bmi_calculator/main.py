def calculate_bmi(weight_kg, height_m):
    """Calculate BMI from weight (kg) and height (m)."""
    return weight_kg / (height_m ** 2)

def get_category(bmi):
    """Return BMI category and advice."""
    if bmi < 18.5:
        return "Underweight", "⚠️ You may need to eat more nutritious food."
    elif 18.5 <= bmi < 25:
        return "Normal weight", "Great! Keep maintaining a healthy lifestyle."
    elif 25 <= bmi < 30:
        return "Overweight", "⚠️ Consider a balanced diet and regular exercise."
    else:
        return "Obese", "🚨 Please consult a doctor for a health plan."

def get_float(prompt, min_val, max_val):
    """Prompt user for a valid float within range."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"  ⚠️  Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  ⚠️  Invalid input. Please enter a number.")

def main():

    print()
    print(" Python BMI Calculator ⚖️")
    print()

    while True:
        print(" [1] Calculate BMI")
        print(" [2] Quit")
        choice = input(" Choose an option: ").strip()

        if choice == "2":
            print("\n Stay healthy! Goodbye \n")
            break

        elif choice != "1":
            print(" ⚠️ Please enter 1 or 2.\n")
            continue

        print()
        print(" Choose unit system:")
        print(" [1] Metric   (kg, cm)")
        print(" [2] Imperial (lbs, inches)")
        unit = input(" Choose an option: ").strip()
        print()

        if unit == "1":
            weight = get_float(" Enter your weight (kg):    ", 1, 500)
            height_cm = get_float(" Enter your height (cm):    ", 50, 300)
            height_m = height_cm / 100

        elif unit == "2":
            weight_lbs = get_float(" Enter your weight (lbs): ", 1, 1000)
            height_in = get_float(" Enter your height (inches): ", 20, 120)
            weight = weight_lbs * 0.453592
            height_m = height_in * 0.0254

        else:
            print(" ⚠️ Invalid choice. Please try again.\n")
            continue
        
        bmi = calculate_bmi(weight, height_m)
        category, advice = get_category(bmi)

        # print()
        print("  ─────────────────────────────────")
        print(f"  Your BMI:    {bmi:.2f}")
        print(f"  Category:    {category}")
        print(f"  {advice}")
        print("  ─────────────────────────────────")
        # print()

        print(" BMI Scale:")
        print(" < 18.5   →  Underweight")
        print(" 18.5–24.9 → Normal weight")
        print(" 25–29.9  →  Overweight")
        print(" ≥ 30     →  Obese")
        print()

if __name__ == "__main__":
    main()