number = 23
running = True
while running:
    guess = int(input("write your number : "))
    if guess == number:
        print("Congratulations, you win.")
        running = False # это останавливает цыкл whil
    elif guess < number:
        print("No, this number is more")
    else:
        print("No, this number is less")
else:
    print("Cycle 'while' is over")
print("the and")