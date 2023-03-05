tabla = [18, 13, 9, 10, 16]

def copia(tabla):
    maxcount = tabla[0] #el primer elemento de la lista es el mayor
    for value in tabla[1:]:
        if value > maxcount:
            maxcount = value #si el valor es mayor que el primer elemento de la lista, este se convierte en el mayor
    return maxcount

print(copia(tabla))

elemnto1 = tabla[0] #primer elemento de la lista
def desplazar(tabla):
    i = 0
    while i < len(tabla)-1:
        tabla[i] = tabla[i+1] #desplaza los elementos de la tabla uno hacia la deracha
        i += 1
    tabla[-1] = elemnto1 #el ultimo elemento de la tabla es igual al primer elemento de esta antes de que se desplazasen para que están todos
    return tabla

print(desplazar(tabla))

def ordenar(tabla):
    for i in range(len(tabla)):
        for x in range(len(tabla)-1):
            if tabla[x] > tabla[x+1]: #compara los valores de las posiciones
                tabla[x], tabla[x+1] = tabla[x+1], tabla[x] #intercambia los valores de las posiciones
    return tabla
print(ordenar(tabla))