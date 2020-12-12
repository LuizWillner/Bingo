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


cores = {'limpar': '\033[m', 'azul': '\033[1;34m', 'azul_claro': '\033[1;36m', 'vermelho': '\033[1;31m', 'verde': '\033[0;32m', 'amarelo': '\033[1;33m', 'roxo': '\033[1;35m'}

with open('cartelas.txt', 'r') as todas_cartelas:  # todas_cartelas = open('cartelas_doc.txt', 'r')
    lista_cartelas = todas_cartelas.readlines()

matriz_cartelas = [[]] * len(lista_cartelas)  # da pra substituir depois pelo numero de cartelas de entrada pelo user

for p in range(len(lista_cartelas)):  # da pra substituir depois pelo numero de cartelas de entrada pelo user
    matriz_cartelas[p] = [0, p + 1]  # transformando o arquivo das cartelas em uma matriz de inteiros
    matriz_cartelas[p].append(list(map(int, lista_cartelas[p].split())))

globo = list(range(100))  # criando lista com as 1oo "bolinhas" do bingo (de 0 a 99)
print(matriz_cartelas, '\n')

rodada = 0
maximo = 99
todos_os_sorteados = []
checa_vencedor = False
vencedores = []
quant_vencedores = 0

while not checa_vencedor:
    index = randint(0, maximo)
    todos_os_sorteados.append(globo[index])
    rodada += 1
    print('{pre_estilo}{cor}{txt}{limpar_cor}{pos_estilo}'.format(pre_estilo='='*64, cor=cores['amarelo'], txt=' {RODADA ' + str(rodada) + '} ', limpar_cor=cores['limpar'], pos_estilo='='*304))
    print('Número sorteado: {}{}{}'.format(cores['roxo'], globo[index], cores['limpar']))
    print('Sorteados até agora:', end=' ')
    print(*todos_os_sorteados[0:-1], cores['roxo'] + str(globo[index]) + cores['limpar'], sep=', ')

    for cartela in matriz_cartelas:
        if globo[index] in cartela[2]:
            cartela[0] += 1
            if cartela[0] == 10:
                checa_vencedor = True
                quant_vencedores += 1
                vencedores.append(cartela[1:])
            elif cartela[0] == 9:
                print('{}A cartela nº {} está próxima da vitória!{}'.format(cores['vermelho'], cartela[1], cores['limpar']))  # pode ser melhorado

    globo.pop(index)
    maximo -= 1

    tabela_classific = selectionsort(matriz_cartelas)  # achar um jeito de chamar função do outro arquivo .py
    print('Classificação atual:')  # modificar para não printar como lista
    pos = 1
    for cartela_clas in tabela_classific:
        pos_str = cores['amarelo'] + str(pos) + ')' + cores['limpar']
        pontuacao_cartela = cores['azul'] + str(cartela_clas[0]) + 'pts' + cores['limpar']
        id_cartela = 'Cartela{' + str(cartela_clas[1]) + '}:'
        print('{}   {}  {} {}'.format(pos_str, pontuacao_cartela, id_cartela, cartela_clas[2]))
        pos += 1

    print()

print('{cor}{pre_estilo}{txt}{pos_estilo}{limpar_cor}'.format(cor=cores['azul_claro'], pre_estilo='='*60, txt=' {RESULTADOS FINAIS} ', pos_estilo='='*300, limpar_cor=cores['limpar']))
print('Quantidade de números sorteados ao todo: {}{}{}'.format(cores['amarelo'], len(todos_os_sorteados), cores['limpar']))
print('Todos os números sorteados na partida:{cor}'.format(cor=cores['roxo']), end=' ')
print(*todos_os_sorteados, sep=', ')

if quant_vencedores > 1:
    print('{}Tivemos {} vencedores:'.format(cores['verde'], quant_vencedores))
else:
    print('{}Tivemos {} vencedor:'.format(cores['verde'], quant_vencedores))

for cartela_vencedora in vencedores:
    print('-> Cartela nº {}: {}{}'.format(cartela_vencedora[0], cartela_vencedora[1], cores['limpar']))
