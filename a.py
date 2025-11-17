import json
import os
from datetime import datetime
import csv

ARQUIVO = "dados.json"


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"usuarios": {}}

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)



def cadastrar_usuario(dados):
    usuario = input("Digite um nome de usuário: ")

    if usuario in dados["usuarios"]:
        print("Usuário já existe!")
        return None

    senha = input("Digite uma senha: ")

    dados["usuarios"][usuario] = {
        "senha": senha,
        "transacoes": []
    }

    salvar_dados(dados)
    print("Cadastro realizado com sucesso!")
    return usuario


def login(dados):
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in dados["usuarios"] and dados["usuarios"][usuario]["senha"] == senha:
        print("Login realizado!")
        return usuario

    print("Usuário ou senha incorretos.")
    return None


def adicionar_transacao(dados, usuario):
    print("\n--- Adicionar Transação ---")

    data = input("Data (YYYY-MM-DD): ")
    tipo = input("Tipo (entrada/saida): ").lower()
    categoria = input("Categoria: ")
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))

    transacao = {
        "data": data,
        "tipo": tipo,
        "categoria": categoria,
        "descricao": descricao,
        "valor": valor
    }

    dados["usuarios"][usuario]["transacoes"].append(transacao)
    salvar_dados(dados)
    print("Transação adicionada!\n")


def remover_transacao(dados, usuario):
    listar_todas(dados, usuario)
    indice = int(input("Digite o número da transação para remover: "))

    transacoes = dados["usuarios"][usuario]["transacoes"]

    if 0 <= indice < len(transacoes):
        transacoes.pop(indice)
        salvar_dados(dados)
        print("Transação removida!\n")
    else:
        print("Índice inválido.")


def listar_por_categoria(dados, usuario):
    categoria = input("Categoria: ")
    transacoes = dados["usuarios"][usuario]["transacoes"]

    for t in transacoes:
        if t["categoria"].lower() == categoria.lower():
            print(t)


def listar_por_periodo(dados, usuario):
    inicio = input("Data início (YYYY-MM-DD): ")
    fim = input("Data fim (YYYY-MM-DD): ")

    transacoes = dados["usuarios"][usuario]["transacoes"]

    for t in transacoes:
        if inicio <= t["data"] <= fim:
            print(t)


def calcular_saldo(dados, usuario):
    inicio = input("Data início (YYYY-MM-DD): ")
    fim = input("Data fim (YYYY-MM-DD): ")

    transacoes = dados["usuarios"][usuario]["transacoes"]

    saldo = 0
    for t in transacoes:
        if inicio <= t["data"] <= fim:
            if t["tipo"] == "entrada":
                saldo += t["valor"]
            else:
                saldo -= t["valor"]

    print(f"Saldo no período: {saldo}")


def listar_todas(dados, usuario):
    print("\n--- Transações ---")
    transacoes = dados["usuarios"][usuario]["transacoes"]

    for i, t in enumerate(transacoes):
        print(f"{i} - {t}")



def exportar_csv(dados, usuario):
    nome_arquivo = f"export_{usuario}.csv"
    transacoes = dados["usuarios"][usuario]["transacoes"]

    with open(nome_arquivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["data", "tipo", "categoria", "descricao", "valor"])

        for t in transacoes:
            escritor.writerow([t["data"], t["tipo"], t["categoria"], t["descricao"], t["valor"]])

    print(f"Exportado para {nome_arquivo}\n")



def menu_usuario(dados, usuario):
    while True:
        print("""
--- Menu ---
1. Adicionar transação
2. Remover transação
3. Listar por categoria
4. Listar por período
5. Calcular saldo por período
6. Listar todas transações
7. Exportar CSV
0. Sair
        """)

        op = input("Escolha: ")

        if op == "1": adicionar_transacao(dados, usuario)
        elif op == "2": remover_transacao(dados, usuario)
        elif op == "3": listar_por_categoria(dados, usuario)
        elif op == "4": listar_por_periodo(dados, usuario)
        elif op == "5": calcular_saldo(dados, usuario)
        elif op == "6": listar_todas(dados, usuario)
        elif op == "7": exportar_csv(dados, usuario)
        elif op == "0": break
        else: print("Opção inválida!")



def main():
    dados = carregar_dados()

    print("1. Login")
    print("2. Cadastrar\n")

    escolha = input("Escolha: ")

    usuario = None
    if escolha == "1":
        usuario = login(dados)
    elif escolha == "2":
        usuario = cadastrar_usuario(dados)

    if usuario:
        menu_usuario(dados, usuario)


if __name__ == "__main__":
    main()
