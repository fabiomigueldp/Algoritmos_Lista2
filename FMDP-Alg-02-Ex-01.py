# 1. Unidades de tempo. Crie um programa Python que leia do usuário um valor de intervalo de
# tempo expresso em número de dias, horas, minutos e segundos. O programa deve computar e
# exibir a quantidade total de segundos deste intervalo de tempo informado.

# Início

print("Insira um número de dias, horas, minutos e segundos para ver o valor total do intervalo em segundos.")

# Solocita os dados

dias = int(input("Insira o número de dias: "))
horas = int(input("Insira o número de horas: "))
minutos = int(input("Insira o número de minutos: "))
segundos = int(input("Insira o número de segundos: "))

# Cálculo

diasphoras = dias * 24
horaspminutos = (horas + diasphoras) * 60
segundostotais = ((minutos + horaspminutos) * 60) + segundos

# Imprime a resposta

print(f"   O perído de {dias} dia(s), {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")
print(f"equivale a {segundostotais} segundos.")