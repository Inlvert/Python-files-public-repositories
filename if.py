number = 100
guess = int(input("введите целое число : "))
if guess == number:
    print("Поздравляю, вы угадали") # Начало нового блока
    print("(хотя и не выграли никакого приза.)") # Конец нового блока
elif guess < number:
    print("Нет, число должно быть больше этого") # Еще один блок
else:
    print("Нет, заданное число меньше")
    