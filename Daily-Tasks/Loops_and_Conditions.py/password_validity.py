def is_valid_password(password):
    if len(password)<6 or len(password)>12:
        return False
    if not any(char.islower()for char in password):# At least one lowercase
        return False
    if not any(char.isupper()for char in password): # At least one uppercase
        return False
    if not any(char.isdigit()for char in password): # At least one digit
        return False
    if not any(char in "!@#$%^&*" for char in password):# At least one special character
        return False
    return True
password=input("enter a string:")
if is_valid_password(password):
    print("password is valid")
else:
    print("password is invalid")

    
        