lista_de_compras = []

while True:
    try:
        print('Selecione uma opção')
        pergunta = input('[i]nserir [a]pagar [l]istar: ')
        if pergunta == 'i':
            inserir = input('Valor: ')
            lista_de_compras.append(inserir)
            print(f'Produto: {inserir} adicionado')
            continue
        elif pergunta == 'a':
            apagar = int(input('Escolha o indice para apagar: '))
            if not lista_de_compras == []:
                lista_de_compras.pop(apagar)
                print('Produto apagado')
            else: 
                print('Não ha nada para apagar')
        elif pergunta == 'l':
            if not lista_de_compras == []:
                print('LISTA DE COMPRARAS')
                for numero, produto in enumerate(lista_de_compras, start=1):
                    print(numero, produto)
            else:
                print('Não há nada para listar')
                continue
        else: 
            print('Opção invalida')
            continue
    except:
        print('Comando inválido')
        continue


