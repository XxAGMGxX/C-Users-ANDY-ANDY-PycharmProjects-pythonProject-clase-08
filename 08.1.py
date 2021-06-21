    class Sintaxis:
        def __init__(self,datos="instancia de la clase"):
            self.frase=datos

        def usoVariables(self):
                edad, __peso = 19, 50.5
                nombres = "Andy Mendoza"
                Tipo_sexo = "M"
                civil = True
                #print("civil={} y su tipo es:{}".format(civil,type(civil)))
                usuario=()
                usuario = ("XxAGMGxX", "0511", "soyproo@gmail.com",True)
                x = usuario[0]
                materias = ["Matematicas", "LENGUAJE", "CCNN", "Programacion"]
                materias[1]="Programacion"
                materias.append("Go")
                estudiante={}
                estudiante = {"nombre": "Andy", "edad": 19, "fac": "faci"}
                estudiante["edad"]=20
                estudiante[cargo]="estudiante"
                y=estudiante["cargo"]

                print(x,y)
                print()estudiante,estudiante["nombre"]
        def mostrar(self):
                print("mostrar")
                print(self.frase)

    ejer1 = Sintaxis()
    ejer1.usoVariables()
