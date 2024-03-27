#laço #loop #menu
while True:
    opcao = menu()
    if opcao == 1:
        print('Carros disponíveis para reserva.')
        carros_disponiveis = lista_carros(carros)
        for i, carro in enumerate(carros_disponiveis):
          print(f'{i} - {carro.modelo} - {carro.cor} - {carro.ano} - {carro.observacao} - {carro.valor_diario} \n')
        carro_escolhido = int(input('Diga qual carro tu tens interesse: '))
        if 0 <= carro_escolhido < len(carros_disponiveis):
            cliente_escolhido = str(input('Qual seu nome? '))
            cliente_existente = clientes.buscar_cliente_nome(cliente_escolhido)
            if cliente_existente:
                print('Cliente já é cadastrado:   \n', cliente_existente.nome)
                data_inicio = date.fromtimestamp(time.mktime(time.strptime(input('Qual a data de reserva (formato dd/mm/aaaa): '), '%d/%m/%Y')))
                data_fim = date.fromtimestamp(time.mktime(time.strptime(input('Qual a data para a devolução do veículo (formato dd/mm/aaaa): '), '%d/%m/%Y')))
                codigo_reserva = input('Informe um código da reserva: ')
                nova_reserva = Reserva(carros[carro_escolhido], cliente_existente, codigo_reserva, 'Ativa', data_inicio, data_fim)
                reservas.append(nova_reserva)
                print('Reserva realizada com sucesso!')
            else:
                cpf_novo_cliente = int(input('Digite o seu CPF: '))
                idade_novo_cliente = int(input('Qual a sua idade? '))
                data_nascimento = date.fromtimestamp(time.mktime(time.strptime(input('Qual a sua data de nascimento (formato dd/mm/aaaa)? '), '%d/%m/%Y')))
                num_carteira_motorista = int(input('Qual o número da sua CNH? '))
                ano_vencimento_carteira_motorista = int(input('Qual o ano de vencimento da sua CNH? '))
                endereco = str(input('Qual a rua que você reside? '))
                telefone = int(input('Qual seu número de celular? '))
                email = str(input('Informe seu email: '))
                novo_cliente = Cliente(cliente_escolhido, cpf_novo_cliente, idade_novo_cliente, data_nascimento, num_carteira_motorista, ano_vencimento_carteira_motorista, endereco, telefone, email)
                clientes.adicionar_cliente(novo_cliente)
                print('Fosse cadastrado com sucesso!')
                print('Cliente encontrado!')
                data_inicio = date.fromtimestamp(time.mktime(time.strptime(input('Qual a data de reserva (formato dd/mm/aaaa): '), '%d/%m/%Y')))
                data_fim = date.fromtimestamp(time.mktime(time.strptime(input('Qual a data para a devolução do veículo (formato dd/mm/aaaa): '), '%d/%m/%Y')))
                codigo_reserva = input('Informe um código da reserva: ')
                nova_reserva = Reserva(carros[carro_escolhido], cliente_existente, codigo_reserva, 'Ativa', data_inicio, data_fim)
                reservas.append(nova_reserva)
                print('Reserva realizada com sucesso!')
    elif opcao == 2:
        print('Você escolheu cancelar uma reserva.\n')
        cancelar_reserva()
    elif opcao == 3:
        codigo_reserva = input('Qual o código da reserva? \n')
        reserva_encontrada = None
        for reserva in lista_de_reservas:
            if reserva.codigo_reserva == codigo_reserva and reserva.status == 'Ativa':
                reserva_encontrada = reserva
                break
        if reserva_encontrada:
            print('Reserva encontrada:')
            print(f'Carro: {reserva_encontrada.carro.modelo}, Status: {reserva_encontrada.status}, Data de Término: {reserva_encontrada.data_fim}')
        else:
            print('Reserva não encontrada!')
    elif opcao == 4:
        print('Obrigado por utilizar nosso sistema. Volte sempre!')
        break
    else:
        print('Opção inválida. Escolha uma opção válida.\n')
