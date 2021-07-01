x = 50
def func(x):
    print("х равен", x)
    x = 2
    print("заменалокального х на", x)
func(x)
print("х по прежнему", x)
