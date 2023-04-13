'''8. Centena, dezena, unidade (novamente). Dado um número de três algarismos N = CDU
(onde C é o algarismo das centenas, D é o algarismo das dezenas e U o algarismo das
unidades), considere o número M constituído pelos algarismos de N em ordem inversa, isto é,
M=UDC. Faça um programa Python para gerar e imprimir M a partir de N (p.ex.:N=123
->M=321).'''

# Solicita os dados

CDU = int(input("Insira um número inteiro de três algarismos: "))

# Limita o valor no intervalo 0<=valor<=99

while True:
    if CDU >= -999 and CDU <= 999:
        break
    print("Valor inválido, tente novamente.")
    CDU = int(input("Insira um número inteiro de três algarismos: "))

# Separa CDU

if CDU < 0:
    C = (-CDU // 100) # arredonda para baixo
    D = (-CDU // 10) % 10
    U = -CDU % 10
else:
    C = CDU // 100
    D = (CDU // 10) % 10
    U = CDU % 10

# Gera M
'''
CM = U * 100

DM = D * 10

UM = C
'''

M = U * 100 + D * 10 + C

# Imprime M

print("   Considerando que o número inserido é N, constituido por três algarismos, centena (C); dezena (D);")
print("unidade (U), organizados dessa forma como CDU, um número M imaginado a partir de N, utilizando os")
print(f"algarismos de N, mas na ordem UDC, será M = {M}.")