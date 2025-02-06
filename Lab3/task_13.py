from random import randint
def game():
    print("Hello! What is your name?\n")
    name=input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20")
    number=randint(1,20)
    gues=0
    while True:
        print("Take a guess.\n")
        print()
        n=int(input())
        gues+=1
        if n==number:
            print(f"Good job, {name}! You guessed my number in {gues} guesses!")
            break
        elif n>number:
            print(f"Your guess {n} is too upper.")
        else:
            print(f"Your guess {n} is too low.")

game()