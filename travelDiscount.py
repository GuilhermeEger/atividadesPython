#Desconto na compra de pacotes

travelValue = int(input('Qual o valor da viagem? '))
travelCategory = int(input('Qual a categoria da sua viagem? (1 - Econômica, 2 - Executiva, 3 - Primeira classe) '))
travelPassengersNumber = int(input('Quantos passageiros irão? '))
discountTravelValue = 0

if travelCategory == 1:
    if travelPassengersNumber == 2:
        discount = 0.03
    elif travelPassengersNumber == 3:
        discount = 0.04
    elif travelPassengersNumber >= 4:
        discount = 0.05
elif travelCategory == 2:
    if travelPassengersNumber == 2:
        discount = 0.05
    elif travelPassengersNumber == 3:
        discount = 0.07
    elif travelPassengersNumber >= 4:
        discount = 0.08
elif travelCategory == 3:
    if travelPassengersNumber == 2:
        discount = 0.10
    elif travelPassengersNumber == 3:
        discount = 0.15
    elif travelPassengersNumber >= 4:
        discount = 0.20

discountTravelValue = travelValue * discount

print(f'Valor da viagem sem desconto: {travelValue}')
print(f'{discount * 100:,.1f}% de desconto')
print(f'Valor com desconto: {travelValue - discountTravelValue}')
print(f'O valor médio por viajante é de {discountTravelValue / travelPassengersNumber:,.2f}')