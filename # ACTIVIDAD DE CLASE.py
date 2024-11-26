# ACTIVIDAD DE CLASE - MÉTODO BURBUJA
# Nombre y apellidos: Jonatan Muñoz Moreno
# Fecha: 25/11/2024
# Objetivo: Crear una lista de mayor a menor.

# Aquí creo la variable "ord_lista" y le asigno una lista de números.
ord_lista = [3, 1, 4, 1, 5, 9]

# La variable "seguir" indica.
seguir = True
n = len(ord_lista)
resultado = ord_lista

# Función para ejecutar el algoritmo.
def mayor_menor(ord_lista):
    n = len(ord_lista)   # A "n" le indico la longitud de la lista.
    for i in range(n):   # Añado los parámetros de comparación a "i".
        for j in range(i+1, n):   # Añado los parámetros de comparación a "j".
            if ord_lista[j] < ord_lista[j+1]:  # Aquí uso "if" para comparar un carácter con otro.
                resultado = ord_lista[j]
                ord_lista[j] = ord_lista[j+1]
                ord_lista[j+1] = resultado
    return ord_lista   # Aquí le indico que devuelva la lista.

print(f"El resultado es {resultado}")  # Este apartado muestra el resultado por pantalla.
    




