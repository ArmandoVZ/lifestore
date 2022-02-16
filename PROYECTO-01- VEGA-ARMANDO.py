from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products
from login import *
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


elegirOperacion = True
while elegirOperacion is True:
    

# Menu del sistema
    clearConsole()
    print (usuario + " ¿Que deseas hacer el dia de hoy? \n")
    Menu = ["Productos más vendidos y productos rezagados","Productos por reseña en el servicio","Total de ingresos"]

    #Imprime el Menu y determina el camino que el usuario desea
    contadorOpciones = 1
    for opcionesMenu in Menu:
        print (str (contadorOpciones) + ") "  + opcionesMenu + "\n")
        contadorOpciones +=1
    seleccion = int(input("Ingresa el numero de la opcion deseada:  "))
    time.sleep(2)

#Valida que la opcion deseada este dentro del rango
    if seleccion >= 1 and seleccion <= len(Menu):
        print("Comencemos \n")
        if seleccion ==1:
            #Generar un listado de los "n" productos con mayores ventas y uno con
            #los 100 productos con mayor búsquedas.
            #Por categoría, generar un listado con los 50 productos con menores
            #ventas y uno con los 100 productos con menores búsquedas.
            print ("Selecciono " + (Menu[0]))
            print ("Ejecutando")
            time.sleep(2)
            cicloInterno = True
            while cicloInterno is True:
                print ("Que desea ver primero :\n 1) Productos mas vendidos \n 2) Productos mas buscados")
                print (" 3) Productos menos vendidos \n 4) Productos menos buscados")
                menuInterno = int(input())
                clearConsole()
                if menuInterno == 1:
                    exec(open("Codigo\mostsold.py").read())
                    print ("Desea observar alguna otra de las opciones anteriormente citadas: Si/No")
                    evaluacionInterna = str (input())
                    if evaluacionInterna == "Si" or evaluacionInterna == "si" or evaluacionInterna == "s" or evaluacionInterna =="S":
                        cicloInterno = True
                        clearConsole()
                    else:
                        cicloInterno = False
                        clearConsole()
                elif menuInterno == 2:
                    clearConsole()
                    exec(open("Codigo\mostsearchproducts.py").read())
                    print ("Desea observar alguna otra de las opciones anteriormente citadas: Si/No")
                    evaluacionInterna = str (input())
                    if evaluacionInterna == "Si" or evaluacionInterna == "si" or evaluacionInterna == "s" or evaluacionInterna =="S":
                        cicloInterno = True
                        clearConsole()
                    else:
                        clearConsole()
                        cicloInterno = False
                elif menuInterno == 3:
                    clearConsole()
                    exec(open("Codigo\leastsoldproducts.py").read())
                    print ("Desea observar alguna otra de las opciones anteriormente citadas: Si/No")
                    evaluacionInterna = str (input())
                    if evaluacionInterna == "Si" or evaluacionInterna == "si" or evaluacionInterna == "s" or evaluacionInterna =="S":
                        cicloInterno = True
                        clearConsole()
                    else:
                        clearConsole()
                        cicloInterno = False
                elif menuInterno == 4:
                    clearConsole()
                    exec(open("Codigo\leastsearchproducts.py").read())
                    print ("Desea observar alguna otra de las opciones anteriormente citadas: Si/No")
                    evaluacionInterna = str (input())
                    if evaluacionInterna == "Si" or evaluacionInterna == "si" or evaluacionInterna == "s" or evaluacionInterna =="S":
                        cicloInterno = True
                        clearConsole()
                    else:
                        clearConsole()
                        cicloInterno = False
                else:
                    print ("La opcion ingresada esta fuera del rango, verifique su respuesta")
                    cicloInterno = True
            print("Desea ejecutar alguna otra operación: Si/No")
            ciclo = input()
            if ciclo == "Si" or ciclo == "si" or ciclo == "s" or ciclo =="S":
                elegirOperacion = True
                clearConsole()
            else: 
                elegirOperacion = False
                clearConsole()
        elif seleccion ==2:
            #Mostrar dos listados de 20 productos cada una, un listado para
            #productos con las mejores reseñas y otro para las peores, considerando
            #los productos con devolución
            print ("Selecciono " + (Menu[1]))
            print ("Ejecutando")
            time.sleep(2)
            cicloInterno = True
            while cicloInterno is True:
                print ("Que desea ver primero :\n 1) Productos con mejores reseñas")
                print (" 2) Productos con peores reseñas \n")
                menuInterno = int(input())
                if menuInterno == 1:
                    clearConsole()
                    exec(open("Codigo/bestreviews.py").read())
                    print ("Desea observar alguna otra de las opciones anteriormente citadas: Si/No")
                    evaluacionInterna = str (input())
                    if evaluacionInterna == "Si" or evaluacionInterna == "si" or evaluacionInterna == "s" or evaluacionInterna =="S":
                        cicloInterno = True
                        clearConsole()
                    else:
                        cicloInterno = False
                        clearConsole()
                elif menuInterno == 2:
                    clearConsole()
                    exec(open("Codigo\worstreview.py").read())
                    print ("Desea observar alguna otra de las opciones anteriormente citadas: Si/No")
                    evaluacionInterna = str (input())
                    if evaluacionInterna == "Si" or evaluacionInterna == "si" or evaluacionInterna == "s" or evaluacionInterna =="S":
                        cicloInterno = True
                        clearConsole()
                    else:
                        cicloInterno = False
                        clearConsole()
                else:
                    print ("La opcion ingresada esta fuera del rango, verifique su respuesta")
                    cicloInterno = True
            print("Desea ejecutar alguna otra operación: Si/No")
            ciclo = input()
            if ciclo == "Si" or ciclo == "si" or ciclo == "s" or ciclo =="S":
                elegirOperacion = True
                clearConsole()
            else: 
                elegirOperacion = False
                clearConsole()
        elif seleccion ==3:
            print ("Selecciono " + (Menu[2]))
            print ("Ejecutando")
            time.sleep(2)
            cicloInterno = True
            while cicloInterno is True:
                print ("Que desea ver primero :\n 1) Meses con mas ventas \n 2) Meses con mas ganancias")
                print (" 3) Meses con mayores porcentajes \n 4) Total de ganancias")
                menuInterno = int(input())
                if menuInterno == 1:
                    clearConsole()
                    exec(open("Codigo\salespermoth.py").read())
                    print ("Desea observar alguna otra de las opciones anteriormente citadas: Si/No")
                    evaluacionInterna = str (input())
                    if evaluacionInterna == "Si" or evaluacionInterna == "si" or evaluacionInterna == "s" or evaluacionInterna =="S":
                        cicloInterno = True
                        clearConsole()
                    else:
                        cicloInterno = False
                        clearConsole()
                elif menuInterno == 2:
                    clearConsole()
                    exec(open("Codigo\profitpermonth.py").read())
                    print ("Desea observar alguna otra de las opciones anteriormente citadas: Si/No")
                    evaluacionInterna = str (input())
                    if evaluacionInterna == "Si" or evaluacionInterna == "si" or evaluacionInterna == "s" or evaluacionInterna =="S":
                        cicloInterno = True
                        clearConsole()
                    else:
                        cicloInterno = False
                        clearConsole()
                elif menuInterno == 3:
                    clearConsole()
                    exec(open("Codigo/averagepermonth.py").read())
                    print ("Desea observar alguna otra de las opciones anteriormente citadas: Si/No")
                    evaluacionInterna = str (input())
                    if evaluacionInterna == "Si" or evaluacionInterna == "si" or evaluacionInterna == "s" or evaluacionInterna =="S":
                        cicloInterno = True
                        clearConsole()
                    else:
                        cicloInterno = False
                        clearConsole()
                elif menuInterno == 4:
                    clearConsole()
                    exec(open("Codigo/totalprofit.py").read())
                    print ("Desea observar alguna otra de las opciones anteriormente citadas: Si/No")
                    evaluacionInterna = str (input())
                    if evaluacionInterna == "Si" or evaluacionInterna == "si" or evaluacionInterna == "s" or evaluacionInterna =="S":
                        cicloInterno = True
                        clearConsole()
                    else:
                        cicloInterno = False
                        clearConsole()
                else:
                    print ("La opcion ingresada esta fuera del rango, verifique su respuesta")
                    cicloInterno = True
            print("Desea ejecutar alguna otra operación: Si/No")
            ciclo = input()
            if ciclo == "Si" or ciclo == "si" or ciclo == "s" or ciclo =="S":
                elegirOperacion = True
                clearConsole()
            else: 
                elegirOperacion = False
                clearConsole()

print ("Saliendo del sistema")
time.sleep(3)

