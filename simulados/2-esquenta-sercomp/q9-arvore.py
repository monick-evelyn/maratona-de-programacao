while True:
    try:
        n = int(input())
        
        for i in range(1, n + 1, 2):
            print(" " * ((n - i) // 2) + "*" * i)
        
        for i in range(1, 4, 2):
            print(" " * ((n - i) // 2) + "*" * i)
        
        print()

    except EOFError:
        break