# adición
print(5+2)

# sustracción
print(5-2)

# multiplicación
print(5*3)

# división
print(10/2)

#------------------------------- TIPOS DE DATOS -------------------------------------

# entero(int)
x=20

# flotante(float)
z=3.1416

# cadena(string == str)
y="hola mundo" 
a='hola planeta'

# booleano(bool)
b=True
c=False

#----------------------------SUMA DE NUMEROS Y CADENAS-----------------------------------

# suma de numeros
2+3

#suma de cadenas
'ab' + 'cd'
("hola"*2) #multiplica la cadena (hola hola)

#---------------------------------------------

# crear variable savings
savings=100
# crea la variable growth_multiplier
growth_multiplier=1.1
# calcular resultado
result=savings*growth_multiplier**7 # '**' es esponente
# imprime resultado
print(result)

#----------------------------LISTAS-----------------------------------------------------

# variables de area (en metros cuadrados)
hall=11.25
kit=18.0
liv=20.0
bed=10.75
bath=9.50
# crea la lista areas
areas=["hallway",hall,"kitchen",kit,"living room",liv,"bedroom",bed,"bathroom",bath]
#  imprimir las areas
print(areas)
# informacion de la casa con lista de listas
house=[["hallway", hall],
       ["kitchen", kit], 
       ["living room", liv], 
       ["bedroom", bed], 
       ["bathroom", bath]]
# imprime house
print(house)
# imprime el tipo de dato de house
print(type(house))

#  ACEDER A LOS DATOS DE UNA LISTA

# imprime el segundo elemento de areas
print(areas[1]) # numeros positivos se cuentan de izquierda a derecha, y los vectores en python empiezan de 0
# imprime el ultimo elemento de areas
print(areas[-1]) # numeros negativos se cuentan de derecha a izquierda
# operaciones con los elementos del vector
eat_sleep_area=areas[3]+areas[7]
print(eat_sleep_area)

# SUBDIVISIÓN DE LISTAS
# lista[begin:end] === se incluira el indice inicio, miestras que el indice fin no será incluido

# subdivide areas para crear otra lista
dowstairs=areas[0:6] # se muestra los primeros 6 elementos
upstairs=areas[6:10] # se muestra los ultimos elementos desde el sexto
# imprime dowstairs y upstairs
print(dowstairs)
print(upstairs)

# si no se especifica begin ( sera tomado en cuenta por  defecto como 0 ) y end ( sera tomado como el final de la lista)

# subdivide areas  en dos partes con un solo indice
dowstairs=areas[:6] # se muestra los primeros 6 elementos
upstairs=areas[6:] # se muestra los ultimos elementos desde el sexto

# SUBDIVISIÓN DE LISTA DE LISTAS

# acceder a las listas de la lista house
x=house[2][0] # accede a la lista dos de hause y al elemento 0 de  esa lista
y=house[2][1] # accede a la lista dos de hause y al elemento 1 de  esa lista
print(x)
print(house[-1][1])

# MODIFICAR ELEMENTOS DE UNA LISTA (VECTOR)

# cambia el area de bathroom
areas[9]=10.50
# cambia "living room" a "chill zone"
areas[4]="Chill Zone"
print(areas)

# EXTENDER UNA LISTA

# agrega mas habitaciones a la casa
# se crea una nueva lista  con las areas originales y las nuevas habitaciones
areas_1=areas + ["poolhouse", 24.5] 
areas_2=areas_1 + ["garage", 15.45]
print(areas_2)

# ELIMINAR ELEMENTOS DE UNA LISTA

del(areas_2[-4:-2])
print(areas_2)

# hacer copia explicita de una lista para que no afecte al original
areas_copy= areas[:]  # para crear una copia explicita de usa " list(areas) o areas[:]"
# modificar areas copy
areas_copy[0]=5.0
#imprime  ambas listas, veras que areas sigue siendo igual porque es una copia de areas
print("funcionamiento interno de la lista")
print(areas)
print(areas_copy)

#-------------------FUNCIONES (FUNCTIONS)----------------------------------------------------------

# una función es como una caja de herramientas que puedes usar para realizar tareas específicas
# usamos las funciones  para: organizar el código, reutilizarlo, simplificarlo y hacerlo más legible
# python nos ofrece funciones como: type(), print(), len( ) , max() entre otras
print("FUNCIONES")

# crea las variables var1 y var2
var1=[1,2,3,4]
var2=True
# Imprime el tipo de var1
print(type(var1))
# imprime la longitud de var1
print(len(var1))
# convierte var2 a un entero: var2
out2=int(var2)

# para tener informacion sobre una funcinon  podemos utilizar la palabra reservada help()
help(len)

# funcion sorted()  ordena los elementos de una lista en base a su valor
# sorted (lista,[key],[reverse]) 
# key : Es una función que se utiliza para determinar la clave por la cual se van a ordenar los elementos
# reverse : indica si queremos que sea ascendente o descendente
first=[11,18,20]
second=[10,9]
full= first + second
# ordena full
ordered=sorted(full, reverse=True)
print(ordered)

#---------------- PROCEDIMIENTOS (PROCEDURE 0R  METHODS) ----------------------------------------

