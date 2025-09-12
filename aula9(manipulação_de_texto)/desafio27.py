n = str(input("Digite seu nome completo: ")).strip() # strip serve para remover todos os espaços desnecessarios
nome = n.split()
print(f"Muito prazer em te coonhecer! ")
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu ultimo nome é {nome[len(nome)-1]}")
