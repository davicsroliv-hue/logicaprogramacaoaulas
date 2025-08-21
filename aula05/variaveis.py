while True:
   try:
      #entrada de dados
      etanol= float(input('digite o preço do etanol: ').replace(',','.'))
      gasolina=float(input('digite o preço da gasolina: ').replace(',','.'))
      calculo=(etanol/gasolina)*100
      resultado= "gasolina" if calculo > 70 else 'Etanol'

      print(f'resultado= {calculo:.2f}%. compensa abastecer com {resultado}.')

      opcao= input('deseja fazer o calculo? (s/n)').lower().strip()
      match opcao:
         case 's':
            continue
         case 'n':
            break
         case _:
            print(f'opção inválida!')
            continue
   except Exception as e:
    print(f'Não foi possível executar a operação {e}')
    continuegit              
