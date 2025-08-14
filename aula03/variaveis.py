# revisão
# variaveis  nome= "" idade= 17
#tipo de variavel- print (type(nome)) # tipos de dados variavel
# concatenação 
# input- entrada de dados nome_usuario= input("digite seu nome: ") #pdrão string
#peso= float(input("digite seu nome: ")) replace .replace(',','.').lower())
# input   replace
# if else # if peso>= 50 #verifica se é verdade 
#print ("acima de 50 kilos")
# else afirma se é falso

'''
problema: crie um sistema que calcula o sistema que calcule o indice de massa corporal(inc) do usuario, 
mostre o valor do inc da imc ela , e retorne se o usuarioesta no peso ideal ou se precosa emagrecer ou engordar mais.
ultilize a tabela do imc

inc = peso / (altura x altura)
18,5 ou menos
abaixo do normal

entre 18,5 e 24,9
normal

'''

print(40*",", 'calculador de imc',40*',')


altura = float(input("digite o seu altura: ").replace(',','.'))
peso = float(input(' digite seu peso: ').replace(',','.'))

imc= peso / (altura * altura)
print()
print(f'seu imc é: {imc:.2f}')

if imc <= 18.5:
    print('abaixo do normal')
elif imc <= 24.9:
    print('normal')
elif imc <= 29.9:
    print('sobre peso')
elif imc <= 34.9:
    print('obesidade grau 1')
elif imc <= 39.9:
    print('obesidade grau 2')
else:
    print('obesidade graus 3')

    

''''
 problema 2: um elevador de carga possui capacidade para 200 kg. crie um programa que receba do usuario seu e 
 o peso da carga e verifica se a carga esta autorizada a usar o elevador ou não.
'''

limite= 200

peso_usuario = float(input('digite seu peso: ').replace(',','.'))
peso_carga = float(input('digite o peso da carga: ').replace(',','.'))

if (peso_usuario + peso_carga) >= 200:
    print('não autorizado, ')

else:
    print('autorizado')

# laços de repetição
#while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

#break #pass ele ignora o erro ou ... #while true

while True:
    print(40 * "-", " sistema console ", 40 * "-")
    print("1 - calculadora imc")
    print("2 - maioridade")
    print("3 - calculadora")
    print("4 - dados pessoais")
    print("5 - sair")

    opcao = input("Digite uma opcao: ")

    if opcao == "1":
        pass  # Aqui vai a lógica da calculadora IMC
    elif opcao == "2":
        pass  # Aqui vai a lógica de verificação de maioridade
    elif opcao == "3":
        pass  # Aqui vai a lógica da calculadora comum
    elif opcao == "4":
        pass  # Aqui vai a lógica de dados pessoais
    elif opcao == "5":
        print("Saindo do sistema!")
        break
    else:
        print("Opcao invalida!")
        

#criar o sistema incluindo eses tópicos

#laço for mais utilizado que o while, não existe loop infinito
#for i in range(5):
   #print(i)
   
for i in range(5):
    print(i)
               





    
