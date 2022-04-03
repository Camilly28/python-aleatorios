nomes = []

while True:
  nome = input()
  if nome == 'fim':
    break
  nomes.insert(0,nome)

  for nome in nomes:
    print(nome)

    #repete os nomes inseridos de ultimo ao primeiro