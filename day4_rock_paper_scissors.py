from random import randrange

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  
winner = '''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

$$\     $$\                         $$\      $$\ $$\           
\$$\   $$  |                        $$ | $\  $$ |\__|          
 \$$\ $$  /$$$$$$\  $$\   $$\       $$ |$$$\ $$ |$$\ $$$$$$$\  
  \$$$$  /$$  __$$\ $$ |  $$ |      $$ $$ $$\$$ |$$ |$$  __$$\ 
   \$$  / $$ /  $$ |$$ |  $$ |      $$$$  _$$$$ |$$ |$$ |  $$ |
    $$ |  $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |$$ |$$ |  $$ |
    $$ |  \$$$$$$  |\$$$$$$  |      $$  /   \$$ |$$ |$$ |  $$ |
    \__|   \______/  \______/       \__/     \__|\__|\__|  \__|

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                                                              
'''
loser = '''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

$$\     $$\                         $$\                                    
\$$\   $$  |                        $$ |                                   
 \$$\ $$  /$$$$$$\  $$\   $$\       $$ |      $$$$$$\   $$$$$$$\  $$$$$$\  
  \$$$$  /$$  __$$\ $$ |  $$ |      $$ |     $$  __$$\ $$  _____|$$  __$$\ 
   \$$  / $$ /  $$ |$$ |  $$ |      $$ |     $$ /  $$ |\$$$$$$\  $$$$$$$$ |
    $$ |  $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ | \____$$\ $$   ____|
    $$ |  \$$$$$$  |\$$$$$$  |      $$$$$$$$\\$$$$$$  |$$$$$$$  |\$$$$$$$\ 
    \__|   \______/  \______/       \________|\______/ \_______/  \_______|

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                                                                               
'''
user_input = input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n>")
print("You choose:")

if user_input == '0':
    print(rock)
elif user_input == '1':
    print(paper)
else:
    print(scissors)
'''
rock 0 and scissors 2 -> rock 0 wins
paper 1 and rock 0 -> paper 1 wins
scissors 2 and paper 1 -> scissors 2 wins
'''
computer = randrange(2)
computer = str(computer)
print("Computer choose: ")
if user_input == '0' and computer == '2':
    print(scissors)
    print(winner)
elif user_input == '1' and computer == '0':
    print(rock)
    print(winner)
elif user_input == '2' and computer == '1':
    print(paper)
    print(winner)
elif user_input == '0' and computer == '1':
    print(paper)
    print(loser)
elif user_input == '1' and computer == '2':
    print(scissors)
    print(loser)
elif user_input == '2' and computer == '0':
    print(rock)
    print(loser)
else:
    print("Is a tie!")
input("Press any key to exit...")