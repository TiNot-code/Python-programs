from random import seed
from random import randint

# choose the range 
print("""Choose your range / Difficulty:
    1: 0-1
    2: 1-10
    3: 1-100
""")

# input
guessedNumber = input()
# while true to check if input is between 1 & 3
while int(guessedNumber) > 3 or int(guessedNumber) < 0:
    print("Please Select a number between 1 and 3 !")
    guessedNumber = input()
else: 
    if int(guessedNumber) == 1:
        lowerDigit = 0
        higherDigit = 1
    elif int(guessedNumber) == 2:
        lowerDigit = 1
        higherDigit = 10
    else:
        lowerDigit = 1
        higherDigit = 100
# output
print("Select a number between " + str(lowerDigit) + " and " + str(higherDigit) + "!")
guessedNumber = input()
randomNumber = randint(lowerDigit, higherDigit)
print("The Number is: " + str(randomNumber))
if randomNumber == guessedNumber:
    ("Congratulation you guessed the Number!")
else:
    ("Try next Time! ")
