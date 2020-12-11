from random import randint

todas_cartelas = open('cartelas_doc.txt', 'r')
lista_cartelas = todas_cartelas.readlines()
matriz_cartelas = [[]] * len(lista_cartelas)  # da pra substituir depois pelo numero de cartelas de entrada pelo user

for i in range(len(lista_cartelas)):  # da pra substituir depois pelo numero de cartelas de entrada pelo user
    matriz_cartelas[i] = list(map(int, lista_cartelas[i].split()))  # transformando o arquivo das cartelas em uma matriz de inteiros
    matriz_cartelas[i].append([0])

print(lista_cartelas)
print(matriz_cartelas)

globo = list(range(100))  # criando lista com as 1oo "bolinhas" do bingo (de 0 a 99)

maximo = 99
todos_os_sorteados = []
vencedor = False

while maximo >= 0 and not vencedor:
    index = randint(0, maximo)
    todos_os_sorteados.append(globo[index])
    globo.pop(index)
    maximo -= 1

    for cartela in matriz_cartelas:
        if globo[index] in cartela:
            cartela[-1] += 1
            if cartela[-1] == 10:
                vencedor = True  # talvez seja interessante adicionar as cartelas vencedoras numa lista para depois printar qum ganhou
            elif cartela[-1] == 9:
                print('A cartela {} está próxima da vitória!'.format(matriz_cartelas.index(cartela)))  # pode ser melhorado
    


