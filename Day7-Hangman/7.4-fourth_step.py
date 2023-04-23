import random
import hangman_art
import hangman_word

print(hangman_art.logo)


# print(stages[5])
#word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_word.word_list)
word_len = len(chosen_word.lower())
lives = len(hangman_art.stages) - 1
print(lives)

display = []

for i in range(word_len):
    display.append("_")

print(display) 

# while correct < word_len:
while display.count("_") > 0:
    if lives == 0:
        break
    guess = input("guess the letter:")
    if guess in display:
        print(f"you have already gussed letter {guess}")
    check = False
    for i in range(word_len):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
            check = True
    if check == False:            
        lives -= 1
    print(f"you have {lives} life left")
    print(hangman_art.stages[lives])                
    print(display)
if lives > 0:
    print("you win!")
else:
    print("you lose!")
    print(f"word is {chosen_word}")             



