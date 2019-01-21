print("Please enter your name and password")
name = input()

if(name == 'Mary' or name == "Pulkit"):
    print("Hello freinds, please enter the password.")
    password = input()
    if(password == "Tabla"):
        print("Access granted")

    elif(password == "Pakhawaj"):
        print("Access granted but temporarily")
    else: print("You can try one more time")
    password = input()
    if(password == "Tabla"):
        print("Access granted")

    elif(password == "Pakhawaj"):
        print("Access granted but temporarily")
    else: print("You can try the last time")
    password = input()
    if(password == "Tabla"):
        print("Access granted")

    elif(password == "Pakhawaj"):
        print("Access granted but temporarily")
    else: print("Come after having your password")

else: print("Fuck Off!")

