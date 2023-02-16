x = 1
y = 1
def fibbon():
    a = int(input("term: "))
    x = 1
    y = 1
    z = x + y
    if a == 1:
        print(x)
    elif a == 2:
        print(x)
        print(y)
    elif a >= 2:
        print(x)
        print(y)
        print(z)
        while z <= a:
            x = y
            y = z
            z = x + y
            print(z)
    return
fibbon()