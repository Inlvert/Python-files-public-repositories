def func_outer ():
    x = 2
    print("х равен", x)

    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print("локальное х сменилось на", x)
func_outer()