class numeros():
    def __init__(self, numeros):
        self.__numeros = numeros  

    def fraccion(self):
        numero = ''

        if(self.__numeros.count('.') > 0):
            numero = self.__numeros
        else:
            numero = self.__numeros+'.0'
        inicio  = numero.find('.')
        limite = len(numero)
        fraccion = ''
        for i in range(inicio, limite):
            fraccion = fraccion + numero[i]
            
        return fraccion



    def numeros_decimales(self):

        numero = self.__numeros
        decimal = ''
        if(numero.count('.')== 1):
            li = numero.find('.')
            for i in range(0,li): 
                decimal = decimal+numero[i]
            return decimal
        else:
            decimal = numero
            return decimal
            

    def simbolo(self):
        simbolo =''
        if(self.__numeros[0] != '-'):
            simbolo = '0'
            return simbolo
        else:
            simbolo = '1'
            return simbolo

    def mantisa(self, numero):
        inicio  = numero.find('.')
        limite = 25
        mantisas = ''
        for i in range(inicio + 1 , limite):
            mantisas = mantisas + numero[i]
        return mantisas

            






