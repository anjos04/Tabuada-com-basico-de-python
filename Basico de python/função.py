#Usar função para dizer oi
def tabuada():
    for n in range(1,10,1):
        nu = 1
        tab = f"{nu} x {n} = {nu * n}"
        print(tab)

tabuada()