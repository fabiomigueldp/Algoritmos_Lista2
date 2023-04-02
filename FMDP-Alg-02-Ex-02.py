# Unidades de tempo (novamente). Neste exercício você deve fazer o processo inverso do
# exercício anterior. Desenvolva um programa Python que recebe do usuário uma quantidade de
# tempo em segundos. Então o programa deve exibir a quantidade de tempo equivalente na
# forma D:HH:MM:SS, onde D, HH, MM e SS representam dias, horas, minutos e segundos
# respectivamente. Os valores de horas, minutos e segundos devem ser formatados todos com
# dois dígitos, sendo obrigatória a inclusão do dígito 0 para valores menores que 10.

# Início

segundos = int(input("Para converter um número em segundos para dias, horas, minutos e segundos, insira um número de segundos: "))

# Cálculo

dias = segundos // 86400
restodias = segundos % 86400

horas = restodias // 3600
restohoras = restodias % 3600

minutos = restohoras // 60
restominutos = restohoras % 60

# Impressão

print(f"{segundos} segundos, equivale a {dias} dias, {horas} horas, {minutos} minutos e {restominutos} segundos.")
print(f"D:HH:MM:SS  ->  {dias}:{horas}:{minutos}:{restominutos}.")