#Classe Cliente
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

#Classe Clientes
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

  #classe
  class Carro:
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.quilometragem = quilometragem
        self.valor_diario = valor_diario
        self.observacao = observacao

#subclasse
class Esportivo(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao, tempo_para_100km_por_hora, melhorias):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diario, observacao)
        self.tempo_para_100km_por_hora = tempo_para_100km_por_hora
        self.melhorias = melhorias

#subclasse
class Utilitario(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao, qtde_passageiros, tamanho_bagageiro, km_por_litro_gasolina):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diario, observacao)
        self.qtde_passageiros = qtde_passageiros
        self.tamanho_bagageiro = tamanho_bagageiro
        self.km_por_litro_gasolina = km_por_litro_gasolina
      
#funçãoLista
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

    #metododeClasse
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

#classePromoção
class Promocao:
    def __init__(self, titulo, descricao, data_validade):
        self.titulo = titulo
        self.descricao = descricao
        self.data_validade = data_validade

    def __str__(self):
     return f'Promoção: {self.titulo}\nDescrição: {self.descricao}\nData de Validade: {self.data_validade}'

#funçãoMenu
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
