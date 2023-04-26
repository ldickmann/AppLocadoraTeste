class Cliente:
    def __init__(self, nome, cpf, idade, data_nascimento, num_carteira_motorista, foto_carteira_motorista, ano_vencimento_carteira_motorista, endereco, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.num_carteira_motorista = num_carteira_motorista
        self.foto_carteira_motorista = foto_carteira_motorista
        self.ano_vencimento_carteira_motorista = ano_vencimento_carteira_motorista
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

cliente1 = Cliente('João', '202.123.565-54', 65, '25/10/1958', 253659326, 'Foto da CNH', '20/05/2025', 'Rua Dr. Blumenau, 65', '47 988953625', 'joãoernesto@gmail.com')
cliente2 = Cliente('Maria', '302.657.982-15', 45, '12/03/1978', 326618935, 'Foto da CNH', '30/08/2024', 'Rua Tamandaré, 215', '48 999326515', 'mariagenoveva@gmail.com')
cliente3 = Cliente('Guilherme', '326.256.258-56', 22, '29/10/2000', 326598745, 'Foto da CNH', '03/03/2023', 'Rua Pedro Nestor Neto, 200', '47 988963520','guiperto@gmail.com ')


class Funcionario:
    def __init__(self, nome, cpf, idade, endereco, data_contratacao, salario, qtd_alugueis_realizados, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco
        self.data_contratacao = data_contratacao
        self.salario = salario
        self.qtd_alugueis_realizados = qtd_alugueis_realizados
        self.telefone = telefone
        self.status = True

func1 = Funcionario('Miguel', '258.326.285-56', 35, 'Rua  Miguel José, 325', '16/08/2017', 'R$2.700,00', '9', '47 988569230')
func1.status = False
func2 = Funcionario('Luana', '203.268.268-69', '40', 'Rua Joana Silva, 1230', '01/02/2019', 'R$2.300,00', '7', '47 989896253')

class Carro:
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.quilometragem = quilometragem
        self.valor_diario = valor_diario
        self.observacao = observacao

class Esportivo(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao, tempo_para_100km_por_hora, melhorias):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diario, observacao)
        self.tempo_para_100km_por_hora = tempo_para_100km_por_hora
        self.melhorias = melhorias

carro_esportivo1 = Esportivo('GHI9012', 2019, 'Branco', 'Camaro', 25000, 'R$300,00', 'Carro impecavél', 5.5, ['Rodas de liga-leve', 'Sistema de som premium'])

class Utilitario(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao, qtde_passageiros, tamanho_bagageiro, km_por_litro_gasolina):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diario, observacao)
        self.qtde_passageiros = qtde_passageiros
        self.tamanho_bagageiro = tamanho_bagageiro
        self.km_por_litro_gasolina = km_por_litro_gasolina

carro_utilit1 = Utilitario("JKL3456", 2021, "Prata", "Hilux", 10000, 'R$250,00', 'Trincado no parabrisa', 5, 'Médio', 10.5)
carro_utilit2 = Utilitario('KLB2363', 2022, 'Preto', 'Toro', 18000, 'R$300,00', 'Sem obeservação', 5, 'Médio', 12.5)

class Reserva:
    def __init__(self, carro, cliente, codigo, status, data_inicio, data_fim):
        self.carro = carro
        self.cliente = cliente
        self.codigo = codigo
        self.status = status
        self.data_inicio = data_inicio
        self.data_fim = data_fim

reserva1 = Reserva('Toro', 'João', '001', 'Ativa', '23/03/2023', '23/04/2023')

class Promocao:
    def __init__(self, titulo, descricao, data_validade):
        self.titulo = titulo
        self.descricao = descricao
        self.data_validade = data_validade
        
promocao1 = Promocao('10% em um mes', 'Se alugar um carro nosso por um mês ganhe 10% de desconto', '05/06/2023')

carros = [carro_esportivo1, carro_utilit1, carro_utilit2]

reservas = [reserva1]

print('Bem-vindo(a) ao sistema de aluguel de carros!\n')

while True:
    opcao = input('Escolha uma opção:\n1. Realizar reserva\n2. Cancelar reserva\n3. Consultar reservas\n4. Sair\n')

    if opcao == '1':
      for i, Carro in enumerate(carros):
        print(f'{i} - {carro.modelo} \n')
    elif opcao == '2':
        print('Você escolheu cancelar uma reserva.\n')
    elif opcao == '3':
       for i, reserva in enumerate(reservas):
        print(f'{i} - {reserva.carro}, {reserva.data_inicio}, {reserva.data_fim} \n')
    elif opcao == '4':
        print('Obrigado por utilizar nosso sistema. Volte sempre!')
        break
    else:
        print('Opção inválida. Escolha uma opção válida.\n')
