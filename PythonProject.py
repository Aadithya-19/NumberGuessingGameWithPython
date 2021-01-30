import random
 
r = random.randint(1, 9)

c = 5

while(c>=0):
    inp = int(input("Please enter your guess: "))
    print("You have ",c," choices left.")
    c = c - 1
    
    if inp == r:
        print("Congratulations you guessed the correct number!")
        break
    elif inp < r:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

print(r)