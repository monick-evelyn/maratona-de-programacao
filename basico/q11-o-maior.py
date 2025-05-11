a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

maior = a
vetor = [a, b, c]
for n in vetor:
    if (n > maior):
        maior = n
print(f"{maior} eh o maior")