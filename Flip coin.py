import random

print("This is a simple program, that flips a coin and gets Heads or Tails")
guess = input("What do you expect to get? Heads or Tails? ")

number = random.randint(0,1)

if (number == 0 and guess == "Heads"):
    print("Heads")
    print("You guessed right (Heads)")
elif (number == 1 and guess == "Tails"):
    print("Tails")
    print("You guessed right (Tails)")
elif (number == 0 and guess == "Tails"):
    print("Heads")
    print("You guessed wrong (Tails)")
elif (number == 1 and guess == "Heads"):
    print("Tails")
    print("You guessed wrong (Heads)")

