'''''
Ejercicio 2: Ordenación topológica

Una restricción se expresa mediante un par (i,j) de números enteros comprometidos entre 1 y n, que indica que la tarea ti va antes que la tarea tj. Es decir, la tarea ti debe estar
terminada antes de empezar la tarea tj. La relación binaria <<...precede...>> así definida en el conjunto de las n tareas es una relación de orden parcial: algunas tareas no son comparables.
- Hacer un algortimo que calcule una ordenación de las n tareas cumpliendo las restricciones.
Está claro que no se pueden cumplir todas las restricciones. En este caso, no hay ordenación de las tareas. El algortimo deberá tratar este caso corretamente.
-----
Entrada: n tareas y restricciones
Salida: ordenación topológica de las tareas (si es quue es posible encontrar una ordenación)
'''''

def ord_topologica(n, restricciones):
    # diccionario para almacenar sucesores
    sucesores = {i: [] for i in range(1, n+1)}

    # diccionario para  almacenar los predecesores
    predecesores = {i: [] for i in range(1, n+1)}

for i,j in restricciones: # rellenar con los diccionarios los sucesores y predecesores
    sucesores[i].append(j)
    predecesores[j].append(i)

no_predecesores = [n for n in predecesores if not predecsores [n]]  # lista para cuando no hay predecesores

orden = []  # lista vacía para el orden topológico

while no_predecesores:  # mientras no haya predecesores
    n = no_predecesores.pop() # elimina y devuelve el elemneto de la lista
    orden.append(n) # añadirlo al orden topológico
    
