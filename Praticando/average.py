from datetime import datetime
data = datetime.today()

# Dados fictícios do banco de dados
dados_aluno = {
    "nome": "João Vitor Gomes Nunes",
    "cpf": "113.641.299-90",
    "nascimento": "08/08/2002",
    "matricula": 123123123
}
# ---------------------------------

while True:
        numero_matricula = input('Digite o número da matrícula: ')
        conversor_matricula_input = int(numero_matricula)
        numero_caracteres_matricula = len(numero_matricula)

        if numero_matricula == dados_aluno['matricula']: # Verifica se a matricula está cadastrada
                print('Matricula encontrada') 

        elif numero_caracteres_matricula > dados_aluno['matricula'] and conversor_matricula_input < dados_aluno['matricula']: #Verifica se a matricula tem numero de caracteres validos
                print('Matricula invalida')
                continue
        else: 
                print('Matricula não encontrada!')
                continue
        nome_aluno = input('Digite o nome do aluno: ') 
        if nome_aluno.isdigit() or not nome_aluno: # Verifica se o nome digitado no input é uma string
                print('Nome invalido!')
                continue
        elif not nome_aluno == dados_aluno ['nome']: # Verifica se o nome do aluno está cadastrado no banco de dados
                print('Nome de aluno não encontrado')
                continue
        else:
                print('Nome encontrado')
        print('Digite sem barra(/) ou travessão(-)')
        nascimento_aluno = input('Digite a data de nascimento do aluno: ')
        numero_caracteres_nascimento = len(nascimento_aluno)
        if nascimento_aluno.isnumeric() and not nascimento_aluno: # Verifica se a data de nascimento é um inteiro
                pass    
        elif numero_caracteres_nascimento > dados_aluno['nascimento'] and numero_caracteres_nascimento < dados_aluno['nascimento']: # Verifica se o numero de caracteres é valido
                print('Caracteres ultrapassam o limite')
                continue
        elif nascimento_aluno == dados_aluno['nascimento']: # Verifica se está cadastrado no banco de dados
                print('Encontrado')
        else: 
                print('Nascimento invalido!')
                continue
        cpf_aluno = input('Digite o CPF do aluno: ')
        numero_caracteres_cpf = len(cpf_aluno)
        if numero_caracteres_cpf > dados_aluno['cpf'] and numero_caracteres_cpf < dados_aluno['cpf']:
                print('Número de caracteres invalido')
                continue
        nota_1 = float(input('Digite a primeira nota do aluno: '))
        nota_2 = float(input('Digite a segunda nota do aluno: '))
        nota_3 = float(input('Digite a terceira nota do aluno: '))
        break


lista_nota = [nota_1, nota_2, nota_3]
media_de_notas = (nota_1 + nota_2 + nota_3)/3





