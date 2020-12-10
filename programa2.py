from random import randint

globo = list(range(100))  # criando lista com as 1oo "bolinhas" do bingo (de 0 a 99)

maximo = 99
todos_os_sorteados = []
index = randint(0, maximo)
todos_os_sorteados.append(globo[index])
globo.pop(index)
maximo -= 1

cartelas = open('cartelas_doc.txt', 'r')
lista_cartelas = cartelas.readlines()
print(lista_cartelas)

for i in range(len(lista_cartelas)):  # da pra substituir depois pelo numero de cartelas de entrada pelo user
    lista_cartelas[i] = list(map(int, lista_cartelas[i].split()))  # transformando o arquivo das cartelas em uma matriz de inteiros

print(lista_cartelas)
