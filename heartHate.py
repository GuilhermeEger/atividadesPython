#Verificar os batimentos cardíacos

age = int(input('Por favor, insira sua idade: '))
hearthRate = int(input('Por favor, insira sua frequência cardiaca: '))

if age <= 2 and (hearthRate >= 120 and hearthRate <= 140):
    print('Batimentos normais')
elif (age >= 8 and age <= 17) and (hearthRate >= 80 and hearthRate <= 100):
    print('Batimentos normais')
elif (age >= 18) and (hearthRate >= 70 and hearthRate <= 80):
    print('Batimentos normais')
elif (age >= 60) and (hearthRate >= 50 and hearthRate <= 60):
    print('Batimentos normais')
else:
    print('Batimentos anormais')
















