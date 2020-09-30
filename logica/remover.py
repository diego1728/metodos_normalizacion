def remover_caracter(s, n):
    inicio = 0
    fin = len(s)
    resultado = s[inicio:n] + s[n+1:fin]
    return resultado