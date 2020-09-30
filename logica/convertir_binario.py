from logica.remover import remover_caracter
class convert():

    def __init__(self, numero, fracion):
        self.__numero = numero
        self.__fracion = fracion
    
    def conver_binario(self):
        nmro=''
       
        if(self.__numero[0]!='-'):
            nmro = self.__numero
        else:
            nmro = remover_caracter(self.__numero, 0)

        decimal = int(nmro)
        binario = ''
        while decimal // 2 != 0:
             binario = str(decimal % 2) + binario
             decimal = decimal // 2
        return str(decimal) + binario
    
    def conver_fra(self):
        
        fraccion = self.__fracion
        base = '0'
        i=1
        binario = ''
        
        while i <= 20:
            agregar_base = base + fraccion
            valor_conve = float(agregar_base)
            nueva_fraccion = valor_conve * 2
            cadena = str(nueva_fraccion)
            cambiar = remover_caracter(cadena, 0)
            fraccion = base + cambiar
           
            i = i+1
            binario = binario + cadena[0]
        return binario

    def compl(self):
        completo = self.conver_binario() +'.'+ self.conver_fra()
        return completo


    def conver_binario_ex(self, exponente):
        numero =  127 - exponente 
        decimal =  numero
        binario = ''
        while decimal // 2 != 0:
             binario = str(decimal % 2) + binario
             decimal = decimal // 2
        return str(decimal) + binario
    
