class Ciclco:
    def __init__(self,num):
        self.numero=num

    def usowhile(self):
        caracter=""
        while caracter not in("a","e","i","o","u"):
            caracter = imput("ingrese voval: ").lower()
            print("felicitaciones el caracter:{} es una vcal".format(caracter))

ciclo1 = ciclo()
ciclo.usowhile()