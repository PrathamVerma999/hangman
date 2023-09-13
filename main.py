import random
import hangman_words
import hangman_art


stages = hangman_art.stages
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
lives = 6

logo = hangman_art.logo
print(logo)
# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in range(len(chosen_word)):
    display.append('_')
print(stages[lives])
while "_" in display:
    print(" ".join(display))
    guess = input("Guess a letter: ").lower().strip()
    if guess in display:
      print("You've already guessed this!")
    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            print(stages[lives])
            display[index] = letter
    if guess not in chosen_word:
        print("INCORRECT GUESS, TRY AGAIN")
        lives -= 1
        print(stages[lives])
    if lives == 0:
        print(stages[lives]) 
        print(f"The word was {chosen_word}")
        print("YOU LOSE!")
        break       
if "_" not in display:
    print(f'YOU GOT IT, YOU WON CONGRATULATIONS,\nThe Word Was {"".join(display)}')

    
