#Usando condições para tomar decisões

nome = str(input("qual é o seu nome "))
idade = int(input("qual é a sua idade "))

if idade > 18:
    print(f"SEU NOME É {nome} e tem {idade} anos já é de menor")

else:
   print(f"SEU NOME É {nome} e vocÊ é de menor porque tem {idade} anos")
