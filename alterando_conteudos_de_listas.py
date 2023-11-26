itens = []
itens = ["livro","caderno","borracha"]
itens [1] = "Régua"
itens.remove("borracha")

print(itens)
print(len(itens))

fatia = itens[1:3]


itens.append("Borracha")
print(itens)
print(len(itens))

# -----------------------------------------------------------------------------------------------

itens = []

itens.append("livro")
itens.append("caderno")
itens.append("borracha")

itens[1] = "régua"

if "caderno" in itens:
    print("A lista contém um caderno")
print(f"a lista possui {len(itens)} elementos")

ultimo_elemento = itens.pop()

print(f"Após a remoção de [ultimo_elemento], a lista ficou com {len(itens)} elementos")

fatia = itens [-2]

print(f"Os dois ultimos elementos da lista são {fatia}")
