req = {"metodo": "POST", "conteudo": ""}

match req:
    case {"metodo": "GET"}:
        print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": c} if c:
        print("Requisição POST com dados válidos")
    case {"metodo": "POST", "conteudo": c} if not c:
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")