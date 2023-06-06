try:
    number_1 = int(input('Digite o primeiro número: '))  
    number_2 = int(input('Digite o segundo número: '))
    expression = input('Informe a expressão desejada: ')
    if expression == '+':
        result = number_1 + number_2
    elif expression == '-':
        result = number_1 - number_2
    elif expression == '*':
        result = number_1 * number_2
    elif expression == '/':
        result = number_1 / number_2
    print(f'Resultado é: {result}')
except NameError and ValueError:
    print('Expressão ou Número Inválido')
    exit()
while True:
    try:
        sair = input('Deseja continuar? [s]im ou [n]ão: ')
        if sair == 'n' and 'N':
            break
        elif sair != 's' and 'S':
            print('Comando não aceito!')
        else: 
            number_continue = int(input('Informe o proximo número: '))
            expression = input('Informe a expressão desejada: ')
            if expression == '+':
                result = result + number_continue
            elif expression == '-':
                result = result - number_continue
            elif expression == '*':
                result = result * number_continue
            elif expression == '/':
                result = result / number_continue
            else:
                print('Expressão invalida')
            print(f'o Resultado é: {result}')
    except (ValueError, NameError):
            print('Expressão ou número inválido')
            exit()
print('Calculadora finalizada! Se caso queria reiniciar aperte o Play')


