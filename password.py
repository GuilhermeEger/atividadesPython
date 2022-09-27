#Senha para se recuperar do ataque hacker

nowMinute = int(input('Qual o minuto atual do seu relógio? '))
result = 1
n = 1

for n in range(1,nowMinute+1):
    result *= n

print(f'A senha para recuperar seus dados é: {"LIBERDADE" + str(result)}')