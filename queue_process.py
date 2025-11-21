from collections import deque

nomes = input()
listaNomesada = [x for x in nomes.split()]

listadecada = deque(listaNomesada)
print(listadecada)

listaDoisDecada = deque()

for x in listadecada:
    validacao = "nao"
    for y in x:
        if y == "a":
            validacao = "sim"
            listaDoisDecada.append(x)
            break
        else:
            validacao = "nao"

for z in listaDoisDecada:
    print(z)
