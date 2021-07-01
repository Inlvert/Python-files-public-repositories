x = 50
def func():
    global x

    print("х равно", x)
    x = 2
    print("Замена глобальное значение х на", x)
func()
print("Значение х составляет", x)

