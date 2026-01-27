#Keyword logger
#This will open up a log file and read it line by line
#It will be looking for certain words such as "Failed" etc. 
#Count how many times the word pops up
#Show the user how many times the word showed up

#Constraints:
#1. Use no lists
#2. Use no functions
#3. Use no classes
#4. Use no regex
#5. Use no external libraries
#6. Use basic file handling only
#7. Logic must be linear(Top > Bottom)
#8. One Script file only

#Pseudocode:
#It will read the contents of log.txt
#It will run line by line checking for the keyword that we put for it to find
#Everytime the keyword is found the counter goes up by 1
#After it goes and checks the entire file it will print how many times the keyword showed up

KEYWORD = "failed"
FILE = 'log.txt'
counter = 0

with open(FILE, 'r') as file:
    for line in file:
        #print(line)
        if KEYWORD in line.strip().lower():
            counter = counter + 1

print("The keyword shows up " + str(counter) + (" times."))