from collections import deque

numeros = input()
listaNumerica = [int(x) for x in numeros.split()]

stack = deque(listaNumerica)

print(stack)

while stack:
    y = stack.pop()
    print(y * 2)