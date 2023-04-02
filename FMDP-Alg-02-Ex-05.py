'''5. Calculando o troco. Considere o software que controla uma máquina automática de compras.
Uma tarefa que ele precisa realizar é determinar quanto troco fornecer ao comprador quando
este faz o pagamento em dinheiro. Escreva um programa Python que inicia lendo do usuario
uma quantidade de centavos como um número inteiro (portanto vamos considerar números de
0 a 99). Então o seu programa deve calcular e exibir quantidade e o valor de cada moeda para
compor este troco em centavos informado. O troco deve ser montado com a menor quantidade
possível de moedas. Assuma que a máquina possui moedas de 50, 25, 10, 5 e 1 centavos.'''

# Solicita o valor do troco em centavos 

valor = int(input("Insira a parte em centavos do valor do troco: "))

# Limita o valor no intervalo 0<=valor<=99

while True:
    if valor >= 0 and valor <= 99:
        break
    print("Valor inválido, tente novamente.")
    valor = int(input("Insira a parte em centavos do valor do troco: "))

# Cálculo

moedas50 = valor // 50
valor %= 50

moedas25 = valor // 25
valor %= 25

moedas10 = valor // 10
valor %= 10

moedas5 = valor // 5
valor %= 5

moedas1 = valor

# Imprime a resposta

print(f"Moedas de 50 centavos: {moedas50}.")
print(f"Moedas de 25 centavos: {moedas25}.")
print(f"Moedas de 10 centavos: {moedas10}.")
print(f"Moedas de 5 centavos: {moedas5}.")
print(f"Moedas de 1 centavo: {moedas1}.")
