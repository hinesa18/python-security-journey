password = "password"
x = 3 
for i in range(3):
    guess_pass = input("What is your password? ")
    if guess_pass == password:
        print("Welcome into your account. You got the password right")
        break
    else:
        x = x - 1
        print("Incorrect password. You have " + str(x) + " attempts left")
        
    if x == 0:
        print("You are now locked out from to many failed attemps")
        exit(-1)

