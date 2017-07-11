
# coding: utf-8

# In[31]:

import random
def randomNumber():
    number = random.randint(1, 100)
    return number


# In[32]:

def game():
    greeting()
    global magicNumber
    magicNumber = randomNumber()
    global tries
    tries = 10
    while tries > 0:
        userNumber = askForInput()
        if(userNumber > magicNumber):
            print("Your guess is too high. Try again")
            tries = tries - 1
            print("Remember, you have %d tries remaining.", tries)
            if(tries <= 8):
                hints()
        elif(userNumber < magicNumber):
            print("Your guess is too low. Try again")
            tries = tries - 1
            print("Remember, you have %d tries remaining.", tries)
        else:
            print("Congratulations! You guessed the right number!")
    print("I'm sorry. You don't have any more tries.")


# In[33]:

def greeting():
    print("Welcome to Brett's Guessing Game!")
    print("Guess the number between 1 and 100")
    print("You'll get 10 tries.")
    print("If you don't guess the correct number after two guesses, you"
          "can press '0' for a random hint.")
    print("You get a maximum of 3 hints so use them wisely!")
    print("Each hint costs 2 tries. Be cautious.")
    print("Good luck!")


# In[34]:

def askForInput():
    userValue = int(input("What is your guess?: "))
    if(userValue < 0 or userValue > 100):
        print("Please input a valid input")
    else:
        return userValue


# In[35]:

def hints():
    userInput = input("Would you like any hints? [Y / N]")
    if(userInput == "Y" or userInput == "y"):
        print("Here are your hint options")
        print(" 0 - Is the number odd or even?")
        print(" 1 - The number is bigger than or equal the square of a number")
        print(" 2 - The number is smaller than or equal the square of a number")
        print(" 3 - Is the number a multiple of 5?")
        print(" 4 - Is the number a multiple of 2?")
        print(" 5 - Is the number a multiple of 3?")
        hintInput = int(input("Press the number for each hint:"))
        if(hintInput == 0):
            oddEvenCheck()
        if(hintInput == 1):
            biggerSquareCheck()
        if(hintInput == 2):
            smallerSquareCheck()
        if(hintInput == 3):
            multipleFiveCheck()
        if(hintInput == 4):
            multipleTwoCheck()
        if(hintInput == 5):
            multipleThreeCheck()


# In[36]:

def oddEvenCheck():
    tries = tries - 2
    oddEvenCheckNumber = int(magicNumber % 2)
    if(oddEvenCheckNumber == 0):
        print("The number is even")
    else:
        print("The number is odd")


# In[37]:

def biggerSquareCheck():
    square = 1
    biggerSquare = square * square
    while(biggerSquare < magicNumber):
        square = square + 1
        biggerSquare = square * square
    square = square - 1
    tries = tries - 2
    print("The number is bigger than or equal to the square of the number %d", square)


# In[38]:

def smallerSquareCheck():
    square = 10
    smallerSquare = square * square
    while(magicNumber < smallerSquare):
        square = square - 1
        smallerSquare = square * square
    square = square + 1
    tries = tries - 2
    print("The number is smaller than or equal to the square of the number %d", square)


# In[39]:

def multipleFiveCheck():
    tries = tries - 2
    fiveCheck = False
    fiveCheckNumber = magicNumber % 5
    if(fiveCheckNumber == 0):
        fiveCheck = True
        print("The number is a multiple of five")
    else:
        print("The number is not a multiple of five")


# In[40]:

def multipleTwoCheck():
    tries = tries - 2
    twoCheckNumber = magicNumber % 2
    if(twoCheckNumber == 0):
        print("Your number is a multiple of two.")
    else:
        print("Your number is not a multiple of two.")


# In[41]:

def multipleThreeCheck():
    tries = tries - 2
    threeCheckNumber = magicNumber % 3
    if(threeCheckNumber == 0):
        print("Your number is a multiple of three.")
    else:
        print("Your number is not a multiple of three.")


# In[ ]:

game()


# In[ ]:



