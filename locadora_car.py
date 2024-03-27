#python
#developer

#################################
#Desenvolvido por Lucas Dickmann#
##### LuksCar #### Locadora #####
#################################

import time #importar modulo time
from datetime import date #biblioteca datatime

#ClasseCliente
class Cliente:
    def __init__(self, nome, cpf, idade, data_nascimento, num_carteira_motorista, ano_vencimento_carteira_motorista, endereco, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.num_carteira_motorista = num_carteira_motorista
        self.ano_vencimento_carteira_motorista = ano_vencimento_carteira_motorista
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

#Instancias da classe Cliente
cliente0 = Cliente('João', '202.123.565-54', 65, '25/10/1958', 253659326, '20/05/2025', 'Rua Dr. Blumenau, 65', '47 988953625', 'joãoernesto@gmail.com')
cliente1 = Cliente('Maria', '302.657.982-15', 45, '12/03/1978', 326618935, '30/08/2024', 'Rua Tamandaré, 215', '48 999326515', 'mariagenoveva@gmail.com')
cliente2 = Cliente('Guilherme', '326.256.258-56', 22, '29/10/2000', 326598745, '03/03/2027', 'Rua Pedro Nestor Neto, 200', '47 988963520','guiperto@gmail.com')

#ClasseClientes
class Clientes:
    def __init__(self):
        self.clientes_lista = []

    def adicionar_cliente(self, cliente):
        self.clientes_lista.append(cliente)

    def buscar_cliente_nome(self, nome):
        for cliente in self.clientes_lista:
            if cliente.nome == nome:
                return cliente
        return None

clientes = Clientes()

clientes.adicionar_cliente(cliente0)
clientes.adicionar_cliente(cliente1)
clientes.adicionar_cliente(cliente2)

#classeCarro
class Carro:
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.quilometragem = quilometragem
        self.valor_diario = valor_diario
        self.observacao = observacao


#subClasseEsport
class Esportivo(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao, tempo_para_100km_por_hora, melhorias):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diario, observacao)
        self.tempo_para_100km_por_hora = tempo_para_100km_por_hora
        self.melhorias = melhorias

carro_esportivo0 = Esportivo('GHI9012', 2019, 'Branco', 'Camaro', 25000, 'R$300,00', 'Carro impecavél', 5.5, ['Rodas de liga-leve', 'Sistema de som premium'])
carro_esportivo1 = Esportivo('JLK6587', 2021, 'Cinza', 'Porshe', 5600, 'R$500,00', 'Conversivel', 3.0, ['Sistema de som premium'])
carro_esportivo2 = Esportivo('ARG2036', 2018, 'Bordo', 'Range Rover', 12000, 'R$390,00', 'Controle de estabilidade e Leitura de pista', 6.0, ['Cambio'])
carro_esportivo3 = Esportivo('DRS5978', 2022, 'Preto', 'Lamborghini', 8400, 'R$650,00', 'Impecavél', 5.5, ['Não há melhorias a serem feitas'])

#subClasseUtilit
class Utilitario(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao, qtde_passageiros, tamanho_bagageiro, km_por_litro_gasolina):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diario, observacao)
        self.qtde_passageiros = qtde_passageiros
        self.tamanho_bagageiro = tamanho_bagageiro
        self.km_por_litro_gasolina = km_por_litro_gasolina

carro_utilit0 = Utilitario('JKL3456', 2021, 'Prata', 'Hilux', 10000, 'R$250,00', 'Trincado no parabrisa', 5, 'Médio', 10.5)
carro_utilit1 = Utilitario('KLB2363', 2022, 'Preto', 'Toro', 18000, 'R$300,00', 'Sem obeservação', 5, 'Médio', 12.5)

carros = [carro_esportivo0, carro_esportivo1, carro_esportivo2, carro_esportivo3, carro_utilit0, carro_utilit1]

#funçãoListaCarros
def lista_carros(carros, modelo=None, ano=None, cor=None, valor_diario=None, observacao=None):
    carros_disponiveis = []
    for carro in carros:
        if (modelo is None or carro.modelo == modelo) and \
           (ano is None or carro.ano == ano) and \
           (cor is None or carro.cor == cor) and \
           (valor_diario is None or carro.valor_diario == valor_diario) and \
           (observacao is None or carro.observacao == observacao):
            carros_disponiveis.append(carro)
    return carros_disponiveis

#classeReserva
class Reserva:
    def __init__(self, carro, cliente, codigo_reserva, status, data_inicio, data_fim):
        self.carro = carro
        self.cliente = cliente
        self.codigo_reserva = codigo_reserva
        self.status = status
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    #metodoDdClasse
    def buscar_reserva(carros, reservas, status, data_fim):
        reservas_constatadas = []
        for reserva in reservas:
            if reserva.carro == carro and reserva.status == status and reserva.data_fim == data_fim:
                reservas_constatadas.append(reserva)
        return reservas_constatadas

    def cancelar_reserva(self):
        if self.status == 'Ativa':
            self.status = 'Cancelada'
            print('Reserva cancelada!')
        else:
            print('Reserva já cancelada ou concluída.')

#funçãoCancelarReserva
def cancelar_reserva():
    codigo_reserva = input('Informe o código da reserva que deseja cancelar: ')
    reserva_encontrada = None
    for reserva in lista_de_reservas:
        if reserva.codigo_reserva == codigo_reserva and reserva.status == 'Ativa':
            reserva_encontrada = reserva
            break
    if reserva_encontrada:
        reserva_encontrada.cancelar_reserva()
    else:
        print('Reserva já cancelada ou inexistente.')

reservas = []

lista_de_reservas = []

lista_de_reservas.append(Reserva(carro_utilit0, cliente0, '000', 'Ativa', '22/03/2024', '23/05/2024'))
lista_de_reservas.append(Reserva(carro_esportivo0, cliente1, '001', 'Ativa', '15/03/2023', '30/04/2023'))
lista_de_reservas.append(Reserva(carro_utilit1, cliente2, '002', 'Ativa', '20/03/2024', '23/06/2024'))

#classePromoção
class Promocao:
    def __init__(self, titulo, descricao, data_validade):
        self.titulo = titulo
        self.descricao = descricao
        self.data_validade = data_validade

    def __str__(self):
     return f'Promoção: {self.titulo}\nDescrição: {self.descricao}\nData de Validade: {self.data_validade}'

#imprimiPromoção
promocao0 = Promocao('10% por 30 dias', 'Se alugar um carro nosso por um mês ganhe 10% de desconto', '05/06/2023 \n')
print(promocao0)

#funcaoMenuLocadora #ChamadanoWhile
def menu():
    print('###########################')
    print('****Bem vindo a LuksCar****')
    print('1*****Realizar reserva*****')
    print('2*****Cancelar reserva*****')
    print('3****Consultar reservas****')
    print('4******SAIR DO MENU********')
    print('###########################')
    opcao = int(input('Qual a tua opção? '))
    return opcao


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
