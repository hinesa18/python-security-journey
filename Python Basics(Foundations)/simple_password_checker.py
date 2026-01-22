#Takes a user password and compares it to the password I preset and if it the same it will print it is correct

password = input("What is your password? ")
real_pass = "Hack3r"

if password == real_pass:
    print("That is correct! ")
else:
    print("That is not correct! ")

