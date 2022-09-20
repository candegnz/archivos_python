# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv
from re import I


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    archivo = open("stock.csv", "r")
    stock = list(csv.DictReader(archivo))
    archivo.close()

    total = 0

    for i in stock:
        col = i
        cant_tornillos = int(col.get("tornillos"))
        total += cant_tornillos
    
    print("La sumatoria del stock de tornillos es", total)



def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    archivo = open("propiedades.csv", "r")
    propiedades = list(csv.DictReader(archivo))
    archivo.close()
    
    amb_2 = 0

    amb_3 = 0

    try:
        for i in propiedades:
            ambiente = int(i.get("ambientes"))

        if ambiente == 2:
            amb_2 += 1

        if ambiente == 3:
            amb_3 += 1
        print("La cantidad de departamentos con 2 ambientes es:", amb_2)
        print("La cantidad de departamentos con 3 ambientes es:", amb_3)

    except:
        print("El departamento", i, "no tiene 2 ni 3 ambientes")


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
