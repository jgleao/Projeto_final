def media_categoria():
    cats = {}
    for l in lancamentos:
        if l['categoria'] not in cats:
            cats[l['categoria']] = []
        cats[l['categoria']].append(l['valor'])
    return {c: sum(v)/len(v) for c, v in cats.items()}


def grafico_pizza():
    cats = {}
    for l in lancamentos:
        if l['tipo'] == 'despesa':
            cats[l['categoria']] = cats.get(l['categoria'], 0) + l['valor']

    plt.figure()
    plt.pie(cats.values(), labels=cats.keys(), autopct="%1.1f%%")
    plt.title("Proporção de Gastos por Categoria")
    plt.show()


def grafico_linha():
    dados = sorted(lancamentos, key=lambda x: x['data'])
    datas = []
    saldos = []
    saldo = 0

    for l in dados:
        if l['tipo'] == 'receita': saldo += l['valor']
        else: saldo -= l['valor']
        datas.append(l['data'])
        saldos.append(saldo)

    plt.figure()
    plt.plot(datas, saldos)
    plt.title("Saldo Acumulado ao Longo do Tempo")
    plt.xlabel("Data")
    plt.ylabel("Saldo")
    plt.grid(True)
    plt.show()



print("Totais:", totais())
print("Saldo mensal:", saldo_mensal())
print("Média categoria:", media_categoria())

grafico_pizza()
grafico_linha()
