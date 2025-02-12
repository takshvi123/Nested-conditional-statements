
medical_cause = input("Do you have a medical cause? (Y/N): ")
attendance = int(input("Enter your attendance percentage: "))

if medical_cause.upper() == 'Y':
    print("You are allowed to take the exam.")
else:
    if attendance > 75:
        print("You are allowed to take the exam.")
    else:
        print("You are not allowed to take the exam.")
