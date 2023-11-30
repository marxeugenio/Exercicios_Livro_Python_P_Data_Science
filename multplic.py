numeros = []

for num in range(2000, 5001):
    if num % 2 == 0 and num % 4 == 0 and num % 3 == 0:
        numeros.append(num * 1.5)
        
print("Valores da lista multiplicados por 1.5:")
print(numeros)
