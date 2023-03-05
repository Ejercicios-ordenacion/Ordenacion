tabla = [18, 13, 9, 10, 16]
elemnto1 = tabla[0]
def desplazar(tabla):
    i = 0
    while i < len(tabla)-1:
        tabla[i] = tabla[i+1]
        i += 1
    tabla[-1] = elemnto1
    return tabla

print(desplazar(tabla))
