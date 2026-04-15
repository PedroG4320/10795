n = int(input("Número: "))
div = 0
for i in range(1, n+1):
    if n % i == 0:
        div += 1
print("Divisores:", div)