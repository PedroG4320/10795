def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def divisores(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count


def perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n

n = int(input("Número (1-30000): "))
while not (1 <= n <= 30000):
    n = int(input("Número válido (1-30000): "))

contador = 0
for i in range(n, 0, -1):
    print(f"Número: {i}")
    print("Primo:" , eh_primo(i))
    print("Divisores:", divisores(i))
    print("Perfeito:", perfeito(i))
    print("----------------")

    contador += 1
    if contador % 10 == 0:
        op = input("Continuar? (s/n): ")
        if op.lower() != 's':
            break