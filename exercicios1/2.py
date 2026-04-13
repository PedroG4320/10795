nota = int(input("Digite a nota (0-100): "))

match True:
    case _ if nota >= 90:
        print("Excelente")
    case _ if 70 <= nota <= 89:
        print("Bom")
    case _ if 50 <= nota <= 69:
        print("Suficiente")
    case _ if nota < 50:
        print("Insuficiente")
    case _:
        print("Nota inválida")