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