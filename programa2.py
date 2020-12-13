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


cores = {'limpar': '\033[m', 'azul': '\033[1;34m', 'azul_claro': '\033[1;36m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[1;33m', 'roxo': '\033[1;35m'}

with open('cartelas.txt', 'r') as todas_cartelas:  # todas_cartelas = open('cartelas_doc.txt', 'r')
    lista_cartelas = todas_cartelas.readlines()

tam_lista_cartelas = len(lista_cartelas)
matriz_cartelas = [[]] * tam_lista_cartelas # da pra substituir depois pelo numero de cartelas de entrada pelo user

for p in range(tam_lista_cartelas):
    matriz_cartelas[p] = [0, p + 1]  # transformando o arquivo das cartelas em uma matriz de inteiros
    matriz_cartelas[p].append(list(map(int, lista_cartelas[p].split())))

globo = list(range(100))  # criando lista com as "bolinhas" do bingo (de 0 a 99)

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
    print('Número sorteado: {cor}{num}{limpar_cor}'.format(cor=cores['roxo'], num=globo[index], limpar_cor=cores['limpar']))
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
                print('{cor}A cartela nº {num} está próxima da vitória!{limpar_cor}'.format(cor=cores['vermelho'], num=cartela[1], limpar_cor=cores['limpar']))  # pode ser melhorado

    globo.pop(index)
    maximo -= 1

    tabela_classific = selectionsort(matriz_cartelas)
    print('\nClassificação atual:')
    pos = 1
    for cartela_clas in tabela_classific:
        pos_str = (cores['amarelo'] + str(pos) + 'º)' + cores['limpar']).ljust(15, ' ')

        if cartela_clas[0] == 9:
            pontuacao_cartela = cores['vermelho'] + str(cartela_clas[0]).zfill(2) + 'pts' + cores['limpar']
        elif cartela_clas[0] == 10:
            pontuacao_cartela = cores['verde'] + str(cartela_clas[0]).zfill(2) + 'pts' + cores['limpar']
        else:
            pontuacao_cartela = cores['azul'] + str(cartela_clas[0]).zfill(2) + 'pts' + cores['limpar']

        id_cartela = ('Cartela{' + str(cartela_clas[1]) + '}:').ljust(13, ' ')
        print('{} {} {: ^15} {}'.format(pos_str, pontuacao_cartela, id_cartela, cartela_clas[2]))
        pos += 1

    if quant_vencedores > 1:
        print('\n{cor}Uau! Temos mais de um vencedor por aqui!{limpar_cor}\n'.format(cor=cores['verde'], limpar_cor=cores['limpar']))
    elif quant_vencedores == 1:
        print('\n{cor}Opa! Parece que temos um vencedor!{limpar_cor}\n'.format(cor=cores['verde'], limpar_cor=cores['limpar']))
    else:
        print()

print('{cor}{pre_estilo}{txt}{pos_estilo}{limpar_cor}'.format(cor=cores['azul_claro'], pre_estilo='='*60, txt=' {RESULTADOS FINAIS} ', pos_estilo='='*300, limpar_cor=cores['limpar']))
print('Quantidade de números sorteados ao todo: {cor}{num}{limpar_cor}'.format(cor=cores['amarelo'], num=len(todos_os_sorteados), limpar_cor=cores['limpar']))
print('Todos os números sorteados na partida:{cor}'.format(cor=cores['roxo']), end=' ')
print(*todos_os_sorteados, sep=', ')

if quant_vencedores == 1:
    print('{}Houve {} vencedor na partida:'.format(cores['verde'], quant_vencedores))
else:
    print('{}Houve {} vencedores na partida:'.format(cores['verde'], quant_vencedores))

for cartela_vencedora in vencedores:
    print('-> Cartela nº {}: {}'.format(cartela_vencedora[0], cartela_vencedora[1]))
