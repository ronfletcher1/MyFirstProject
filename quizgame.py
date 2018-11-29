#      ==========Notes==========
# My first project was assigned afer a brief but extensive Command Line and Python training.
# The Python training consisted of developing a Pygame game.  While I understand the
# concepts and am able to follow/read the code, I still need help getting requirements 
# to the terminal.  
# My project is a Python Quiz game.  Inspiration for the code was picked up from
# https://codereview.stackexchange.com/questions/202532/python-multi-choice-quiz-with-a-score-to-count
# Folling the lead of the previous code, The initial project just runs through a series 
# of questions and allows the users to select the appropriate answer.I modified the 
# questions/ansewrs and added/subtracted dollars for correct/incorrect answers.  I also provide 
# the correct answer along with the explanation of the correct answer.
 
print ("Welcome to Python Quiz Game\n")
print ("*** Game Instructions *** ")
print ("Read each question carefully and select an answer, A, B, C, or D and press enter")
print ("Easy questions earn you $100 and tougher questions earn you $500\n")

name = raw_input("What is your name?  ")
print("Hello " + name + " Good Luck, You Got This!\n")
print("Let's begin by getting some quick cash in your wallet to start you off,\nHere's a real easy one for you...\n") 
wallet = 0
score = 0
score = int(score)
print("Sample Question ")
print ("What year was Python implemented?\n A. 1981 \n B. 1986 \n C. 1989 \n D. 1990 \n")
answerS = "C" 
responseS = raw_input("Your answer is:  ").upper()

if responseS != answerS:
    print("\n Sorry, that is incorrect!\n ")
    print("Python was invented in the late 1980's and implemented in December 1989. \nWell we thought is was easy enough, here's a benjamin for the try...")
    wallet = wallet + 100
else:
    print("You got it! " + responseS + " is correct!\n")
    print("Python was invented in the late 1980's and implemented in December 1989.\n")
    score = score + 0
if responseS == "C":
    wallet = wallet + 100

print("Your current score is " + str(score) + " out of 6 \n")
print("Your wallet balance is " + str(wallet) + " dollars \n")

print("Ready, Let's Go!!!\n \n")

print(" Question # 1:\n")
print ("What will be the output of the following code?\n \nprint type(type(int)) \n \n A. type 'int' \n B. type 'type' \n C. Error \n D. 0 \n")
answer1 = "B" 
response1 = raw_input("Your answer is:  ").upper()

if response1 != answer1:
    print("\n Sorry, that is incorrect!\n ")
    print(" Explanation: The type() function returns the class\n of the argument the object belongs to. \n Thus, type(int) returns which is \n of the type 'type' object. \n")
    wallet = wallet - 100
else:
    print("You got it! " + response1 + " is correct!\n")
    score = score + 1
if response1 == "B":
    wallet = wallet + 100

print("Your current score is " + str(score) + " out of 6 \n")
print("Your wallet balance is " + str(wallet) + " dollars \n")

print(" Question # 2:\n")
# https://www.geeksforgeeks.org/python-functions-question-5/
print ("What is called when a function is defined inside a class?\n A. Module \n B. Class \n C. Another Function \n D. Method \n")


answer1 = "D" 
response1 = raw_input("Your answer is:  ").upper()

if response1 != answer1:
    print("\n Sorry, that is incorrect! \n")
    wallet = wallet - 100
else:
    print("You got it! " + response1 + " is correct!\n")
    score = score + 1
if response1 == "D":
    wallet = wallet + 100

print("Your current score is " + str(score) + " out of 6 \n")
print("Your wallet balance is " + str(wallet) + " dollars \n")

print(" Question # 3:\n")
print ("What will be the output of the following code?\n \nprint 9//2 \n \n A. 4.5 \n B. 4.0 \n C. 4 \n D. Error \n")


answer1 = "C" 
response1 = raw_input("Your answer is:  ").upper()

if response1 != answer1:
    print("Sorry, that is incorrect! \n")
    print(" Explanation:  The '//' operator in Python returns the integer part of the floating number. \n")
    wallet = wallet - 100
else:
    print("You got it! " + response1 + " is correct!\n")
    score = score + 1
if response1 == "C":
    wallet = wallet + 100

print("Your current score is " + str(score) + " out of 6 \n " )
print("Your wallet balance is " + str(wallet) + " dollars \n ")

# if wallet >= 500:
#     print("Looks like you have enough cash in your wallet to move the the next level\n where the questions are harder and the value of each question hereafter is $500")
# else:
#     print("Sorry, you don't have enough money in your wallet\n You'll need to study and start again!\n")
# keep_going = raw_input("Would you like to continue? y/n ")
# if keep_going == "y":
#     print("High Level questions...")

# Question 1
print ("What will be the output for x?\n \n r = lambda q: q * 2 \n s = lambda q: q * 3 \n x = 2 \n x = r(x) \n x = s(x) \n x = r(x) \n print x \n \n A. 42 \n B. 14 \n C. 24 \n D. 22 \n")


answer1 = "C"
response1 = raw_input("Your answer is:  ").upper()

if response1 != answer1:
    print("\n Sorry, that is incorrect! \n")
    print("Explanation : In the above program r and s are lambda functions or anonymous functions \n and q is the argument to both of the functions. \n In first step we have initialized x to 2. \n In second step we have passed x as argument to the lambda function r \n this will return x*2 which is stored in x. \n That is, x = 4 now. Similarly in third step we have passed x \n to lambda function s, So x = 4*3. i.e, x = 12 now. \n Again in the last step, x is multiplied by 2 by passing \n it to function r. Therefore, x = 24.\n")
    wallet = wallet - 500
else:
    print("You got it! " + response1 + " is correct! \n")
    score = score + 1
if response1 == "D":
    wallet = wallet + 500

print("Your current score is " + str(score) + " out of 6 \n")
print("Your cash balance is " + str(wallet) + " dollars \n")

#Question 2
print ("What will be the output of the following code?\n i = 0 \n while i < 3: \n   print i \n   i++   \n   print i+1\n \n  A. 0 2 1 3 2 4\n  B. 0 1 2 3 4 5\n  C. Error\n  D. 1 0 2 4 3 5 \n")
# cash = 500
# score = 0
# score = int(score)

answer1 = "C" 
response1 = raw_input("Your answer is:  ").upper()

if response1 != answer1:
    print("Sorry, that is incorrect! \n")
    print("Explanation: There is no operator ++ in Python \n")
    wallet = wallet - 500
else:
    print("You got it! " + response1 + " is correct!\n")
    score = score + 1
if response1 == "C":
    wallet = wallet + 500

print("Your current score is " + str(score) + " out of 6 \n " )
print("Your cash balance is " + str(wallet) + " dollars \n ")

#Question 3
print ("What will be the output of the following code?\n  x = ['ab', 'cd'] \n for i in x: \n   i.upper() \n   print (x)\n \n  A. ['ab, CD']\n  B. ['ab, cd']\n  C. ['AB, CD']\n  D. ['AB, cd'] \n")
# cash = 500
# score = 0
# score = int(score)

answer1 = "B" 
response1 = raw_input("Your answer is:  ").upper()

if response1 != answer1:
    print("Sorry, that is incorrect! \n")
    print("Explanation: The function upper() does not modify a string in place, but it returns a new string which here isn't being stored anywhere. So we will get our orignal list as output \n")
    wallet = wallet - 500
else:
    print("You got it! " + response1 + " is correct!\n")
    score = score + 1
if response1 == "B":
    wallet = wallet + 500

print("Your current score is " + str(score) + " out of 6 \n " )
print("Your cash balance is " + str(wallet) + " dollars \n ")

