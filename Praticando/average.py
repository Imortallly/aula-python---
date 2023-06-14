from datetime import datetime
data = datetime.today()

# Dados fictícios do banco de dados
dados_aluno = {
    "nome": "João Vitor Gomes Nunes",
    "cpf": "11364129990",
    "nascimento": "08082002",
    "matricula": "123123123"
}
# ---------------------------------

while True:
        numero_matricula = input('Digite o número da matrícula: ')
        numero_caracteres_matricula_bd = len(dados_aluno['matricula'])

        if numero_matricula == dados_aluno['matricula']: # Verifica se a matricula está cadastrada
                print('Matricula encontrada') 

        elif len(numero_matricula) > len(dados_aluno['matricula']) or len(numero_matricula) < numero_caracteres_matricula_bd: #Verifica se a matricula tem numero de caracteres validos
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
                print('Nome encontrado!')
        print('--Não use barra(/) ou travessão(-)--')
        nascimento_aluno = input('Digite a data de nascimento do aluno: ')
        numero_caracteres_nascimento = len(nascimento_aluno)
        if nascimento_aluno.isnumeric() and not nascimento_aluno: # Verifica se a data de nascimento é um inteiro
                pass    
        elif numero_caracteres_nascimento > len(dados_aluno['nascimento']) or numero_caracteres_nascimento < len(dados_aluno['nascimento']): # Verifica se o numero de caracteres é valido
                print('Caracteres ultrapassam o limite')
                continue
        elif nascimento_aluno == dados_aluno['nascimento']: # Verifica se está cadastrado no banco de dados
                print('Encontrado')
        else: 
                print('Nascimento invalido!')
                continue
        cpf_aluno = input('Digite o CPF do aluno: ')
        if len(cpf_aluno) > len(dados_aluno['cpf']) or len(cpf_aluno)< len(dados_aluno['cpf']): # Verifica se o numero de caracteres é valido
                print('Número de caracteres invalido')
                continue
        elif cpf_aluno == dados_aluno['cpf']: # Verifica se está cadastrado no banco de dados
                print('CPF Encontrado!')
        notas = {
                "nota_1": float(input('Digite a primeira nota do aluno: ')),
                "nota_2": float(input('Digite a segunda nota do aluno: ')),
                "nota_3": float(input('Digite a terceira nota do aluno: ')),
                "nota_4": float(input('Digite a quarta nota do aluno: ')),
                } 
        break

media_de_notas = (notas['nota_1'] + notas['nota_2'] + notas['nota_3'] + notas['nota_4'])/4
nota_mais_alta = max(notas.values())
nota_mais_baixa = min(notas.values())
formatacao_nascimento = dados_aluno['nascimento']
data_formatada = f'{formatacao_nascimento[:2]}/{formatacao_nascimento[2:4]}/{formatacao_nascimento[4:]}'
formacao_cpf = dados_aluno['cpf']
cpf_formatada = f'{formacao_cpf[:3]}.{formacao_cpf[3:6]}.{formacao_cpf[6:9]}-{formacao_cpf[9:]}'
data_e_hora_em_texto = data.strftime('%d/%m/%Y %H:%M')

print(f'O aluno: {dados_aluno["nome"]}, nascido na data de {data_formatada}, no cpf {cpf_formatada}, com a matrícula {dados_aluno["matricula"]}. A média final o aluno é {media_de_notas},\
 sendo a nota mais alta {nota_mais_alta} e a nota mais baixa {nota_mais_baixa}')
print(f'Capivari de Baixo, {data_e_hora_em_texto}')





