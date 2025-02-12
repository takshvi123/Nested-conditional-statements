u=int(input("Please enter the number of units"))
if u<=50:
    amount=u*2.60
    surcharge=25
elif u<=100:
    amount=u*3.25
    surcharge=35
elif u<=200:
    amount=u*5.26
    surcharge=45
elif u>200:
    amount=u*8.25
    surcharge=75
else:
    print("Please enter valid input ")

total=amount+surcharge
print("Your total bill is ",total)