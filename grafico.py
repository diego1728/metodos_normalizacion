from tkinter import *
from tkinter import ttk
from logica.numero import numeros
from logica.convertir_binario import convert
from logica.exponente import exponente



ventana = Tk()
ventana.config(bg = 'white')

frame = Frame(ventana)
frame.grid(row = 0, column = 0, padx = 40, pady = 50)
frame.config(bg ='white')
labenumero = Label(frame, text ='INGRESE EL NUMERO')
labenumero.grid(row =0, column =0, padx = 20, pady=10, columnspan= 3)
labenumero.config(bg='white')
inp_numero = Entry(frame)
inp_numero.grid(row =1, column = 0, padx =70, pady = 10, columnspan= 3)
resultados = Label(frame)
resultados.grid(row =5, column = 0, padx =20, pady = 100, columnspan =3)
resultados.config(bg='white')
signo = LabelFrame(resultados, text ='Signo')
signo.grid(row =0, column = 0, padx =20, pady = 2, ipadx=9)
signo.config(bg = "white")
exponentef = LabelFrame(resultados, text ='Exponente')
exponentef.grid(row =0, column = 1, padx =20, pady = 2)
exponentef.config(bg = "white")
mantisaf = LabelFrame(resultados, text ='Mantisas')
mantisaf.grid(row =0, column = 2, padx =3, pady = 2, ipadx =1)
mantisaf.config(bg = "white")
panel = Frame(frame)
panel.grid(row = 3, column = 0, padx = 20, pady =20,  columnspan =3)
panel.config(bg='white')
labe_numero = Label(panel, text = 'Numero :')
labe_numero.grid(row = 0, column =0, padx =20, pady =3 )
labe_numero.config(bg ='white')

labe_binario = Label(panel, text = 'Binario :')
labe_binario.grid(row = 1, column =0, padx =20, pady =3 )
labe_binario.config(bg ='white')


labe_notacion = Label(panel, text = 'Notacion Cintifica :')
labe_notacion.grid(row = 2, column =0, padx =20, pady =3 )
labe_notacion.config(bg='white')

labe_notacion = Label(panel, text = 'Expoonete :')
labe_notacion.grid(row = 3, column =0, padx =20, pady =3 )
labe_notacion.config(bg ='white')






def calcular():
    if(len(inp_numero.get()) > 0):

        numero = inp_numero.get()
        mn = numeros(numero)
        decimal = mn.numeros_decimales()
        bn = convert(decimal, mn.fraccion())
        binario = bn.conver_binario()
        exp = exponente(binario)
        mantisa =exp.mover_punto()+''+bn.conver_fra()
        notacion = mn.simbolo()+''+exp.mover_punto()+''+bn.conver_fra()
        numro = inp_numero.get()
       
        inp_numero.delete(0, 'end')
        
   
        

        labe_numeror = Label(panel, text = numro)
        labe_numeror.grid(row = 0, column =1, padx =20, pady =3 )
        labe_numeror.config(bg ='white')

        labe_binarior = Label(panel, text =  mn.simbolo() +''+ bn.compl())
        labe_binarior.grid(row = 1, column =1, padx =20, pady =3 )
        labe_binarior.config(bg='white')


        labe_notacionr = Label(panel, text = notacion)
        labe_notacionr.grid(row = 2, column =1, padx =20, pady =3 )
        labe_notacionr.config(bg ='white')

        labe_exponenter = Label(panel, text = '-' + str(exp.exponent()))
        labe_exponenter.grid(row = 3, column =1, padx =20, pady =3 )
        labe_exponenter.config(bg ='white')

       
        labelsigno = Label(signo, text = mn.simbolo())
        labelsigno.grid(row =0, column = 0, padx = 3, pady = 1)
        labelsigno.config(bg='white')
        labelexponente = Label(exponentef, text = bn.conver_binario_ex(exp.exponent()))
        labelexponente.grid(row =0, column = 0, padx = 10, pady = 1)
        labelexponente.config(bg='white')
        labelmantisa = Label(mantisaf, text = mn.mantisa(mantisa))
        labelmantisa.grid(row =0, column = 0, padx = 30, pady = 1)
        labelmantisa.config(bg='white')

        

    else:

        label1 = Label(frame, text = 'ingrese un numero' )
        label1.grid(row = 3 , column = 0 , padx =10, pady=10, columnspan= 3)
        

enviar = Button(frame, text = 'calcular', command =calcular)
enviar.grid(row =2, column = 0, padx =60, pady = 10, ipadx=20, columnspan= 3)

















ventana.mainloop()




