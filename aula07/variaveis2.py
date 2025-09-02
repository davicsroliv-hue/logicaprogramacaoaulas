import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

usuarios = []
idade= []

def criar_conta():
    usuario = {}
    usuario['nome'] = input('digite seu nome: ').strip()
    usuario['idade'] = input('digite sua idade: ') 
    usuario['email'] = input('Digite seu email: ').strip().lower()
    usuario['cpf'] = input('Digite seu CPF: ')
    usuario['saldo'] = 0.0
    usuarios.append(usuario)
    limpar()
    print('Conta criada com sucesso!')                                           
def exibir_contas():
    if not usuarios:
        print('Nenhuma conta cadastrada.')
    else:
        for i, usuario in enumerate(usuarios, start=1):
            print(f"\n Conta {i} ")
            print(f'Nome: {usuario['nome']}')
            print(f'Idade: {usuario['idade']}')
            print(f'Email: {usuario['email']}')
            print(f'CPF: {usuario['cpf']}')
            print(f'Saldo: R$ {usuario['saldo']:.2f}')

def depositar():
    if not usuarios:
        print('sua conta não foi cadastra ')
        return
    cpf = input('Digite o CPF da conta para depositar sua grana: ')
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            valor = float(input('Digite o valor do depósito: '))
            usuario['saldo'] += valor
            print(f'Depósito realizado! Saldo atual: R$ {usuario['saldo']:.2f}')
            return
    print('Conta não encontrada.')

def sacar():
    if not usuarios:
        print('Nenhuma conta cadastrada.')
        return
    cpf = input('Digite o CPF da conta para saque: ')
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            valor = float(input('Digite o valor do saque: '))
            if valor > usuario['saldo']:
                print('Saldo insuficiente!')
            else:
                usuario['saldo'] -= valor
                print(f'Saque realizado! Saldo atual: R$ {usuario['saldo']:.2f}')
            return
    print('Conta não encontrada.')

def encerrar_conta():
    if not usuarios:
        print('Nenhuma conta cadastrada.')
        return
    cpf = input('Digite o CPF da conta a encerrar: ')
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)
            print('Conta encerrada com sucesso.')
            return
    print('Conta não encontrada.')

while True:
    print('1 - Criar conta')
    print('2 - Exibir dados da conta')
    print('3 - Depositar valor')
    print('4 - Sacar valor')
    print('5 - Encerrar conta')
    print('6 - Sair do programa')

    opcao = input('Informe a opção desejada: ')
    limpar()

    match opcao:
        case '1':
            criar_conta()
        case '2':
            exibir_contas()
        case '3':
            depositar()
        case '4':
            sacar()
        case '5':
            encerrar_conta()
        case '6':
            print('Saindo do sistema!')
            break
        case _:
            print('Opção inválida! Tente novamente.') 


            