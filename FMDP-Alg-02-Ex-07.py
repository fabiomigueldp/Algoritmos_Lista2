'''7. Centena, dezena, unidade. Dado um número de três algarismos N = CDU (onde C é o
algarismo das centenas, D é o algarismo das dezenas e U o algarismo das unidades) Faça um
programa Python que receba do usuário o número inteiro N, e imprima separadamente a
centena, a dezena e a unidade.'''

# Solicita os dados

CDU = int(input("Insira um número inteiro de três algarismos: "))

# Limita o valor no intervalo 0<=valor<=99

while True:
    if CDU >= -999 and CDU <= 999:
        break
    print("Valor inválido, tente novamente.")
    CDU = int(input("Insira um número inteiro de três algarismos: "))

# Defnine CDU

C = CDU // 100

D = (CDU // 10) % 10

U = CDU % 10

# Imprime a resposta

print(f"Centena = {C}.")
print(f"Dezena = {D}.")
print(f"Unidade = {U}.")



