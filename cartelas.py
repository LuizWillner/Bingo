from random import randint  # importando a funcao de aleatoriedade


def selectionsort(lista):  # criando o metodo de ordenacao selectionsort
    i = 0
    while i < len(lista) - 1:
        j = i + 1
        while j < len(lista):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
            j += 1
        i += 1
    return lista


ncartelas = int(input('Digite o número de cartelas desejadas: '))  # quantidade de cartelas a serem geradas
matrizcartela = []  # lista de todas cartelas
for x in range(ncartelas):  # definindo o numero de cartelas a serem geradas
    cartela = []  # numeros da cartela
    while len(cartela) < 10:
        numero = str(randint(0, 99))  # selecionando aleatoriamente os numeros entre 00 e 99 para a cartela
        if len(numero) == 1:  # caso o numero tenha apenas um algarismo adicionar 0 antes
            numero = '0' + numero
        if numero not in cartela:
            cartela.append(numero)  # armazenando os numeros na cartela
    while cartela in matrizcartela:  # evitando cartelas iguais
        num = cartela[9]
        while cartela[9] == num:
            cartela[9] = randint(0, 99)
    cartela = selectionsort(cartela)  # aplicando a ordenacao selectionsort nas cartelas criadas
    matrizcartela.append(cartela)  # armazenando as cartelas na lista(matrizcartelas)
with open('cartelas.txt', 'w') as arquivo:  # abrindo o arquivo
    for cartela in matrizcartela:  # selecionando a cartela para salvar no arquivo em linhas diferentes
        arquivo.write(' '.join(cartela) + '\n')
