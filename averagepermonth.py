from profitoperations import *

def Sort(salesxmonth): # Ordenar de manera ascendente
    salesxmonth.sort(key = lambda x: x[-1])
    return salesxmonth
salesxmonth = Sort(salesxmonth)

controlRango = True 
while controlRango is True: # Control para la validacion de la entrada
    countList = -1
    list50products =[]
    limiteLista = int(input ("Cuantos MESES deseas listar:  "))
    if limiteLista <=12: #Validacion para que el valor ingresado por el usuario
        while countList <= -1 and countList>= -limiteLista:
            list50products.append(countList) 
            countList -= 1
            print("\n MESES CON MAYORES PORCENTAJES")
            for i in list50products:
                print( F'MES: {salesxmonth[i][0]}\t GANANCIA: {"${:,.2f}".format(salesxmonth[i][1])}\t VENTAS: {salesxmonth[i][2]}\t PROMEDIO: {salesxmonth[i][-1]}' )
                controlRango = False
    else:
        print ("El numero ingresado esta fuera del rango, verifique su respuesta")
        controlRango = True