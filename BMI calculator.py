# BMI calculator
weight = float(input('Enter your weight in kilograms: '))
height_ft = float(input('Enter your height in feet: '))



height_m = height_ft * 0.3048



bmi = weight / (height_m ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"


print("\n--- Results ---")
print(f"Weight: {weight} kg")
print(f"Height: {height_m:.2f} meters (converted from {height_ft} feet)")
print(f"Your BMI is: {bmi:.2f}")

print(f"Category: {category}")
