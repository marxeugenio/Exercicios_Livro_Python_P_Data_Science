A = set() # Criando um conjunto vazio
print(f"Criando um conjunto vazio: A= {A}")

A.add("X") # Adicionando um elemento ao conjunto
print(f"Adicionando um elemento ao conjunto A: A = {A}")

A.add("Y")
print(f"Adicionando outro elemento ao conjunto A: A = {A}")

A.add("Z")
print(f"Adcionando mais um elemento ao conjunto A: A= {A}")

A.add(123)
print(f"Adicionando um quarto elemento ao conjunto A: A = {A}")

print(f"A contem agora {len(A)} elementos")

teste_pertinencia = "X" in A
print(f"O elemento \"X\" está contido em A? {teste_pertinencia}")

teste_pertinencia = "o" in A
print(f"O elemento \"o\" está contido em A? {teste_pertinencia}")
