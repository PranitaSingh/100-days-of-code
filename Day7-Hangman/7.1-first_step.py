import random

# word_list = ["ardvark", "baboon", "camel"]
word_list = ["baboon"]

#randomly choose a word from word_list and assign it to variable called chosen_word.


chosen_word = random.choice(word_list)
word_length = len(chosen_word.lower())
print(chosen_word)

guess = input("guess the letter: ").lower()

# check if the letter user guess is one of the letter in chosen_word

found_indices = []

for i in range(word_length):
    if chosen_word[i] == guess:
        found_indices.append(i)
        print("right")
    else:
        print("wrong")
 

##Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display=[]

for i in range(word_length):
    display.append("_")


for idx in found_indices:
    display[idx] = guess

print(display)

# Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"]. 




# Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3     



