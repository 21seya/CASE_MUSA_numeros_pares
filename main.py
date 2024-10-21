
#ler a função de uma lista mostrar os pares 
def ler_lista_dados() -> list:
    lista_dados = [0,2,3,4,5,6,7,8,9,12,16,20]
    dados_lista = []
    for num in lista_dados:
        if num % 2 == 0:
            dados_lista.append(num)
            
    return sum(dados_lista),len(dados_lista)


sum_num,qtd_num =ler_lista_dados()
eh_par = (sum_num %2 ==0)
print(qtd_num)
print(eh_par)
