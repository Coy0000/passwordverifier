password = input("Enter your password: ")

if len(password) < 8:
    print("Too short! Password should be at least 8 characters.")
elif password.isdigit():
    print("Almost there! Don't use only numbers.")
elif password.isalpha():
    print("Almost there! Don't use only letters.")
elif password.islower():
    print("Going strong! Add at least one uppercase letter.")
else:
    print("Good password!")
