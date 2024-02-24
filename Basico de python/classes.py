#Usar classes para criar um conjunto de de ações de algo

class tabuada:
    def __init__(self,numero):
        self.numero = numero
        for n in range(1,10,1):
            print(f"{numero} x {n} = {numero*n}")

tabuada(int(input("digite um numero ")))
tabuada(int(input("digite segundo numero ")))