import os

saldo = 0
contador_deposito = 0
contador_saque = 0
lista_deposito = []
lista_saque = []

LIMITE_VALOR_SAQUE = 500
LIMITE_QTD_SAQUE = 3

def main():
    exibir_titulo()
    exibir_menu()
    escolher_opcao()

def exibir_titulo ():
    print('''
          
██╗░░░██╗░█████╗░██╗░░░██╗  ██████╗░░█████╗░███╗░░██╗██╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔══██╗██╔══██╗████╗░██║██║░██╔╝
░╚████╔╝░██║░░██║██║░░░██║  ██████╦╝███████║██╔██╗██║█████═╝░
░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══██╗██╔══██║██║╚████║██╔═██╗░
░░░██║░░░╚█████╔╝╚██████╔╝  ██████╦╝██║░░██║██║░╚███║██║░╚██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
          ''')

def exibir_menu ():
    print(
    '''
        [1]DEPOSITAR
        [2]SACAR
        [3]EXTRATO
        [0]SAIR
        '''
    ) 

def escolher_opcao():
    global saldo, contador_deposito, contador_saque, LIMITE_VALOR_SAQUE, LIMITE_QTD_SAQUE    
    opcao = int(input('DIGITE A OPÇÃO DESEJADA: '))
    match opcao:
        case 1: # deposito
            exibir_subtitulo(' DEPOSITO ')
            valor = float(input('\nDigite o valor a ser depositado: '))
            depositar(valor)
        case 2:
            exibir_subtitulo(' SAQUE ')
            valor = float(input('\nDigite o valor a ser sacado: '))
            sacar(valor)
            
        case 3:
            extrato()
        case 0:
            sair()
            
def depositar(valor):
    global saldo, contador_deposito, contador_saque, LIMITE_VALOR_SAQUE, LIMITE_QTD_SAQUE
    exibir_subtitulo(' DEPOSITO ')  
    if valor <= 0 or valor == str:
        print()
        print('Valor inválido!')
    else:
        saldo += valor
        contador_deposito += 1
        lista_deposito.append(valor)
        print(f'\nValor de R$ {valor:.2f} depositado com sucesso!\n')
    voltar_menu_principal()

def sacar(valor):
    global saldo, contador_deposito, contador_saque, LIMITE_VALOR_SAQUE, LIMITE_QTD_SAQUE  
    exibir_subtitulo(' SAQUE ')
    limite_saque = contador_saque >= LIMITE_QTD_SAQUE
    limite_valor = valor > LIMITE_VALOR_SAQUE
    print()
    if valor <= 0 or valor == str:
        print()
        print('Não é permitido letras ou valores zerados', end='\n')
    elif valor > saldo:
        print(f'Saldo insuficiente. Seu saldo é de {saldo:.2f}')
    elif limite_valor:
        print(f'Transação não efetuada. Limite de R$ {LIMITE_VALOR_SAQUE} por saque.')
    elif limite_saque:
        print(f'Transação não efetuada. Limite de {LIMITE_QTD_SAQUE} saques diários.')
    else:
        saldo -= valor
        contador_saque += 1
        lista_saque.append(valor)
        print()
        print(f'\nValor de R$ {valor:.2f} sacado com sucesso!\n')
    voltar_menu_principal()

def extrato ():
    global saldo, contador_deposito, contador_saque, LIMITE_VALOR_SAQUE, LIMITE_QTD_SAQUE 
    exibir_subtitulo(' EXTRATO ')
    # extrato depositos
    print('\nDEPOSITOS:')
    for deposito in lista_deposito:
        if contador_deposito == 0:
            print('Nenhum depósito.')
        else: 
            print(f'R$ {deposito:.2f}')
    print('-'*30)
    # extrato saques
    print('\nSAQUES:')
    for saque in lista_saque:
        if contador_saque == 0:
            print('Nenhum saque.')
        else: 
            print(f'R$ {saque:.2f}')
    print('-'*30)        
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('='*30)
    print()
    voltar_menu_principal()

def sair():
    os.system('cls')
    print('\nEncerrando o programa...')

def limpar_tela():
    os.system('cls')

def voltar_menu_principal():
    input('Aperte qualquer tecla para voltar ao menu principal...')
    limpar_tela()
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto.center(30, '='))

if __name__ == '__main__':
    main()