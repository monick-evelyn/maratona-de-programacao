import math

while True:
    try:
        m,n = input("").split(" ")
        m = int(m)
        n = int(n)
        if (m >= 0 and m <= 20 and n >= 0 and n<=20):
            print(f"{math.factorial(m) + math.factorial(n)}")
    except EOFError:
        break