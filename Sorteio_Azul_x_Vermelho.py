import random

# Inicializando as contagens

contagem_vermelha = 0
contagem_azul = 0

# Realizando 10 sorteios

for _ in range(10):
    bola_sorteada = random.choice(["vermelha","azul"]) # Escolhe aleatoriamente

    # Incrementando a contagem da bola sorteada
    
    if bola_sorteada == "vermelha":
        contagem_vermelha += 1
    else:
        contagem_azul += 1

print(f"A bola vermelha foi sorteada {contagem_vermelha} vezes.")
print(f"A bola azul foi sorteada {contagem_azul} vezes.")
