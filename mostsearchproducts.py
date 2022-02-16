from lifestore_file import *


searchedproduct = []; timesearched = []

searchedproduct = [search[1] for search in lifestore_searches]

for search in lifestore_products: # Creacion de lista nested
    nested=[]
    timesearched.append(nested)
    for k in range(1):
        nested.append(search[0]) # Obtenemos el ID
        nested.append(search[1]) # Obtenemos el nombre del producto
        nested.append(searchedproduct.count(search[0])) # Contamos cuantas veces se busco
        nested.append(search[-2]) # Guardamos la categoria
        
def Sort(timesearched):
    timesearched.sort(key = lambda x: x[2])
    return timesearched

timesearched = Sort(timesearched) # Ordenamos de manera ascendente


countList = -1
list50products =[]
limiteLista = int(input ("Cuantos de 'Los productos mas buscados' deseas listar:  "))
print("\n Productos mas buscados")
while countList <= -1 and countList>= -limiteLista:
  list50products.append(countList) 
  countList -= 1
for i in list50products:
    print( F'ID: {timesearched[i][0]}\t NAME: {timesearched[i][1]}\t SEARCHES: {timesearched[i][-2]}' )