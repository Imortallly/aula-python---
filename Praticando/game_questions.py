import time

questions = [
    {
        "question": 'Quantas letras tem a palavra peixe? ',
        "alternatives": ['7', '9', '5', '4', '2'],
        "answer": '5',
    },
    {
        "question": 'Em que ano o titanic afundou?',
        "alternatives": ['1912', '1960', '2002', '1952', '1670'],
        "answer": '1912',
    },
    {
        "question": 'Quantos anos o João tem?',
        "alternatives": ['20', '19', '15', '29', '8'],
        "answer": '20',
    },
]
acertou = 0
print(questions[0]['question'])
print('')
print('Opções:')
alternativas_1 = questions[0]['alternatives']
for i, b in enumerate(alternativas_1, start=1):
    print(i, b, sep=') ')
print('')
first_question = input('Escolha uma opção: ')
if first_question == '3':
    print('Acertou!')
    acertou = acertou + 1
else:
    print('Errou!')
time.sleep(0.5)
print(questions[1]['question'])
print('')
print('Opções:')
alternativas_2 = questions[1]['alternatives']
for i, b in enumerate(alternativas_2, start=1):
    print(i, b, sep=') ')
print('')
second_question = input('Escolha uma opção: ')
if second_question == '1':
    print('Acertou!')
    acertou = acertou + 1
else:
    print('Errou!')
time.sleep(0.5)
print(questions[2]['question'])
print('')
print('Opções:')
alternativas_3 = questions[2]['alternatives']
for i, b in enumerate(alternativas_3, start=1):
    print(i, b, sep=') ')
print('')
third_question = input('Escolha uma opção: ')
if third_question == '1':
    print('Acertou!')
    acertou = acertou + 1
else:
    print('Errou!')

print(f"Você acertou {acertou} de 3")





