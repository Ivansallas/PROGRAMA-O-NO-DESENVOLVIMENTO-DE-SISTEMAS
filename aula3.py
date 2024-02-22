# Operadores de Comparação
# Operadores como ==, !=, <, >, <= e >= são usados para comparar valores.
# Eles são cruciais nas estruturas de decisão e retornam valores booleanos (True ou False) com base na comparação.

# Definindo duas variáveis para comparção

a = int(input("Digite o primeiro numero "))
b = int(input("Digite o segundo numero "))


# Usando operadores de comparação

# Comparação de igualdade
if a == b:
    print("{} é igual a {}".format(a, b))
elif a != b:
    print("{} é diferente de {}".format(a, b))

# Comparação de Menor ou Maior
if a < b:
    print("{} é menor que {}".format(a, b))
elif a > b:
    print("{} é maior que {}".format(a, b))


# Comparação de Maior e Menor ou igual
if a < b:
    print(" {} é menor que {}".format(a, b))

if b > a:
    print(" {} é maior que {}".format(b, a))
else:
    print("{} é igual a {}".format(a, b))


"""# Solicita a idade do usuário
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
print(f"Você está na categoria: {categoria}.")"""
