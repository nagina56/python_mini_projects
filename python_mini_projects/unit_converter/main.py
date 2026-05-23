def length_converter(value, source_unit, target_unit):
    meters_map = {
        "km": 1000, "m": 1, "cm": 0.01, "mm": 0.001,
        "mile": 1609.34, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254
    }

    value_in_meters = value * meters_map[source_unit]
    return value_in_meters / meters_map[target_unit]


def weight_converter(value, source_unit, target_unit):
    kg_map = {
        "kg": 1, "g": 0.001, "mg": 0.000001,
        "lb": 0.453592, "oz": 0.0283495, "ton": 1000
    }

    value_in_kg = value * kg_map[source_unit]
    return value_in_kg / kg_map[target_unit]


def temperature_converter(value, source_unit, target_unit):
    if source_unit == target_unit:
        return value

    if source_unit == "Celsius":
        return value + 273.15 if target_unit == "Kelvin" else (value * 9/5) + 32

    if source_unit == "Fahrenheit":
        return (value - 32) * 5/9 if target_unit == "Celsius" else (value - 32) * 5/9 + 273.15

    if source_unit == "Kelvin":
        return value - 273.15 if target_unit == "Celsius" else (value - 273.15) * 9/5 + 32


def speed_converter(value, source_unit, target_unit):
    ms_map = {
        "m/s": 1, "km/h": 0.277778,
        "mph": 0.44704, "knot": 0.514444
    }

    value_in_ms = value * ms_map[source_unit]
    return value_in_ms / ms_map[target_unit]


def area_converter(value, source_unit, target_unit):
    sqm_map = {
        "m²": 1, "km²": 1e6, "cm²": 0.0001,
        "ft²": 0.092903, "acre": 4046.86, "hectare": 10000
    }

    value_in_sqm = value * sqm_map[source_unit]
    return value_in_sqm / sqm_map[target_unit]


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️ Please enter a valid number.")


def select_unit(options, title):
    print(f"\n{title}")
    for index, unit in enumerate(options, 1):
        print(f"[{index}] {unit}")

    while True:
        try:
            choice = int(input("Select option: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            print("⚠️ Invalid selection.")
        except ValueError:
            print("⚠️ Enter a valid number.")


def main():

    print("\nPython Unit Converter 🔄\n")

    categories = {
        "1": "Length",
        "2": "Weight",
        "3": "Temperature",
        "4": "Speed",
        "5": "Area",
    }

    unit_options = {
        "Length": ["km", "m", "cm", "mm", "mile", "yard", "foot", "inch"],
        "Weight": ["kg", "g", "mg", "lb", "oz", "ton"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "Speed": ["m/s", "km/h", "mph", "knot"],
        "Area": ["m²", "km²", "cm²", "ft²", "acre", "hectare"],
    }

    converters = {
        "Length": length_converter,
        "Weight": weight_converter,
        "Temperature": temperature_converter,
        "Speed": speed_converter,
        "Area": area_converter,
    }

    while True:
        print("Select category:")
        for key, name in categories.items():
            print(f"[{key}] {name}")
        print("[6] Exit")

        option = input("Choose: ").strip()

        if option == "6":
            print("Goodbye")
            break

        if option not in categories:
            print("Invalid choice.\n")
            continue

        category_name = categories[option]
        units = unit_options[category_name]

        from_unit = select_unit(units, "Convert From:")
        to_unit = select_unit(units, "Convert To:")

        if from_unit == to_unit:
            print("⚠️ Same units selected.\n")
            continue

        value = get_number(f"Enter value in {from_unit}: ")

        result = converters[category_name](value, from_unit, to_unit)

        print(f"\nResult: {value} {from_unit} = {result:.4f} {to_unit}\n")

        again = input("Convert again? (y/n): ").lower()
        if again != "y":
            print("Goodbye")
            break


if __name__ == "__main__":
    main()