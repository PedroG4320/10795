soma = 0
count = 0
while count < 30:
    n = int(input("Número (1-50): "))
    if 1 <= n <= 50 and n % 2 == 0:
        soma += n
        count += 1
print("Média:", soma/30)