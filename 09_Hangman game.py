import random
import hangman_words
import hangman_art
print(hangman_art.logo)
stages=hangman_art.stages

word_list=hangman_words.hangman_words_list
chosen_word=random.choice(word_list)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

num_guesses=0
correct_guesses=[]
game_over=False
lives=6
while game_over==False:
    placeholder=""
    guess=input("Enter a letter: ").lower()
    if guess in correct_guesses:
        print(f"You've already guessed {guess}")

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"{guess} is not in the word")
        print(f"{lives}/6 lives left")


    word_length=len(chosen_word)
    for i in range(word_length):
        placeholder+="_"

    display=""
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_guesses+=letter
            print(stages[lives])
        elif letter in correct_guesses:
            display+=letter
        else:
            display+="_"
    print(display)
    if "_" not in display:
        print("**********You win!**********")
        game_over = True
    elif  lives == 0:
        print("**********You lose!**********")
        print(f"The word was {chosen_word}")
        game_over = True








