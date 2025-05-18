m = 1
n = 1

soma = 0
while(m > 0 and n > 0):
    m, n = input().split(" ")
    m = int(m)
    n = int(n)
    if (m>0 and n>0):
        if (n > m):
            aux = n
            n = m
            m = aux

        for i in range(n, m + 1):
            soma += i
            print(f"{i} ", end=(""))
        print(f"Sum={soma}")
        soma=0