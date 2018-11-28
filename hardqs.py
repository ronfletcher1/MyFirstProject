cash = 500
score = 0
score = int(score)
# Question 1
print ("What will be the output for x?\n \n r = lambda q: q * 2 \n s = lambda q: q * 3 \n x = 2 \n x = r(x) \n x = s(x) \n x = r(x) \n print x \n \n A. 42 \n B. 14 \n C. 24 \n D. 22 \n")


answer1 = "C"
response1 = raw_input("Your answer is:  ").upper()

if response1 != answer1:
    print("\n Sorry, that is incorrect! \n")
    print("Explanation : In the above program r and s are lambda functions or anonymous functions \n and q is the argument to both of the functions. \n In first step we have initialized x to 2. \n In second step we have passed x as argument to the lambda function r \n this will return x*2 which is stored in x. \n That is, x = 4 now. Similarly in third step we have passed x \n to lambda function s, So x = 4*3. i.e, x = 12 now. \n Again in the last step, x is multiplied by 2 by passing \n it to function r. Therefore, x = 24.\n")
    cash = cash - 100
else:
    print("You got it! " + response1 + " is correct! \n")
    score = score + 1
if response1 == "D":
    cash = cash + 50

print("Your current score is " + str(score) + " out of 5 \n")
print("Your cash balance is " + str(cash) + " dollars \n")

#Question 2
print ("What will be the output of the following code?\n i = 0 \n while i < 3: \n   print i \n   i++   \n   print i+1\n \n  A. 0 2 1 3 2 4\n  B. 0 1 2 3 4 5\n  C. Error\n  D. 1 0 2 4 3 5 \n")
# cash = 500
# score = 0
# score = int(score)

answer1 = "C" 
response1 = raw_input("Your answer is:  ")

if response1 != answer1:
    print("Sorry, that is incorrect! \n")
    print("Explanation: There is no operator ++ in Python \n")
    cash = cash - 100
else:
    print("You got it! " + response1 + " is correct!")
    score = score + 1
if response1 == "C":
    cash = cash + 100

print("Your current score is " + str(score) + " out of 5 \n " )
print("Your cash balance is " + str(cash) + " dollars \n ")

#Question 3
print ("What will be the output of the following code?\n  x = ['ab', 'cd'] \n for i in x: \n   i.upper() \n   print (x)\n \n  A. ['ab, CD']\n  B. ['ab, cd']\n  C. ['AB, CD']\n  D. ['AB, cd'] \n")
# cash = 500
# score = 0
# score = int(score)

answer1 = "B" 
response1 = raw_input("Your answer is:  ")

if response1 != answer1:
    print("Sorry, that is incorrect! \n")
    print("Explanation: The function upper() does not modify a string in place, but it returns a new string which here isn't being stored anywhere. So we will get our orignal list as output \n")
    cash = cash - 100
else:
    print("You got it! " + response1 + " is correct!")
    score = score + 1
if response1 == "B":
    cash = cash + 100

print("Your current score is " + str(score) + " out of 5 \n " )
print("Your cash balance is " + str(cash) + " dollars \n ")