age = int(input("Enter your age: "))
membership = input("Enter your membership type (e.g., 'premium' or 'standard'): ")

if age > 18:
    if membership.lower() == "premium":
        print("You can access all premium content.")
    else:
        print("You need a premium membership to access this content.")
else:
    print("You need to be over 18 to access this content.")
