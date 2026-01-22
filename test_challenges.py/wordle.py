import random

def guess():
    while True:
        word = input("What is your guess? ").lower().strip()
        if not len(word) == 5:
            print("Your word needs to be 5 letters long. ")
            continue
        else:
            break
    return word

def checker(y):
    for i in range(5):
        print(wordle[i])
        if wordle[y] == real_word[i] and y == i:
            #That letter is correct and in the right spot
            print("That letter is correct and in the right spot: " + str(i +1))
            break
        elif wordle[y] in real_word and not :
            #This letter is correct but not in the right spot
            print("This letter is right but not in the right spot: " + str(i + 1))
            break
        else:
            #This letter is not correct
            print("This letter is not correct: " + str(i + 1))
            break

    


words = ["items", "steve", "witch"]

word_picker = random.randint(0, (len(words) - 1) )
print(words[word_picker])
real_placeholder = words[word_picker]
real_word = list(real_placeholder)
print(real_word)

x = 5
for i in range(5):
    print("You get " + str(x) + " guesses!! ")
    x = x - 1
    wordle = list(guess())
    print(wordle)
    for m in range(5):
        checker(m)
