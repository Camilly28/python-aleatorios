from operator import truediv


nomes = []

while True:
  nome = input()
  if nome == 'fim':
    break
  nomes.append(nome)

nomes.sort()
nomes.reverse()
print(nomes)

#ordem alfabetica do Z-A