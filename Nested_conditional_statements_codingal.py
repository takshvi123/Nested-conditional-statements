MC=input("Do u have a medical cause (Y/N) ? ")
if MC=="Y" or MC== "y":
    print("You are allowed to write the exam")
else:
    AP=float(input("Enter your atendance percentage :-"))
    if AP>=75:
        print("You are allowed to write the exam")
    else:
        print("You are not allowed to write the exam because you don't have * any medical cause * or enough attendance")    

