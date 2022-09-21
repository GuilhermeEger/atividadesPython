#Votação entre os prêmios a receber

playVotes = 0
xboxVotes = 0
nintendoVotes = 0

for i in range(5):
    vote = int(input('Qual dos consoles você gostaria de receber? (1 - Playstatios, 2 - Xbox, 3 - Nintendo) '))

    if vote == 1:
        playVotes += 1
    elif vote == 2:
        xboxVotes += 1
    elif vote == 3:
        nintendoVotes += 1
    else:
        print('Voto inválido')

if playVotes > xboxVotes and playVotes > nintendoVotes:
    print('O prêmio será um Playstation')
elif xboxVotes > playVotes and xboxVotes > nintendoVotes:
    print('O prêmio será um Xbox')
elif nintendoVotes > xboxVotes and nintendoVotes > playVotes:
    print('O prêmio será um Nintendo')
else:
    print('Empate')
