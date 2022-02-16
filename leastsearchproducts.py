from lifestore_file import *
import time




searchedproduct = []; timesearched = []
searchedproduct = [search[1] for search in lifestore_searches]

categories= []
processors = []; gpus = []; motherboards = []; drives = []; usb = []; screens = []; speakers = []; headphones = []

categories= [item[-2] for item in lifestore_products]

categories = list(dict.fromkeys(categories))


for search in lifestore_products: # Creacion de lista nested
    nested=[]
    timesearched.append(nested)
    for k in range(1):
        nested.append(search[0]) # Obtenemos el ID
        nested.append(search[1]) # Obtenemos el nombre del producto
        nested.append(searchedproduct.count(search[0])) # Contamos cuantas veces se busco
        nested.append(search[-2]) # Obtenemos la Categoria
        
def Sort(timesearched):
    timesearched.sort(key = lambda x: x[2])
    return timesearched

timesearched = Sort(timesearched)

for item in timesearched:
    if categories[0] in item:
        processors.append(item[:3])
    elif categories[1] in item:
        gpus.append(item[:3])
    elif categories[2] in item:
        motherboards.append(item[:3])
    elif categories[3] in item:
        drives.append(item[:3])
    elif categories[4] in item:
        usb.append(item[:3])
    elif categories[5] in item:
        screens.append(item[:3])
    elif categories[6] in item:
        speakers.append(item[:3])
    elif categories[7] in item:
        headphones.append(item[:3])

time.sleep (2)
print("\n Procesadores con menos busquedas")
for i in range(9):
    print(f"ID: {processors[i][0]}\t NAME: {processors[i][1]}\t TIMES SEARCHED: {processors[i][-1]}")

time.sleep (2)
print("\n GPU con menos busquedas")
for i in range(10):
    print(f"ID: {gpus[i][0]}\t NAME: {gpus[i][1]}\t TIMES SEARCHED: {gpus[i][2]}")

time.sleep (2)
print("\n Motherboards con menos busquedas")
for i in range(10):
    print(f"ID: {motherboards[i][0]}\t NAME: {motherboards[i][1]}\t TIMES SEARCHED: {motherboards[i][-1]}")

time.sleep (2)
print("\n Dives con menos busquedas")
for i in range(10):
    print(f"ID: {drives[i][0]}\t NAME: {drives[i][1]}\t TIMES SEARCHED: {drives[i][-1]}")

time.sleep (2)
print("\n USB con menos busquedas")
for i in range(2):
    print(f"ID: {usb[i][0]}\t NAME: {usb[i][1]}\t TIMES SEARCHED: {usb[i][-1]}")

time.sleep (2)
print("\n Pantallas con menos busqeudas")
for i in range(10):
    print(f"ID: {screens[i][0]}\t NAME: {screens[i][1]}\t TIMES SEARCHED: {screens[i][-1]}")

time.sleep (2)
print("\n Altavoces con menos busquedas")
for i in range(10):
    print(f"ID: {speakers[i][0]}\t NAME: {speakers[i][1]}\t TIMES SEARCHED: {speakers[i][-1]}")

time.sleep (2)
print("\n Audifonos con menos busquedas")
for i in range(10):
    print(f"ID: {headphones[i][0]}\t NAME: {headphones[i][1]}\t TIMES SEARCHED: {headphones[i][-1]}")
