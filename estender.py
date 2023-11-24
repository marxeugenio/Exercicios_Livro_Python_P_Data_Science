usuarios = []

usuarios_informatica = ["Marx Eugenio","Eugenio Lenine","Alan Novais"]

usuarios_contabilidade = ["Dani","Jucineide","Sabrina","Fernanda"]

print(f"Lista vazia de usuarios: {usuarios}")

print(f"Usuarios da informatica: {usuarios_informatica}")

print(f"Usuarios da contabilidade: {usuarios_contabilidade}")

usuarios.extend(usuarios_informatica)
print(f"Lista usuarios preenchida com usuarioss de informatica: {usuarios}")

print("Agora acrescentando a contabilidade...")

usuarios.extend(usuarios_contabilidade)
print(f"Agora a lista usuarios com Contabilidade junto com Informatica: {usuarios}")
