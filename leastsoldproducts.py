
from lifestore_file import * 
import time 

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

timesold = Sort(timesold) # Ordenamos de manera ascendente

categories= []
processors = []; gpus = []; motherboards = []; drives = []; usb = []; screens = []; speakers = []; headphones = []

categories= [item[-2] for item in lifestore_products]

categories = list(dict.fromkeys(categories))

for item in timesold:
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
print("\n Procesadores con menos ventas")
for i in range(5):
    print(f"ID: {processors[i][0]}\t NAME: {processors[i][1]}\t TIMES SOLD: {processors[i][-1]}")

time.sleep (2)
print("\n GPU con menos ventas")
for i in range(5):
    print(f"ID: {gpus[i][0]}\t NAME: {gpus[i][1]}\t TIMES SOLD: {gpus[i][-1]}")

time.sleep (2)
print("\n MotherBoards con menos ventas")
for i in range(5):
    print(f"ID: {motherboards[i][0]}\t NAME: {motherboards[i][1]}\t TIMES SOLD: {motherboards[i][-1]}")

time.sleep (2)
print("\n Dives con menos ventas")
for i in range(5):
    print(f"ID: {drives[i][0]}\t NAME: {drives[i][1]}\t TIMES SOLD: {drives[i][-1]}")

time.sleep (2)
print("\n USB con menos ventas")
for i in range(2):
    print(f"ID: {usb[i][0]}\t NAME: {usb[i][1]}\t TIMES SOLD: {usb[i][-1]}")

time.sleep (2)
print("\n Pantallas con menos ventas")
for i in range(5):
    print(f"ID: {screens[i][0]}\t NAME: {screens[i][1]}\t TIMES SOLD: {screens[i][-1]}")

time.sleep (2)
print("\n Altavoces con menos ventas")
for i in range(5):
    print(f"ID: {speakers[i][0]}\t NAME: {speakers[i][1]}\t TIMES SOLD: {speakers[i][-1]}")

time.sleep (2)
print("\n Audifonos con menos ventas")
for i in range(5):
    print(f"ID: {headphones[i][0]}\t NAME: {headphones[i][1]}\t TIMES SOLD: {headphones[i][-1]}")