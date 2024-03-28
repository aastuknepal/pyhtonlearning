from random import randint

easy_level_turns = 10
hard_level_turns = 5 


def check_answer(guess, answer, turns):
   
    if guess>answer:
        print("Too high")
        return turns - 1
    elif guess<answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it. The answer is {answer}.")


def set_difficulty():
    level = input("Please chose a difficulty level. Type 'easy' or 'hard'").lower()
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns 
    
 
def game():
    print("Welcome to the number guessing game")
    print("I am thhinking of a number between 1 and 100")
    answer = randint(1, 100)



    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the right answer")

        guess = int(input("Make a guess"))
        turns = check_answer(guess, answer, turns)
        
game()