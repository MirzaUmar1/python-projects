pswrd = input("Password: ")
while True:
    rpswrd = input("Repeat password: ")

    if pswrd != rpswrd:
        print("They do not match!")
    elif pswrd == rpswrd:
        break
print("User account created!")
