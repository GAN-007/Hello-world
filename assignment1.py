#This is the ticket assignment
"""WE WILL NEED ;
Age variance variables
messege after age variance
ie allow /disallow
Then ticket payment variance
ie Amount per ticket
message of sucssesful purchase
balance/ change if any.
A goodbye message at the end."""
#This part is cordial
print("Enter your name:")
x = input()
print("Hello, " + x)
#this part deals with age
Age =18

print("Enter your Age:")
Age = input()
print("Your age is  " + Age)
if int(Age)>=18:
  print("Welcome to the show")
else:
  print("Underage")

   #TICKETING

   #deposit
print("Enter your amount:")
y = input()
print(" Your deposit is " + y)
#ticket
ticket=200
bal = int(y)-int(ticket)
loss =  int(ticket) - int(y)

if ticket>=200:

  print(" Your balance is")
  print("your bal is" and bal)
else:
  print("less funds with")
  print("insufficient funds, less with " + loss)

#leaving remarks
print("Thank you for purchasing with us . GOOD BYE ;)")
  