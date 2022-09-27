#Calcular notas dos alunos da escola de inglês JoWell Sant’ana

def createList(r1, r2):
    return [item for item in range(r1, r2+1)]

def separeteList(mode):
    list = createList(0, 50)
    for ele in list:
        if mode == 2 and (ele % 2 == 0):
            list.remove(ele)
        elif ele % 2 == 1:
            list.remove(ele)
    return list

def runGrades(mode, list):

    total = 0

    if mode == 1:
        for i in range(len(oddnumbers)):
            print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES')
            total += int(input(f'Por favor digite a nota do aluno {oddnumbers[i]}: '))
    else:
        for i in range(len(evenNumbers)):
            print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES')
            total += int(input(f'Por favor digite a nota do aluno {evenNumbers[i]}: '))

    return total

def calculateGreater(result1,result2):

    if result1['value'] > result2['value']:
        return result1["name"]
    else:
        return result2["name"]

oddnumbers = separeteList(1)
evenNumbers = separeteList(2)
totalOdd = runGrades(2,oddnumbers)
totalEven = runGrades(1,evenNumbers)

print(f'A média do alunos pares foi: {totalOdd / len(oddnumbers)}')
print(f'A média do alunos pares foi: {totalEven / len(evenNumbers)}')
print(f'A metade que teve a maior médio foi a {calculateGreater({"value":totalOdd,"name":"impar"},{"value":totalEven,"name":"pares"})}')