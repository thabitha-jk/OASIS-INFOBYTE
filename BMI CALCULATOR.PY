def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers.")
    else:
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        print(f"Your BMI is {bmi:.2f}. You are classified as: {category}")
except ValueError:
    print("Please enter valid numbers.")
