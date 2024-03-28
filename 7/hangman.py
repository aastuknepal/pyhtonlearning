import random
print("Welcome to hangman ")
word_list = ["hello", "Kathmandu", "camel"]

#randomly chose the item from the list

chosen_word = random.choice(word_list)


#asking the user to enter their characters and letters

display = []
for letter in chosen_word:
    display += "_"
print(display)

guess = input("Enter the letter").lower()




for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        
print(display)
      