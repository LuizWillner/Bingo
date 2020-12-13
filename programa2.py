from random import randint


def selectionsort_reverse(lista):  # função de ordenação selection sort revertida, para ordenar a classificação
    i = 0
    while i < len(lista) - 1:
        j = i + 1
        while j < len(lista):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
            j += 1
        i += 1
    return lista


# Dicionário para utilizar como referência para a aplicação de cores na saída do código
cores = {'limpar': '\033[m', 'azul': '\033[1;34m', 'azul_claro': '\033[1;36m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[1;33m', 'roxo': '\033[1;35m'}

with open('cartelas.txt', 'r') as todas_cartelas:  # lendo o doc de texto das cartelas geradas pelo programa montador de cartelas e armazenando em formato de lista de strigs
    lista_cartelas = todas_cartelas.readlines()

tam_lista_cartelas = len(lista_cartelas)  # quantidade de cartelas lidas do arquivo
matriz_cartelas = [[]] * tam_lista_cartelas  # alocando espaço na memória para transformar a lista de strings das carteals em uma matriz (lista de listas)...
# ... contendo informações das cartelas

for p in range(tam_lista_cartelas):  # para cada cartela, faça:
    matriz_cartelas[p] = [0, p + 1]  # os primeiros dois elementos das sublistas de "matrz_cartelas" representam, respectivamente, a quantidade de números sorteados daquela cartela...
    # ...e o identificador daquela cartela, começando de 1 até tam_lista_cartelas
    matriz_cartelas[p].append(list(map(int, lista_cartelas[p].split())))  # o terceiro elemento é a própria cartela...
    # cujos elementos internos são inteiros que representam os valores numéricos contidos na cartela

globo = list(range(100))  # criando o globo com as "bolinhas" do bingo (de 0 a 99) no formato de uma lista

rodada = 0  # contador do número rodada
maximo = 99  # index máximo do globo, que vai de 0 a 99 (100 bolinhas)
todos_os_sorteados = []  # lista para armazenar todos os números sorteados
checa_vencedor = False  # booleano para indicar se foi encontrado algum vencedor
vencedores = []  # lista para armazenar as cartelas vencedoras
quant_vencedores = 0  # quantidade de vencedores

while not checa_vencedor:  # enquanto não há vencedores, faça:
    index = randint(0, maximo)  # sorteamos um index do globo e...
    todos_os_sorteados.append(globo[index])  # adicionamos o valor correspondente nos sorteados
    rodada += 1
    print('{pre_estilo}{cor}{txt}{limpar_cor}{pos_estilo}'.format(pre_estilo='='*64, cor=cores['amarelo'], txt=' {RODADA ' + str(rodada) + '} ', limpar_cor=cores['limpar'], pos_estilo='='*304))
    print('Número sorteado: {cor}{num}{limpar_cor}'.format(cor=cores['roxo'], num=globo[index], limpar_cor=cores['limpar']))
    print('Sorteados até agora:', end=' ')
    print(*todos_os_sorteados[0:-1], cores['roxo'] + str(globo[index]) + cores['limpar'], sep=', ')  # printando os sorteados até o momento

    for cartela in matriz_cartelas:  # para cada cartela na matriz cartela, verificamos se o num sorteado está na cartela
        if globo[index] in cartela[2]:  # se estiver:
            cartela[0] += 1  # somamos 1 na pontuação de sorteados
            if cartela[0] == 10:  # se a pontuação for igual a 10, já temos um vencedor
                checa_vencedor = True
                quant_vencedores += 1
                vencedores.append(cartela[1:])  # adicionamos a cartela vencedora e sua classificação em vencedores
            elif cartela[0] == 9:  # se a pontuação for 9:
                print('{cor}A cartela nº {num} está próxima da vitória!{limpar_cor}'.format(cor=cores['vermelho'], num=cartela[1], limpar_cor=cores['limpar']))  # pode ser melhorado
                # printamos um aviso de que aquelacartela está próxima da vitória

    globo.pop(index)  # retiramos o num sorteado do globo de bolinhas
    maximo -= 1  # reduzimos o index máximo do globo de sorteados

    if quant_vencedores > 1:  # se há algum vencedor, um alerta é emitido indicando que, em seguida, haverá a classificação final e os resultados finais
        print('\n{cor}Uau! Temos mais de um vencedor por aqui!{limpar_cor}'.format(cor=cores['verde'], limpar_cor=cores['limpar']))
    elif quant_vencedores == 1:
        print('\n{cor}Opa! Parece que temos um vencedor!{limpar_cor}'.format(cor=cores['verde'], limpar_cor=cores['limpar']))
    else:
        print()

    tabela_classific = selectionsort_reverse(matriz_cartelas)  # ordenando a matriz para printar a classificação
    print('\nClassificação atual:')
    pos = 1  # variável da posição da tabela (1º lugar, 2º lugar, 3º...)
    for cartela_clas in tabela_classific:  # printando a classificação
        pos_str = (cores['amarelo'] + str(pos) + 'º)' + cores['limpar']).ljust(15, ' ')

        if cartela_clas[0] == 9:  # se a cartela tiver 9 pontos, sua pontuação é destacada em vermelho pois está próxima da vitória
            pontuacao_cartela = cores['vermelho'] + str(cartela_clas[0]).zfill(2) + 'pts' + cores['limpar']
        elif cartela_clas[0] == 10:  # se tiver 10 pontos, ela é uma das vencedoras, então sua pontuação é printada em verde
            pontuacao_cartela = cores['verde'] + str(cartela_clas[0]).zfill(2) + 'pts' + cores['limpar']
        else:
            pontuacao_cartela = cores['azul'] + str(cartela_clas[0]).zfill(2) + 'pts' + cores['limpar']

        id_cartela = ('Cartela{' + str(cartela_clas[1]) + '}:').ljust(13, ' ')
        print('{} {} {: ^15} {}'.format(pos_str, pontuacao_cartela, id_cartela, cartela_clas[2]))
        pos += 1

# printando os resultados finais
print('\n{cor}{pre_estilo}{txt}{pos_estilo}{limpar_cor}'.format(cor=cores['azul_claro'], pre_estilo='='*60, txt=' {RESULTADOS FINAIS} ', pos_estilo='='*300, limpar_cor=cores['limpar']))
print('Quantidade de números sorteados ao todo: {cor}{num}{limpar_cor}'.format(cor=cores['amarelo'], num=len(todos_os_sorteados), limpar_cor=cores['limpar']))
print('Todos os números sorteados na partida:{cor}'.format(cor=cores['roxo']), end=' ')
print(*todos_os_sorteados, sep=', ')

if quant_vencedores == 1:
    print('{}Houve {} vencedor na partida:'.format(cores['verde'], quant_vencedores))
else:
    print('{}Houve {} vencedores na partida:'.format(cores['verde'], quant_vencedores))

for cartela_vencedora in vencedores:
    print('-> Cartela nº {}: {}'.format(cartela_vencedora[0], cartela_vencedora[1]))
