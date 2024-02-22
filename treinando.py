"""n1 = int(input("Digite um valor "))
n2 = str(input("Digite um valor "))
n3 = float(input("Digite um valor "))
n4 = bool(input("Digite um valor "))


print(type(n1))
print(type(n2))
print(type(n3))
print(type(n4))"""

# Definindo uma lista vazia para armazenar os cadastros
cadastros = []


# Definindo uma função para adicionar cadastros à lista
def adicionar_cadastro():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    email = input("Digite o email: ")
    endereco = input("Digite o endereço: ")
    numerocasa = int(input("Digite o numero da casa: "))
    cadastro = {
        "Nome": nome,
        "Idade": idade,
        "Email": email,
        "Endereço": endereco,
        "numerocasa": numerocasa,
    }
    cadastros.append(cadastro)
    print("Cadastro adicionado com sucesso!")
    print("/n")


# Definindo uma função para mostrar todos os cadastros
def mostrar_cadastros():
    if len(cadastros) == 0:
        print("Nenhum cadastro encontrado.")
    else:
        for i, cadastro in enumerate(cadastros, start=1):
            print(f"Cadastro {i}:")
            print(f"Nome: {cadastro['Nome']}")
            print(f"Idade: {cadastro['Idade']}")
            print(f"Email: {cadastro['Email']}")
            print(f"Endereço: {cadastro['Endereço']}")
            print(f"Numero da Casa: {cadastro['numerocasa']}")

            print()


# Adicionando alguns cadastros de exemplo
adicionar_cadastro()
adicionar_cadastro()

# Mostrando os cadastros
print("Lista de Cadastros:")
mostrar_cadastros()
