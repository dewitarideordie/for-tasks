# game secret number

secret_number = 280808

guests = int(input("Guess the number: "))

while secret_number != guests:
    print("Poor you, you're stuck in this loop forever!")
    print("Try guess again")
    guests = int(input("Guess the number: "))

print("Congartulations,you did it!")
