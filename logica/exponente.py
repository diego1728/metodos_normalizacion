from logica.remover import remover_caracter
class exponente():
    def __init__(self, numero):
        self.__numero = numero
        
    def mover_punto(self):
        p= self.__numero[0]
        nuevo = remover_caracter(self.__numero, 0)
        notacion = p + '.' + nuevo
        return notacion

    def exponent(self):
        nuevo = remover_caracter(self.__numero, 0)
        expon = len(nuevo)
        return  expon
    


