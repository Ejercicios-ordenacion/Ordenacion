tabla = [18, 13, 9, 10, 16]
def ordenar(tabla):
    for i in range(len(tabla)):
        for x in range(len(tabla)-1):
            if tabla[x] > tabla[x+1]:
                tabla[x], tabla[x+1] = tabla[x+1], tabla[x]
    return tabla
print(ordenar(tabla))