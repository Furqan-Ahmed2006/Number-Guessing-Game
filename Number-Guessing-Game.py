import random
def func():
  winning_number = random.randint(1,10)
  print("_________________Welcome To Number Guessing game__________________")
  print("_____Hint:Select a number From  1 to 10________")
  print("_________You Have 3 Chances to guess a Winning Number_______")
  has_won=False
  for i in range(0,3):
   guess_number=input("Enter your Guess_Number (1 to 10)=")
   while not guess_number.isdigit() or not (1 <= int(guess_number) <= 10):
            guess_number = input("Invalid input! Please enter a number from (1 to 10)=")
   guess_number=int(guess_number)
   if winning_number==guess_number:
        has_won=True
        print("_____Congratulations! You Win the Game:_______")
        break
   elif guess_number>winning_number:
        print("Hint:Try Again! Your Guessing Number is Too High:")
   else: 
        print("Hint:Try Again! Your Guessing number is too Low:")
  if not has_won:
    print("_____Ohh! You lose the Game_______")
    print("Winning Number is:",winning_number)
    print("______Better_Luck! NexT Time:_____")
func()
def confirm():
    while True:
     confirmation=input("Do you want to Play Again:(Yes/No):").lower()
     if confirmation=="yes" or confirmation=="no":
      match confirmation:
       case "yes":
         func()
       case "no":
         print("________Exit You from Game_________")
         break
     else:
        print("plese Enter a valid confirmation:(Yes/No):")  
confirm()