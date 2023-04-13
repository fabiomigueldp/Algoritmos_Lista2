'''10. Número de matrícula. Suponha que uma escola utilize, como código de matrícula, um
número inteiro no formato AASDDD, onde:
• os dois primeiros dígitos, representados pela letra A, são os dois últimos algarismos do ano
da matrícula;
• o terceiro dígitos, representado pela letra S, vale 1 ou 2, conforme o aluno tenha se
matriculado no 1o ou 2o semestre;
• os três últimos dígitos, representados pela letra D, correspondem à ordem da matrícula do
aluno, no semestre e no ano em questão.
Crie um programa Python que leia o número de matrícula de um aluno e imprima o ano e o
semestre em que ele foi matriculado. Por exemplo, um número de matrícula 182034 deve
resultar ano 18 e semestre 2.'''

# Solicita o número de matrícula

codMatricula = int(input("Insira o número de matrícula do aluno: "))

# Limita o valor no intervalo 0<=valor<=99

while True:
    if codMatricula >= -999999 and codMatricula <= 999999:
        break
    print("Valor inválido, tente novamente.")
    codMatricula = int(input("Insira o número de matrícula do aluno: "))

# Separa AASDDD

AA = codMatricula // 10000
S = ((codMatricula // 1000) % 10)
DDD = codMatricula % 1000

# Gera o ano

ano = "20" + str(AA)

# Gera semestre

if S == 1:
    semestre = "1º semestre"
elif S == 2:
    semestre = "2º semestre"

# Imprime a resposta

print(f"O aluno foi matriculado no ano de {ano}, no {semestre}, com o número {DDD}.")