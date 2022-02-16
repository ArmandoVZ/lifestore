from profitoperations import *

def Sort(salesxmonth): # Ordenamos de manera ascendente
    salesxmonth.sort(key = lambda x: x[1])
    return salesxmonth
salesxmonth = Sort(salesxmonth)

controlRango = True
while controlRango is True: 
    countList = -1
    list50products =[]
    limiteLista = int(input ("Cuantos MESES deseas listar:  "))

    if limiteLista <=12:
        while countList <= -1 and countList>= -limiteLista:
            list50products.append(countList) 
            countList -= 1
            print("\n MESES CON MAS GANANCIAS")
            for i in list50products:
                print( F'MES: {salesxmonth[i][0]}\t GANANCIA: {"${:,.2f}".format(salesxmonth[i][1])}\t VENTAS: {salesxmonth[i][2]}\t PROMEDIO: {salesxmonth[i][-1]}' )
                controlRango = False
    else:
        print ("El numero ingresado esta fuera del rango, verifique su respuesta")
        controlRango = True