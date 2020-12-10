cartelas = open('cartelas_doc.txt', 'r')
lista_cartelas = cartelas.readlines()
print(lista_cartelas)
for i in range(len(lista_cartelas)):  # da pra substituir depois pelo numero de cartelas de entrada pelo user
    lista_cartelas[i] = list(map(int, lista_cartelas[i].split()))

print(lista_cartelas)
# maximo = 99
# globo = [0, 1, 2, 3, 4, 5 ...... 97, 98, 99]
# todos_os_sorteados = []
# index = randint(0, maximo)
# sorteado = globo[index]
# todos_os_sorteados.append(sorteado)
# globo.pop(index)
# maximo = maximo - 1