print("PROCEDIMINETOS")
# metodos de cadenas

texto="Hola Mundo"
# usa el metodo upper() y  lower() para pasar todo a mayúsculas o minúsculas
texto1=texto.upper()
texto2=texto.lower()
#imprimir
print(texto)
print(texto1)
print(texto2)
# usar count() para  contar cuantas veces aparece una letra en una cadena
contador=texto.count("o")
print("La letra o aparece ",contador,"Veces")

# metodos de listas

# usaremos los metodos index() y count( ) para buscar un elemento en una lista
nums=[5,3,7,4,6,8,2]
print(nums)
# imprime en indice del elemento 4
indice= nums.index(4)
print ("El numero 4 esta en el  indice",indice)
# cuenta las apariciones de un elemento en una lista
print(nums.count(4)) # imprime 1
# usamos el metodo append( ) para agregar un elemento a una lista
nums.append(1)
# usamos el metodo reverse( ) para invertir una lista
nums.reverse()
print(nums)

#----------------------- PACKAGES AND  MODULES ------------------------------------ 

print("MODULOS O PAQUETES")

# importar paquetes
import math
# llamar funciones de paquetes sin necesidad de indicar la clase
print(math.sqrt(9))  # devuelve la raiz cuadrada de 9 es 3
# importa radians del paquete math
from math import radians
r=123
phi=12
# convertir grados a radianes
rad_phi=radians(phi)
# calcular distancia entre dos puntos en coordenadas polares (x,y)
dist=abs(r*(rad_phi)) # abs  para eliminar signos negativos (valor absoluto)
print("la distancia es: ",dist)

#---------------------------------- NUMPY--------------------------------------------

print( "NUMPY \n")
# numpy es un  modulo que permite trabajar con arrays multidimensionales y numericos
# importa el paquete numpy
import numpy as np
# crea un array
baseball_in=[180,215,210,188,176,209,200]
baseball_lb=[50,30,234,15,432,765,332]
#  convierte la lista a un array numpy
np_baseball_in=np.array(baseball_in)
np_baseball_lb=np.array(baseball_lb)
# imprime el np_baseball
print(np_baseball_in)
print(type(np_baseball_in)) # muestra el tipo de dato del array numpy
print(np_baseball_lb)
# convertir pulgadas a metros
np_baseball_m=np_baseball_in*0.0254
np_baseball_kg=np_baseball_lb*0.453592
# calcular el incremento corporal
inc_corporal=np_baseball_m/np_baseball_m**2
# imprimir los valores de inc_corporal
print ("Incremento Corporal: " ,inc_corporal)
# crea un vector numpy booleano
vbool = inc_corporal  > 0
# imprime el vbool
print("Vectores booleanos:\n",vbool)
# imprime los imc de todos  los jugadores cuyo  IMC sea mayor a 63 kg
print("\nIMC mayores a  63 kg\n" ,inc_corporal[vbool])
# los subconjuntos funcionan igual de los vectores de python  vector==np_vector 

#------------------------------ 2D NUMPY  ARRAYS ----------------------------

# Crea baseball, una lista de listas
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
# Crea una matriz numpy 2D de baseball: np_baseball
np_baseball=np.array(baseball)
# Imprime el tipo de np_baseball
print(type(np_baseball))
# Imprime el atributo shape de np_baseball
print(np_baseball.shape) # shape  es (4, 2), porque tiene  4 filas y 2 columnas     
# Imprime el contenido de np_baseball
print(np_baseball)
# subconjuntos o sublistas

# Imprime la fila 50 de np_baseball
print(np_baseball[3,:])
# Selecciona toda la segunda columna de np_baseball: np_weight_lb
np_weight_lb=np_baseball[:,1]
# Imprime la altura del jugador 2
print(np_baseball[1,0])
# operaciones  con arrays 2d

updated=np.array([[1,2],
                 [2,3],
                 [5,6],
                 [8,3]])
# Imprime la suma de np_baseball y updated
print(np_baseball+updated)
# Crea una matriz numpy: conversion
conversion=np.array([0.0254,0.453592])
# Imprime el producto de np_baseball y conversion
print(np_baseball*conversion)

#------------------ ESTADISTICA  CON NUMPY ------------------------

# Crea np_height_in usando np_baseball
np_height_in=np_baseball[:,0]
# Imprime la media de np_height_in
print(np.mean(np_height_in))
# Imprime la mediana de np_height_in
print(np.median(np_height_in))
# Imprime la desviación estándar de la altura. Reemplaza 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))
# Imprime la correlación entre la primera y la segunda columnas. Reemplaza 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))

positions=["GK","D","H","F"]
heights=[134,234,142,217]
# Convierte positions y heights en matrices numpy: np_positions, np_heights
np_heights=np.array(heights)
np_positions=np.array(positions)
# Alturas de los porteros: gk_heights
gk_heights=np_heights[np_positions=='GK']
# Alturas de los otros jugadores: other_heights
other_heights=np_heights[np_positions!='GK']
# Imprime la altura mediana de los porteros. Reemplaza 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))
# Imprime la altura mediana de los otros jugadores. Reemplaza 'None'
print("Median height of other players: " + str(np.median(other_heights)))