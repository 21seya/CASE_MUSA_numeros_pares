#ler a função de uma lista mostrar os pares 

def ler_lista_dados(num_1:int , num_2:int) -> list:
    lista_dados = [0,2,3,4,5,6,7,8,9,12,16,20]
    dados_lista = []
    for num_1 in lista_dados:
        if num_1 % 2 == 0:
            dados_lista.append(num_1)
    for num_2 in lista_dados:        
            if num_2 % 2 != 0:
                dados_lista.append(num_2)    
    return sum(dados_lista)

dados =ler_lista_dados()
print(dados)
