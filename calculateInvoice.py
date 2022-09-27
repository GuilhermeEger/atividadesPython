#Criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês.

def getSubscriptionType():
    subscriptionType = int(input('Por favor, qual seu tipo de assinatura? (1 - Basic, 2 - Silver, 3 - Gold, 4 - Platinum): '))

    if subscriptionType < 1 or subscriptionType > 4:
        print('Desculpe, valor inválido, digite novamente.')
        getSubscriptionType()
    else:
        calculeInvoice(subscriptionType)

def calculeInvoice(subscriptionType):
    anualInvoicing = int(input('Por favor, qual seu faturamento anual? '))
    result = 0

    if subscriptionType == 1:
        result = anualInvoicing * 0.3
    elif subscriptionType == 2:
        result = anualInvoicing * 0.2
    elif subscriptionType == 3:
        result = anualInvoicing * 0.1
    elif subscriptionType == 4:
        result = anualInvoicing * 0.05

    print(f'O custo pelos serviços prestados é de {result}')

getSubscriptionType()