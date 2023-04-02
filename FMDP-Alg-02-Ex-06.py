'''6. Soma dos dígitos de um inteiro. Desenvolva um programa que obtenha do usuário um
número inteiro de 4 dígitos e exiba a soma dos dígitos do número. Por exemplo, se o usuário
fornecer o número 3141, então seu programa deve exibir o número 9 (3 + 1 + 4 + 1).'''

# Solicita os dados

numero = input("Digite um número de 4 dígitos: ")

# Define a soma

soma = 0

# Itera sobre cada caractere da str de numero e adiciona-o à variável soma

for digito in numero:
    soma += int(digito)
print("A soma dos dígitos é:", soma)

# Imprime a resposta

print(f"A soma dos quatro dígitos de {numero}, é {soma}.")
