'''4. Ordenação de 3 inteiros. Crie um programa que obtém 3 números inteiros do usuário e os
exibe de forma ordenada do menor para o maior. Use as funções min e max para encontrar o
menor valor e o maior valor. Dica: o valor do meio pode ser obtido pela soma dos três valores,
subtraída do maior e do menor.'''

#Início

print("Insira 3 números inteiros aleatórios para o programa ordena-los em ordem crescente:")

# Solicita os dados

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

# Ordena utilizando a função max e a função min

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
meio = num1 + num2 + num3 - maior - menor

# Imprime a resposta

print(f"Os números em ordem crescente são: {menor},{meio} e {maior}.")