import random

Rock = '''"!!!THAT'S IT, MAN!!! KEEP THROWING THAT
HEAVY SHIT AT ME!!! THAT HEAVY SHIT!!!"   _____
        \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
          / ---._.---._.---\        /       /
          \||    '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/'''


Scissor = '''   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/'''

Paper = ''' _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|             '''


user_input = int(input("Type 0 for Rock, 1 for papaer or 2 for scissor"))

if user_input == 0:
    print(Rock)
elif user_input == 1:
    print(Paper)
elif user_input == 2:
    print(Scissor)
else:
    print("Type a valid input")

#Lets start a game####

computer_choice = random.randint(0, 2)

if computer_choice == 0 and user_input == 1:
    print(f"computer choice is Rock\n {Rock}\n you won!")
elif computer_choice == 0 and user_input == 2:
    print(f"computer choice is  Rock\n {Rock}\n You lose")
elif computer_choice == 0 and user_input == 0:
    print(f"computer choice is  Rock\n {Rock}\n Try again!")

elif computer_choice == 1 and user_input == 0:
    print(f"computer choice is Paper\n {Paper}\n you won!")
elif computer_choice == 1 and user_input == 1:  
    print(f"computer choice is Paper\n {Paper}\n Try again!!")
elif computer_choice == 1 and user_input == 2:
    print(f"computer choice is Paper\n {Paper}\n You lose")
elif computer_choice == 2 and user_input == 0:
    print("fcomputer choice is Scisor\n {Scissor}\n You lose")
elif computer_choice == 2 and user_input == 1:    
    print("fcomputer choice is Scisor\n {Scissor}\n you won!")
elif computer_choice == 2 and user_input == 2:
    print("fcomputer choice is Scisor\n {Scissor}\n Try again!")
    



