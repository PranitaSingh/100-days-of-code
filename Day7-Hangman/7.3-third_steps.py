import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_len = len(chosen_word.lower())

display = []

for i in range(word_len):
    display.append("_")

print(display) 

# while correct < word_len:
while display.count("_") > 0:
    guess = input("guess the letter:")
    for i in range(word_len):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    print(display)
print("you win!")            

      
