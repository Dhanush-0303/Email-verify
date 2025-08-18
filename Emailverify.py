email = input("Enter email: ")
if "@" in email and "." in email:
    print("Looks like a valid email")
else:
    print("Invalid email format")
