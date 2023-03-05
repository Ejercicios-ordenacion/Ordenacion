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
    # diccionario para ir almacenando
    sucesor = {i: [] for i in range(1, n+1)}
    