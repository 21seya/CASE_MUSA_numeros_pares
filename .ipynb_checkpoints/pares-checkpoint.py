def ler_dados_pares():
    lista_dados = [0,2,3,4,5,6,7,8,9,12,16,20]
    dados_lista = []
    for num in lista_dados:
        if num % 2 == 0:
            dados_lista.append(num)
    return sum(dados_lista)

dados = ler_dados_pares()
print(dados)       