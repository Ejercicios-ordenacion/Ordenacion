tabla = [18, 13, 9, 10, 16]
elemnto1 = tabla[0] #primer elemento de la lista
def desplazar(tabla):
    i = 0
    while i < len(tabla)-1:
        tabla[i] = tabla[i+1] #desplaza los elementos de la tabla uno hacia la deracha
        i += 1
    tabla[-1] = elemnto1 #el ultimo elemento de la tabla es igual al primer elemento de esta antes de que se desplazasen para que están todos
    return tabla

print(desplazar(tabla))
