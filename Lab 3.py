#Gabe Gonzalez
#Lab 3
p = 1 
while p == 1:
  print('Welcome to the Flarsheim Guesser!')
  print()
  print('Please think of a number between and including 1 and 100.')
  rem_three = int(input('What is the remainder when your number is divided by 3?'))
  while rem_three < 0 or rem_three > 2:
    if rem_three < 0:
      print('The value entered must be 0 or greater')
      rem_three = int(input('What is the remainder when your number is divided by 3?'))
    elif rem_three > 2:
      print('The value entered must be less than 3')
      rem_three = int(input('What is the remainder when your number is divided by 3?'))
    
    
  


  rem_five = int(input('What is the remainder when your number is divided by 5?'))
  while rem_five < 0 or rem_five > 4:
    if rem_five < 0:
      print('The value entered must be 0 or greater')
      rem_five = int(input('What is the remainder when your number is divided by 5?'))
    elif rem_five > 4:
      print('The value entered must be less than 5')
      rem_five = int(input('What is the remainder when your number is divided by 5?'))



  rem_seven = int(input('What is the remainder when your number is divided by 7?'))
  while rem_seven < 0 or rem_seven > 6:
    if rem_seven < 0:
      print('The value entered must be 0 or greater')
      rem_seven = int(input('What is the remainder when your number is divided by 7?'))
    elif rem_seven > 6:
      print('The value entered must be less than 7')
      rem_seven = int(input('What is the remainder when your number is divided by 7?'))





  for i in range(101):
    if i %3 == rem_three and i %5 == rem_five and i %7 == rem_seven:
      print(f'Your number was {i}')
      print('How amazing was that?\n')
    else:
      ('Error: not found')

  again = input('Do you want to play again? Y to continue, N to quit ==> ')
  d = 1
  while d == 1:
    
    if again == "y" or again == "Y":
      d = 2
      continue
    elif again == "n" or again == "N":
      d = 2
      p = 3
      break
    else:
      again = input('Do you want to play again? Y to continue, N to quit ==> ')
