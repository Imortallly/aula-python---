while True: # O código começa com um loop while True para solicitar ao usuário que digite um CPF válido. 
    cpf_digitado = input('Digite o CPF para verificação: ') 
    if len(cpf_digitado) != 14: # Ele solicita ao usuário que digite o CPF e verifica se o comprimento do CPF digitado é diferente de 14 (incluindo a pontuação). Se for diferente, exibe a mensagem "CPF inválido".
        print('CPF invalido')
    else: 
        break # Caso o CPF tenha o comprimento válido, o loop é interrompido com o break.

cpf_sem_pontuacao = cpf_digitado.replace('.', "").replace('-', "") # Nesta linha, o código remove a pontuação do CPF digitado utilizando os métodos replace() para substituir os pontos (.) e o hífen (-) por uma string vazia "". O resultado é armazenado na variável cpf_sem_pontuacao.
soma_cpf = 0 # Aqui são definidas as variáveis soma_cpf, contagem e soma_total_cpf com valores iniciais.
contagem = 10
soma_total_cpf = 0

for contagem_cpf in str(cpf_sem_pontuacao)[:9]: # O código inicia um loop for para percorrer os primeiros nove dígitos do CPF (excluindo o dígito verificador).
    soma_cpf = contagem * int(contagem_cpf) # Em cada iteração, ele multiplica o dígito do CPF pela contagem atual e atualiza as variáveis soma_cpf, contagem e soma_total_cpf.
    contagem = contagem - 1
    soma_total_cpf = soma_cpf + soma_total_cpf

resultado_cpf = (soma_total_cpf * 10) % 11 # Aqui é calculado o dígito verificador do CPF multiplicando a soma_total_cpf por 10 e fazendo o módulo 11.

if resultado_cpf > 9:
    print('CPF valido com digito 0') # Por fim, o código verifica se o resultado do cálculo é maior que 9. 
else: # Se for maior, exibe a mensagem "CPF válido com dígito 0".
    print(f'CPF valido com digito {resultado_cpf}') # Caso contrário, exibe a mensagem "CPF válido com dígito {resultado_cpf}", em que {resultado_cpf} é o valor do dígito verificador calculado.