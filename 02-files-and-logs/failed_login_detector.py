#Pseudocode
#1. Open a file
#2. Read it line by line and if it is too many then print a warning message
#3. it will detect failed and login messages
#4. if it is normal it will print a normal message

FILE = 'auth.log'
KEYWORD_Failed = "failed"
KEYWROD_Login = "login"
failed_count = 0
login_count = 0
line_count = 0

with open(FILE, 'r') as file:
    for line in file:
        line_count = line_count + 1
        
        if KEYWORD_Failed in line.lower().strip():
            failed_count = failed_count + 1
        
        if KEYWROD_Login in line.lower().strip():
            login_count = login_count + 1 

if failed_count >= 3:
    print("Warning, your account has had " + str(failed_count) + " login attempts!")

print("Out of " + str(line_count) + " lines. Your account was logged into " + str(login_count) + " times. \nWith " + str(failed_count) + " failed login attempts")