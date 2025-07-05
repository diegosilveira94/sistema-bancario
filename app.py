menu = '''
    [1]DEPOSITAR
    [2]SACAR
    [3]EXTRATO
    [0]SAIR

    DIGITE A OPÇÃO DESEJADA: '''

opcao = 0
saldo = 0
deposito = 0
contador_deposito = 0
saque = 0
contador_saque = 0
lista_deposito = []
lista_saque = []
LIMITE_VALOR_SAQUE = 500
LIMITE_QTD_SAQUE = 3

while True:
    print()
    opcao = int(input(menu))

    # Depositar
    if opcao == 1:
        print()
        deposito = float(input('Digite o valor a ser depositado: '))
        if deposito <= 0 and deposito == str:
            print()
            print('Não é permitido letras ou valores zerados')
        else:
            saldo += deposito
            contador_deposito += 1
            lista_deposito.append(deposito)
            print()
            print(f'Valor de R$ {deposito:.2f} depositado com sucesso!')

    # Sacar
    elif opcao == 2:
        print()
        saque = float(input('Digite o valor a ser sacado: '))
        limite_saque = contador_saque >= LIMITE_QTD_SAQUE
        limite_valor =  saque > LIMITE_VALOR_SAQUE
        print()
        if saque <= 0 and saque == str:
            print()
            print('Não é permitido letras ou valores zerados', end='\n')
        elif saque > saldo:
            print(f'Saldo insuficiente. Seu saldo é de {saldo:.2f}')
        elif limite_valor:
            print(f'Transação não efetuada. Limite de R$ {LIMITE_VALOR_SAQUE} por saque.')
        elif limite_saque:
            print(f'Transação não efetuada. Limite de {LIMITE_QTD_SAQUE} saques diários.')
        else:
            saldo -= saque
            contador_saque += 1
            lista_saque.append(saque)
            print()
            print(f'Valor de R$ {saque:.2f} sacado com sucesso!')
    
    # Extrato
    elif opcao == 3: # Extrato
        # extrato depositos
        print(' EXTRATO ' .center(30, '='))
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

    # Sair
    elif opcao == 0: # Sair
        print('\nEncerrando o programa...')
        break

    # Opção do menu válida
    else:
        print()
        print('Opção inválida. Digite uma das opções.')