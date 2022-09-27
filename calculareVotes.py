#Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido

votes = [{'day':'segunda-feira', 'votes':0},{'day':'terça-feira', 'votes':0},{'day':'quarta-feira', 'votes':0},{'day':'quinta-feira', 'votes':0},{'day':'sexta-feira', 'votes':0}]

for i in range(len(votes)):
    votes[i]['votes'] = input(f'Quais foram os votos na {votes[i]["day"]}? ')

mostVoted = votes[0]["day"]

for i in range(len(votes)):

    if i > 0 and (votes[i]["votes"] > votes[i - 1]["votes"]):
        mostVoted = votes[i]["day"]

print(f'O dia mais votado foi {mostVoted}')
