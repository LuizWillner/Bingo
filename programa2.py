from random import randint


def selectionsort(lista):  # criando o metodo de ordenacao selectionsort
    i = 0
    while i < len(lista) - 1:
        j = i + 1
        while j < len(lista):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
            j += 1
        i += 1
    return lista


cores = {'limpar': '\033[m', 'azul': '\033[0;34m', 'azul_claro': '\033[0;36m', 'vermelho': '\033[1;31m', 'verde': '\033[0;32m', 'amarelo': '\033[0;33m'}

with open('cartelas.txt', 'r') as todas_cartelas:  # todas_cartelas = open('cartelas_doc.txt', 'r')
    lista_cartelas = todas_cartelas.readlines()

matriz_cartelas = [[]] * len(lista_cartelas)  # da pra substituir depois pelo numero de cartelas de entrada pelo user

for p in range(len(lista_cartelas)):  # da pra substituir depois pelo numero de cartelas de entrada pelo user
    matriz_cartelas[p] = [0]  # transformando o arquivo das cartelas em uma matriz de inteiros
    matriz_cartelas[p].append(list(map(int, lista_cartelas[p].split())))

print('======================='*10)
print(lista_cartelas)
print(matriz_cartelas)
print('======================='*10)
print('')

globo = list(range(100))  # criando lista com as 1oo "bolinhas" do bingo (de 0 a 99)

maximo = 99
todos_os_sorteados = []
checa_vencedor = False

while not checa_vencedor:
    index = randint(0, maximo)
    print('Index sorteado:', index)
    todos_os_sorteados.append(globo[index])
    print('Número sorteado da rodada:', globo[index])
    print('Sorteados até agora:', todos_os_sorteados)  # modificar para não printar como lista

    for cartela in matriz_cartelas:
        if globo[index] in cartela[1]:
            cartela[0] += 1
            if cartela[0] == 10:
                checa_vencedor = True  # talvez seja interessante adicionar as cartelas vencedoras numa lista para depois printar quem ganhou
            elif cartela[0] == 9:
                id_cartela = matriz_cartelas.index(cartela) + 1
                print('{}A cartela {} está próxima da vitória!{}'.format(cores['vermelho'], id_cartela, cores['limpar']))  # pode ser melhorado

    globo.pop(index)
    maximo -= 1

    classific_cartelas = selectionsort(matriz_cartelas)  # achar um jeito de chamar função do outro arquivo .py
    print('Classificação atual:', classific_cartelas)  # modificar para não printar como lista
    print('')

print('Quantidade de números sorteados ao todo:', len(todos_os_sorteados))
print('Todos os números sorteados na partida:', todos_os_sorteados)  # modificar para não printar como lista

quant_vencedores = 0
vencedores = []
for p in range(len(classific_cartelas)):  # da pra substituir depois pelo numero de cartelas de entrada pelo user
    if classific_cartelas[p][0] == 10:
        quant_vencedores += 1
        vencedores.append(classific_cartelas[p][1])

if quant_vencedores > 1:
    print('{}Houve {} vencedores{}'.format(cores['verde'], quant_vencedores, cores['limpar']))
else:
    print('{}Houve {} vencedor{}'.format(cores['verde'], quant_vencedores, cores['limpar']))

print('{}{}{}'.format(cores['verde'], vencedores, cores['limpar']))  # modificar para não printar como lista
