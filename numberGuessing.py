import random
answer = input("Do you wanna take it easy or hard?")
attempts=10
number= random.randint(0,100)

if(answer=="easy"):
    attempts=10

else:
    attempts=5
print(f"You have {attempts} attempts")
for i in range(attempts):
    guess = int(input("Enter your guess"))
    if(guess==number):
        print("YOU WON")
        break
    else:
        if (number-guess>10):
            print("You guessed too low")
        elif(guess-number>10):
            print("You guessed too high")
        else:
            print("You're almost there")
    if(i==attempts-1):
      print("You're out of attempts bruv")
print(f"Correct answer {number}")

