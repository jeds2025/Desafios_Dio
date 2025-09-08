from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco): # Inicializa o cliente com um endereço e uma lista vazia de contas
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao): # Realiza uma transação (depósito ou saque) em uma conta específica
        transacao.registrar(conta)

    def adicionar_conta(self, conta): # Adiciona uma nova conta à lista de contas do cliente
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco): # Inicializa com nome, data de nascimento, CPF e endereço, chamando o construtor da superclasse
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __str__(self): # Retorna uma string com informações básicas do cliente
        return f"Nome: {self.nome}, CPF: {self.cpf}"


class Conta:
    def __init__(self, numero, cliente): # Inicializa a conta com número, cliente e configurações padrão
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero): # Método de fábrica para criar uma nova instância de conta
        return cls(numero, cliente)

    @property
    def saldo(self): # Propriedade para acessar o saldo da conta
        return self._saldo

    @property
    def numero(self): # Propriedade para acessar o número da conta
        return self._numero

    @property
    def agencia(self): # Propriedade para acessar a agência da conta
        return self._agencia

    @property
    def cliente(self): # Propriedade para acessar o cliente associado à conta
        return self._cliente

    @property
    def historico(self): # Propriedade para acessar o histórico de transações
        return self._historico

    def sacar(self, valor): # Realiza um saque, verificando saldo e validade do valor
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n---> Operação falhou! Você não tem saldo suficiente. <---")
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n---> Operação falhou! O valor informado é inválido. <---")
        return False

    def depositar(self, valor): # Realiza um depósito, verificando se o valor é válido
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        print("\n---> Operação falhou! O valor informado é inválido. <---")
        return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3): # Inicializa a conta corrente com limite de saque e número máximo de saques
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self): # Propriedade para acessar o limite de saque
        return self._limite

    @property
    def limite_saques(self): # Propriedade para acessar o limite de saques diários
        return self._limite_saques

    def sacar(self, valor): # Sobrescreve o método sacar para incluir limites específicos da conta corrente
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n---> Operação falhou! O valor do saque excede o limite. <---")
        elif excedeu_saques:
            print("\n---> Operação falhou! Número máximo de saques excedido. <---")
        else:
            return super().sacar(valor)
        return False

    def __str__(self): # Retorna uma string formatada com informações da conta
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self): # Inicializa uma lista vazia para armazenar transações
        self._transacoes = []

    @property
    def transacoes(self): # Propriedade para acessar a lista de transações
        return self._transacoes

    def adicionar_transacao(self, transacao): # Adiciona uma nova transação ao histórico com tipo, valor e data
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self): # Propriedade abstrata para o valor da transação
        pass

    @abstractmethod
    def registrar(self, conta): # Método abstrato para registrar a transação em uma conta
        pass

class Deposito(Transacao): 
    def __init__(self, valor): # Inicializa um depósito com um valor específico
        self._valor = valor

    @property
    def valor(self): # Retorna o valor do depósito
        return self._valor

    def registrar(self, conta): # Registra o depósito na conta e adiciona ao histórico se bem-sucedido
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor): # Inicializa um saque com um valor específico
        self._valor = valor

    @property
    def valor(self): # Retorna o valor do saque
        return self._valor

    def registrar(self, conta): # Registra o saque na conta e adiciona ao histórico se bem-sucedido
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

