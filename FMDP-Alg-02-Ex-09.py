'''9. Data invertida. Admitindo que uma data é lida pelo algoritmo em uma variável inteira, e não
em uma variável do tipo data, crie um programa Python que leia uma data no formato
DDMMAA e imprima essa data no formato AAMMDD, onde:
• a letra D corresponde a dois algarismos representando o dia;
• a letra M corresponde a dois algarismos representando o mês;
• a letra A corresponde aos dois últimos algarismos representando o ano.
Por exemplo: a data 110618 (11 de junho de 2018), deve ser impressa como 180611'''

# Solicita os dados.
print("Insira uma data no formato de um número inteiro organizado como DDMMAA, onde:")
print("• a letra D corresponde a dois algarismos representando o dia;")
print("• a letra M corresponde a dois algarismos representando o mês;")
print("• a letra A corresponde aos dois últimos algarismos representando o ano.")
data = int(input("DDMMAA: "))

# Limita o valor no intervalo 0<=valor<=999999

while True:
    if data >= 0 and data <= 999999:
        break
    print("Valor inválido, tente novamente.")
    data = int(input("Insira a data no formato DDMMAA: "))

# Separa os dados

DD = data // 10000 # arredonda para baixo
MM = (data // 100) % 100
AA = data % 100
'''
# Gera a data invertida

data_invertida = AA * 10000 + MM * 100 + DD

AAf = AA * 10000

MMf = MM * 100

DDf = DD
'''
# Imprime a resposta

print(f"A data invertida é {AA:02d}{MM:02d}{DD:02d}.")