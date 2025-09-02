#python
# html, css, java script, json,react native, type scrip, node, flask, sql, d jango

#funções: reaproveitamento de código, usamos para não termos que ficar reinscrevendo codigo
#não importa a linguagem de programação, o que importa é a função
#facilitar a leitura, otimizar o programa, reutilizar o mesmo codigo
#utilizar um determinado trecho do codigo quando necessario
#podem ser inscritas dentro do mesmo arquivo ou em um arquivo separado
#declara-se usando "def"
#retorno- só pode ter um
#yiel 
#função recursiva- a função que chama a si mesma quando executada
#dificuldade de depuração, possibilidade de loop infinito etc...

#1. crie uma aplicação de banco, onde o usuario se cadastra e cria um conta corrente que começa com saldo de R$ 0,00. O usuario tera as opções: Criar conta, exibir dados da conta, depositar valor, sacar valor, encerrar conta, sair do programa

import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

usuarios = []


while True:
    usuario = {}
    print('1 - Cadastrar novo usuário.')
    print('2 - Exibir dados da conta. ')
    print('3 - Sair do sistema.')

    opcao = input('Informe a opção desejada: ')
    limpar()


    match opcao:
        case '1':
            usuario['nome'] = input('Informe o nome: ').strip()
            usuario['idade'] = input('Informe a idade: ')
            usuario['email'] = input('Digite o email: ').strip().lower()
            usuario['cpf'] = input('digite seu cpf: ')

            usuarios.append(usuario)
            limpar()
            print('Usuário cadastrado com sucesso!')
            continue

        

        case '3':
            print('Saindo do sistema!')
            break

        case _:
            print("Opção inválida! Tente novamente.")
            continue


        