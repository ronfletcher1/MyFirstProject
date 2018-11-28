# import pygame
# pygame.init()
# screen_size = (512,480)
# pygame_screen = pygame.display.set_mode(screen_size)
# pygame.display.set_caption("Python Quiz")
# #start_button = Start_Button(pygame_screen)
# game_on = True
# game_start = False



print ("What year was Python invented?")
print (" A: Late 1970s B: Early 1980s C: Late 1980s D: Early 1990s")
#answer = raw_input
#Convert the 0 into a number so we can add scores
cash = 500
score = 0
score = int(score)
#user = name
#Ask user for their name
name = raw_input("What is your name?  ")
# name = name.title()
print("Hello " + name + " Welcome to PyQuiz! \n You will be presented with 5 questions. \n Enter the appropriate number to answer the question\n Good luck!")

#Question1

print ("What will be the output for x?\n r = lambda q: q * 2 \n s = lambda q: q * 3 \n x = 2 \n x = r(x) \n x = s(x) \n x = r(x) \n print x \n A. 42 \n B. 14 \n C. 24 \n D. 22")


answer1 = "D"
response1 = raw_input("Your answer is:  ")

if response1 != answer1:
    print("Sorry, that is incorrect!")
    cash = cash - 100
else:
    print("You got it! " + response1 + " is correct!")
    score = score + 1
if response1 == "D":
    cash = cash + 50

print("Your current score is " + str(score) + " out of 5")
print("Your cash balance is " + str(cash) + " dollars")

keep_going = raw_input("Would you like to continue? y/n")
if keep_going == "y":
    print("Next question...")

#Question2

print ("What will print for x?\n r = lambda q: q * 2 \n s = lambda q: q * 3 \n x = 2 \n x = r(x) \n x = s(x) \n x = r(x) \n print x \n 1. 42 \n 2. 14 \n 3. 24 \n 4. 22")


answer1 = 24
response1 = input("Your answer is:  ")

if response1 != answer1:
    print("Sorry, that is incorrect!")
    cash = cash - 100
else:
    print("You got it! " + str(response1) + " is correct!")
    score = score + 1
if response1 == 24:
    cash = cash + 50

print("Your current score is " + str(score) + " out of 5")
print("Your cash balance is " + str(cash) + " dollars")