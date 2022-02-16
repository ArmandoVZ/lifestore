from re import X
from lifestore_file import *

soldproduct = []; timesold = []

soldproduct = [sale[1] for sale in lifestore_sales]

for sale in lifestore_products: # Creamos la lista nested
    nested=[]
    timesold.append(nested)
    for k in range(1):
        nested.append(sale[0])
        nested.append(sale[1])
        nested.append(soldproduct.count(sale[0])) # Contamos cuantas veces se vendio
        nested.append(sale[-2])

def Sort(timesold):
    timesold.sort(key = lambda x: x[2])
    return timesold

timesold = Sort(timesold)

tempsum=0; totalscore = []; averagescore = []



for product in lifestore_products: 
    for review in lifestore_sales:
        if product[0]==review[1]:
            tempsum += review[2] 
    
    totalscore.append(tempsum)
    tempsum=0


for review in timesold: # Creamos lista nested
    nested=[]
    if review[2] > 0: #Obtenemos todas las reviews
        averagescore.append(nested)
        for k in range(1):
            nested.append(review[0])
            nested.append(review[1])
            nested.append(review[2]) 
            nested.append(totalscore[review[0]-1]/review[2]) #Obtenemos el promedio

def Sort(averagescore):
    averagescore.sort(key = lambda x: x[-1])
    return averagescore

averagescore = Sort(averagescore)

limiteLista = int(input ("Cuantos de 'Los productos peor calificados' deseas listar:  "))
print("\n Productos peor calificados")
for i in range(0,limiteLista):
    print( F'ID: {averagescore[i][0]}\t NAME: {averagescore[i][1]}\t SCORE: {averagescore[i][-1]}\t TIMES REVIEWED: {averagescore[i][2]}' )