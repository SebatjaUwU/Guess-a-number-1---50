import random

CorrectAnswer = random.randint(1,100)

gameover = false


while gameOver:
    playGuess = int(input("Guess a number"))

    if playGuess == 1:
        gameOver = True
