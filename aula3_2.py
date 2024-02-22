# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))
# Categoriza a idade
if idade < 13:
    categoria = "Criança"
elif idade < 18:
    categoria = "Adolescente"
elif idade < 60:
    categoria = "Adulto"
else:
    categoria = "Idoso"
# Exibe a categoria
print(f"Você está na categoria: {categoria}.")
