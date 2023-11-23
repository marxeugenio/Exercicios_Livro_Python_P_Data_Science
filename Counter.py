from collections import Counter

lista_numeros = [0,1,2,3,2,32,3,2,12,]

lista_strings = ["a","a","b","b","c","c","c"]

c1 = Counter(lista_numeros)
c2 = Counter(lista_strings)

print(f"Lista de numeros {lista_numeros}")
print(f"Distribuição dos números: {c1}")
print(f"Lista de letras: {lista_strings}")
print(f"Distribuição das letras: {c2}")
