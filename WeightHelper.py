# Calculate body mass index, BMI
def calculate_BMI(wt, ht):

    try:
        if not isinstance(wt, (int, float)):
            raise ValueError("Invalid Case")
        if not isinstance(ht, (int, float)):
            raise ValueError("Invalid Case")

        if wt <= 0 or ht <= 0:
            raise ValueError("Invalid Case")

        bmi = round((wt / ((ht / 100) * (ht / 100))), 2)
        print("\nBMI :", bmi)
        return bmi

    except Exception:
        raise ValueError("Invalid Case")


# Get a category based on the BMI
def category_BMI(wt, ht):

    res = calculate_BMI(wt, ht)

    if res < 18.5:
        print("Underweight")
        stat = "Underweight"
    elif 18.5 <= res < 25:
        print("Normal weight")
        stat = "Normal weight"
    elif 25 <= res < 30:
        print("Overweight")
        stat = "Overweight"
    else:
        print("Obese")
        stat = "Obese"
    return stat
