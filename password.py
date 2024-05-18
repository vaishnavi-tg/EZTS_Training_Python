password="secret"
while True:
    user_input=input("Enter the password:")
    if user_input==password:
        print("Welcome!You've entered the correct password")
        break
    else:
        print('Incorrect password.Please try again')