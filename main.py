import os

ARQUIVO = "transacoes.txt"

def carregar_transacoes():
    if not os.path.exists(ARQUIVO):
        return []
    transacoes = []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for linha in f:
            data, tipo, categoria, desc, valor = linha.strip().split("|")
            transacoes.append({
                "data": data,
                "tipo": tipo,
                "categoria": categoria,
                "descricao": desc,
                "valor": float(valor)
            })
    return transacoes

def salvar_transacoes(transacoes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for t in transacoes:
            f.write(f'{t["data"]}|{t["tipo"]}|{t["categoria"]}|{t["descricao"]}|{t["valor"]}\n')

def adicionar(transacoes):
    print("\n--- Adicionar Transação ---")
    data = input("Data (dd/mm/aaaa): ")
    tipo = input("Tipo (entrada/saida): ").lower()
    categoria = input("Categoria: ")
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))

    transacoes.append({
        "data": data,
        "tipo": tipo,
        "categoria": categoria,
        "descricao": descricao,
        "valor": valor
    })

    salvar_transacoes(transacoes)
    print("Transação adicionada!\n")

def listar(transacoes):
    print("\n--- Lista de Transações ---")
    for t in transacoes:
        print(f'{t["data"]} | {t["tipo"]} | {t["categoria"]} | {t["descricao"]} | R$ {t["valor"]}')
    print()

def saldo(transacoes):
    print("\n--- Saldo Total ---")
    total = 0
    for t in transacoes:
        if t["tipo"] == "entrada":
            total += t["valor"]
        else:
            total -= t["valor"]
    print(f"Saldo atual: R$ {total}\n")

def menu():
    transacoes = carregar_transacoes()

    while True:
        print("1 - Adicionar transação")
        print("2 - Listar transações")
        print("3 - Ver saldo")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            adicionar(transacoes)
        elif op == "2":
            listar(transacoes)
        elif op == "3":
            saldo(transacoes)
        elif op == "0":
            break
        else:
            print("Opção inválida!\n")

menu()
git remote add origin https://github.com/jgleao/Projeto_final.git
git remote add origin
git config --global user.name "Joao Vieira"
git config --global user.email "jgleaovieira@gmail.com"
