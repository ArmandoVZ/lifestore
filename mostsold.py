from lifestore_file import * 

soldproduct = []; timesold = []

soldproduct = [sale[1] for sale in lifestore_sales]

for sale in lifestore_products: # Creacion de lista nested
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

timesold = Sort(timesold) # Orden Ascendente

countList = -1
list50products =[]
limiteLista = int(input ("Cuantos de 'Los productos mas vendidos' deseas listar:  "))
print("\n Productos mas vendidos")
while countList <= -1 and countList>= -limiteLista:
  list50products.append(countList) 
  countList -= 1
  
for i in list50products:
    print( F'ID: {timesold[i][0]}\t NAME: {timesold[i][1]}\t SALES: {timesold[i][2]}' )

