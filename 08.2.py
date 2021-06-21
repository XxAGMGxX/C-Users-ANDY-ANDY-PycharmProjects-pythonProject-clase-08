class Condicion:

    def __init__(self,nume1,nume2):
        self.numero1=nume1
        self.numero2=nume2
        numero = self.numero1+self.numero2
        self.numero3=numero

    def Condicion(self):
       if self.numero1 == self.numero2:
        print("numero1:{} y numero2{} son iguales".format(self.numero1,self.numero2))
    if self.numero1 == self.numero3:
        print("numero1:{} es menor numero3:{}".format(self.numero1, self.numero3))
    else:
        print("no son iguales")
    print("fin del metodo")
condi1 = Condicion(5,8)
print(condi1.numero3)
