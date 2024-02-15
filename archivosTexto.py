from io import open

"""
archivo1 = open('archivo.txt', 'a')
archivo1.write('\n Saludo IDGS-801 nuevo')
archivo1.close()
"""

"""
archivo1 = open('archivo.txt', 'r')
print(archivo1.read())
archivo1.seek(3)
print(archivo1.read())
archivo1.close()
"""

archivo1 = open('archivo.txt', 'r')

for datos in archivo1.readlines():
    print(datos.rstrip())
    
## print(archivo1.readlines())

archivo1.close()