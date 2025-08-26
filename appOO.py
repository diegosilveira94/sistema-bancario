from abc import ABC, abstractmethod
from datetime import datetime

class Cliente():
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nasc,endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc

class Conta():
    def __init__(self, saldo, num_conta, agencia, cliente, historico):
        self._saldo = saldo
        self._num_conta = num_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, num_conta):
        return cls(num_conta, cliente)
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def num_conta(self):
        return self._num_conta
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self.historico
    
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo o suficiente. @@@")
        elif valor > 0:
            self._saldo -= valor
            print("\n⇛ Saque realizado com sucesso! ⇚")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
        return False
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n⇛ Depósito realizado com sucesso! ⇚")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self,saldo, num_conta, agencia, cliente, historico, limite_saques=3, limite=500):
        super().__init__(saldo, num_conta, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        
        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        
        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            """

class Historico():
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao._class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strtime("%d-%m-%Y %H:%M:%s"),
            }
        )
    
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        super().__init__()
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            
class Saque(Transacao):
    def __init__(self, valor):
        super().__init__()
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)