def calculate_bmi(weight, height):
    return weight / (height ** 2)

def calorie_categories(calories):
    if calories < 1500:
        return "low"
    elif 1500 <= calories <= 2200:
        return "normal"
    else:
        return "high"

def steps_category(steps):
    if steps < 3000:
        return "low number of steps"
    elif 3000 <= steps < 7000:
        return "moderate number of steps"
    else:
        return "high number of steps"

def age_group(age):
    if age < 18:
        return "teenager"
    elif 18 <= age <= 40:
        return "adult"
    else:
        return "senior adult"


def recommend_meals(bmi, cal_status, step_status, age_grp):
    # age=teenager
    if age_grp == "teenager":
        return {
            "Breakfast": ["Milk + banana", "Oats with dry fruits"],
            "Lunch": ["Dal rice", "Roti + paneer"],
            "Dinner": ["Vegetable khichdi", "Roti + sabzi"]
        }

    # age=adult
    if age_grp == "adult":
        # Underweight
        if bmi < 18.5:
            if cal_status == "low":
                return {
                    "Breakfast": ["Peanut butter and jam toast", "Banana smoothie"],
                    "Lunch": ["Paneer curry + rice", "Veg paratha + curd"],
                    "Dinner": ["Oats with milk", "Khichdi with ghee"]
                }
            else:
                return {
                    "Breakfast": ["Avocado toast", "Milk + dry fruits"],
                    "Lunch": ["Dal rice + sabzi", "Veg pulao"],
                    "Dinner": ["Paneer tikka", "Stuffed roti + sabzi"]
                }

        # Normal weight
        elif 18.5 <= bmi <= 24.9:
            if step_status == "low number of steps":
                return {
                    "Breakfast": ["Sprouts salad", "Poha"],
                    "Lunch": ["Roti + sabzi", "Mixed veg bowl"],
                    "Dinner": ["Grilled paneer", "Light dal + salad"]
                }
            else:
                return {
                    "Breakfast": ["Oats + fruits", "Upma"],
                    "Lunch": ["Dal khichdi", "Veg pulao"],
                    "Dinner": ["Chapati + sabzi", "Vegetable soup"]
                }

        # Overweight
        else:
            if cal_status == "high":
                return {
                    "Breakfast": ["Fruit bowl", "Green tea + soaked almonds"],
                    "Lunch": ["Boiled veggies", "Clear soup + salad"],
                    "Dinner": ["Moong dal chilla", "Low-oil roti + sabzi"]
                }
            else:
                return {
                    "Breakfast": ["Oats porridge", "Idli + sambar"],
                    "Lunch": ["Roti (less oil) + sabzi", "Upma"],
                    "Dinner": ["Vegetable soup", "Fruit salad"]
                }

    # age=senior adult
    if age_grp == "senior adult":
        return {
            "Breakfast": ["Oats + apple", "Idli + chutney"],
            "Lunch": ["Soft roti + sabzi (less oil)", "Dal + rice (light)"],
            "Dinner": ["Clear vegetable soup", "Fruit bowl"]
        }


# main program

age = int(input("Enter age: "))
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (meters): "))
calories = float(input("Enter today's calorie intake: "))
steps = int(input("Enter steps walked today: "))

bmi = calculate_bmi(weight, height)
cal_status = calorie_categories(calories)
steps_status = steps_category(steps)
age_grp = age_group(age)

print("\nYour BMI:", round(bmi, 2))
print("Calorie Level:", cal_status)
print("Activity Level:", steps_status)
print("Age Group:", age_grp)

meals = recommend_meals(bmi, cal_status, steps_status, age_grp)

print("\n--- Food Recommendations ---")
for meal, items in meals.items():
    print(f"\n{meal}:")
    for item in items:
        print("-", item)
