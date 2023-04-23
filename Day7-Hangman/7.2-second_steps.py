
import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_len = len(chosen_word.lower())

# print(chosen_word)
# print(word_len)

display = []

for i in range(word_len):
    display.append("_")

print(display) 

guess = input("guess the letter:")

# for i in chosen_word:
#     if i == guess:
#         print("right")
        
#     else:
#         print("wrong")  

for i in range(word_len):
    letter = chosen_word[i]
    if letter == guess:
        display[i] = letter      

print(display)






#Step 2

#Testing code

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
