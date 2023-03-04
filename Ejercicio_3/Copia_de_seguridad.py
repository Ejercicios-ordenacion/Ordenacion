tabla = [18, 13, 9, 10, 16]

def copia(tabla):
    maxcount = tabla[0]
    for value in tabla[1:]:
        if value > maxcount:
            maxcount = value
    return maxcount

print(copia(tabla))
