lista_duplicadas = ["a","a","b","b","c","c","d","e"]

print(f"Conteudo inicial da lista: {lista_duplicadas}")

print("Convertendo a lista em conjunto para eliminar duplicidades")

conjunto = set(lista_duplicadas)

print("Convertendo o conjunto em uma lista sem duplicações..")

lista_sem_duplicacoes = list(conjunto)

print(f"Conteudo da lista sem valores duplicados: {lista_sem_duplicacoes}")
