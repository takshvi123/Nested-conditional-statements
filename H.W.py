age = int(input("Enter the age: "))

if 0 <= age <= 1:
    category = "Infant"
elif 1 < age <= 3:
    category = "Toddler"
elif 3 < age <= 5:
    category = "Preschooler"
elif 5 < age <= 12:
    category = "Child"
elif 10 <= age <= 12:
    category = "Tween"
elif 13 <= age <= 15:
    category = "Early Teen"
elif 16 <= age <= 19:
    category = "Late Teen"
elif 18 <= age <= 25:
    category = "Young Adult"
elif 20 <= age <= 30:
    category = "Early Adulthood"
elif 25 <= age <= 30:
    category = "Post-Graduate Young Adult"
elif 40 <= age <= 59:
    category = "Middle Aged Adult"
elif 65 <= age <= 74:
    category = "Senior Citizen"
elif 75 <= age:
    category = "Elderly"
else:
    category = "Age out of range"

print(f"The person falls under the category: {category}")
