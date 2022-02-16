from lifestore_file import *
from datetime import datetime; import calendar

date = [sale[3] for sale in lifestore_sales] # Definicion de lista para almacenar las ventas por fecha
date.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y')) # Uso de Lambda para ordenar las ventas por fecha 

month =calendar.month_name[1:]

refundeditem = []; totalrefunds = 0; averageticket = [] # Declaracion de listas a utilizar
totalsales = 0; monthsales = [0]*12;  monthprofit = [0]*12

soldproduct = [sale[1] for sale in lifestore_sales]

for i in range(0,len(lifestore_sales)):
    if int(lifestore_sales[i][-1]) == 0:                    # Control de devoluciones
        totalsales+=lifestore_products[soldproduct[i]][2]   # Ciclo para el total de productos vendidos
        if "/01/" in date[i]:
            monthprofit[0]+=lifestore_products[soldproduct[i]][2]
            monthsales[0]+=1
        elif "/02/" in date[i]:
            monthprofit[1]+=lifestore_products[soldproduct[i]][2]
            monthsales[1]+=1
        elif "/03/" in date[i]:
            monthprofit[2]+=lifestore_products[soldproduct[i]][2]
            monthsales[2]+=1
        elif "/04/" in date[i]:
            monthprofit[3]+=lifestore_products[soldproduct[i]][2]
            monthsales[3]+=1
        elif "/05/" in date[i]:
            monthprofit[4]+=lifestore_products[soldproduct[i]][2]
            monthsales[4]+=1
        elif "/06/" in date[i]:
            monthprofit[5]+=lifestore_products[soldproduct[i]][2]
            monthsales[5]+=1
        elif "/07/" in date[i]:
            monthprofit[6]+=lifestore_products[soldproduct[i]][2]
            monthsales[6]+=1
        elif "/08/" in date[i]:
            monthprofit[7]+=lifestore_products[soldproduct[i]][2]
            monthsales[7]+=1
        elif "/09/" in date[i]:
            monthprofit[8]+=lifestore_products[soldproduct[i]][2]
            monthsales[8]+=1
        elif "/10/" in date[i]:
            monthsales[9]+=lifestore_products[soldproduct[i]][2]
            monthsales[9]+=1
        elif "/11/" in date[i]:
            monthprofit[10]+=lifestore_products[soldproduct[i]][2]
            monthsales[10]+=1
        elif "/12/" in date[i]:
            monthprofit[11]+=lifestore_products[soldproduct[i]][2]
            monthsales[11]+=1
    else:
        refundeditem.append(soldproduct[i])                 # Manejo de devoluciones
        totalrefunds+=lifestore_products[soldproduct[i]][2] 

for i in range(12): 
    if monthsales[i] > 0:
        averageticket.append(monthprofit[i]/monthsales[i]) # Obtenemos el promedio
    else:
        averageticket.append(0)

salesxmonth = [list(l) for l in zip(month, monthprofit, monthsales, averageticket)]