def perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n

count = 0
for i in range(1, 1001):
    if perfeito(i):
        count += 1
print("Perfeitos:", count)