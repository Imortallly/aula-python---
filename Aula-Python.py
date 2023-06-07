try:
    number_1 = float(input('Digite o primeiro número: '))  
    number_2 = float(input('Digite o segundo número: '))
    expression = input('Informe a expressão desejada: ')
    if expression == '+':
        result = number_1 + number_2
    elif expression == '-':
        result = number_1 - number_2
    elif expression == '*':
        result = number_1 * number_2
    elif expression == '/':
        result = number_1 / number_2
    print(f'Resultado é: {result:.2f}')
except (NameError, ValueError):
    print('Expressão ou Número Inválido')
    exit()
while True:
    exit_expression = input('Deseja continuar? [y]Sim ou [n]Não: ')
    if exit_expression.lower() == 'n':
        break
    elif exit_expression.lower() != 'y':
        print('Comando não aceito!')
    else: 
        number_continue = float(input('Informe o proximo número: '))
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
            print('Expressão ou Número Inválido')
            exit()  
        print(f'o Resultado é: {result:.2f}')
print('Calculadora finalizada! Se caso queria reiniciar aperte o Play')


