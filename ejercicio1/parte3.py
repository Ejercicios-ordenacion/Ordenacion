def ordenar_tabla(tabla):
    n = len(tabla)
    ordenado = [None] * n
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if tabla[j] < tabla[minimo]:
                minimo = j
        ordenado[i] = tabla[minimo]
        tabla[minimo] = tabla[i]
    return ordenado
