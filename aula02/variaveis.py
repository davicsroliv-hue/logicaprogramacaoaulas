#aula passada:
#print programação a nivel de console, conseguimos fazer operações
#concatenação 
#declaração de variavel e tipos de variavel
#operadores soma, divisão, mustiplicação, exponenciação
#operadores de comparação
#operadores lógicos
#entrada de dados
#fazer calculadora
#comando: cd- abrir uma pasta, cd ..- volta na pasta anterior
#ls- listar, dir- listar diretório, cls- limpa o terminal

#aula 2:
#concatenação
#quebra de linha
#formatando decimais
#alterando virgula e ponto
#if else
#operador ternario

#FIXME - concatenação com +

nome= "Davi"
idade= 17
altura= 1.91



#saida de dados
print("Olá, meu nome é, " + nome + ", tenho " + str(idade) + " anos de idade")

#FIXME - concatenação com ,
print("Olá, meu nome é,", nome, ", tenho", idade, "anos de vida")

#FIXME - concatenação com format
print("Olá, meu nome é, {} , tenho anos de idade".format(nome,idade))

#FIXME - concatenação com f-string
print(f"Olá, meu nome é {nome} e tenho {idade} anos de idade")

#eliminando quebra de linha
print("O sábio sabia ", end="") #end=""
print("que o sabiá sabia assobiar")



# exibindo o valor com duas casas depois da virgula
valor= 1.23456789
bool= False
print(f"{valor:.2f}")

print(30* "=")
peso= input("digite seu peso: ").replace(",",".")
peso= float(peso)
print(f'{peso:.2f}')

#atividade 
#crie variaveis com os tipos int, float, str e bool e imprima seus valores
print(f'tipo da variavel{nome}: {type(nome)}')
print(f'tipo da variavel{idade}: {type(idade)}')
print(f'tipo da variavel{altura}: {type(altura)}')
print(f'tipo da variavel{bool}: {type(bool)}')

#realize as operações operações 12+7,15% 4,3**2 e verifique os resultados
print(12 + 7)   
print(15 % 4)   
print(3 ** 2)
#crie uma programa que peça nome de usuario e exiba uma mensagem de boas vindas

print() #estrada de dados
print(30*'-','entrada de daos',30*'-')
nome_usuario = input("digite o seu nome: " )



print()
print(30*'-','entrada de dados' ,30*'-')
dados_usuario = input("coloque o seu email: ")
senha_email = input("digite sua senha: ")
print("seja bem vindo ao nosso site", nome_usuario)

#converta uma string "20" para inteiro e somar com um número
vinte= '20'
vinte= int(vinte)
resultado = vinte + 1000
print(resultado)
''''''

# estudar if...else - condição 
#estrutura de decisão
# if idade>= 18:
#print(f'{nome} é maior de idade.')
#else:
nome= input('digite seu nome:')
idade= int(input('digite sua idade: '))

print('Antes do if')
if idade >= 18:
    print('você é maior de idade!')
    print('você esta dentro do bloco if')
else:
    print('você é menor de idade!')
    print('você esta dentro do bloco else')
print('você está fora da estrutura condicionl if else')
''''''

if idade >= 15 and altura >= 1.5:
    print(f'A entrada de {nome} está autorizada.')
else:
    print(f'A entrada de {nome} não está está autoriza.')

#operador ternário 
# em uma unica linha, interface moagle
print(nome, 'é maior de idade.' if idade >= 18 else 'é menor de idade.')
      







