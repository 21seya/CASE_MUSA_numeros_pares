#ler a função de uma lista mostrar os pares 
def ler_lista_dados(num_1 : int,num_2 :int) -> list:
    lista_dados = [0,2,3,4,5,6,7,8,9,12,16,20]
    novos_dados = []
    for i in lista_dados:
        if num_1 % 2 == 0:
            novos_dados.append(num_1)
        elif num_2 % 2 == 0:
            novos_dados.append(num_2)
    return sum(novos_dados)

dados =ler_lista_dados(1,6)
print(dados)

