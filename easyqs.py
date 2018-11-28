cash = 500
score = 0
score = int(score)
#Question 1
print ("What will be the output of the following code?\n \nprint type(type(int)) \n \n A. type 'int' \n B. type 'type' \n C. Error \n D. 0 \n")


answer1 = "B" 
response1 = raw_input("Your answer is:  ").upper()

if response1 != answer1:
    print("\n Sorry, that is incorrect!\n ")
    print(" Explanation: The type() function returns the class\n of the argument the object belongs to. \n Thus, type(int) returns which is \n of the type 'type' object. \n")
    cash = cash - 100
else:
    print("You got it! " + response1 + " is correct!")
    score = score + 1
if response1 == "B":
    cash = cash + 100

print("Your current score is " + str(score) + " out of 5 \n")
print("Your cash balance is " + str(cash) + " dollars \n")

# Question 2
# https://www.geeksforgeeks.org/python-functions-question-5/
print ("What is called when a function is defined inside a class?\n \nprint type(type(int)) \n \n A. Module \n B. Class \n C. Another Function \n D. Method \n")
# cash = 500
# score = 0
# score = int(score)

answer1 = "D" 
response1 = raw_input("Your answer is(select the corresponding letter):  ")

if response1 != answer1:
    print("\n Sorry, that is incorrect! \n")
    cash = cash - 100
else:
    print("You got it! " + response1 + " is correct!")
    score = score + 1
if response1 == "D":
    cash = cash + 100

print("Your current score is " + str(score) + " out of 5 \n")
print("Your cash balance is " + str(cash) + " dollars \n")

#Question 3
print ("What will be the output of the following code?\n \nprint 9//2 \n \n A. 4.5 \n B. 4.0 \n C. 4 \n D. Error \n")
# cash = 500
# score = 0
# score = int(score)

answer1 = "C" 
response1 = raw_input("Your answer is:  ")

if response1 != answer1:
    print("Sorry, that is incorrect! \n")
    print(" Explanation:  The '//' operator in Python returns the integer part of the floating number. \n")
    cash = cash - 100
else:
    print("You got it! " + response1 + " is correct!")
    score = score + 1
if response1 == "C":
    cash = cash + 100

print("Your current score is " + str(score) + " out of 5 \n " )
print("Your cash balance is " + str(cash) + " dollars \n ")


