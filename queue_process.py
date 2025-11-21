from collections import deque

palavras = input()

queue = deque()

for palavra in palavras.split():
    queue.appendleft(palavra)

print(queue)

while queue:
    palavra = queue.pop()
    if "a" in palavra:
        print(palavra)