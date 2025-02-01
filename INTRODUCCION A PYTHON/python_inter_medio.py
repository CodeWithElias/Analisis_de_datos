#----------------- BASIC PLOTS WITH  MATPLOTLIB ----------------

# importar numpy
import numpy as np

#--------------------- GRAFICO  DE LINEA ------------
print("Grafico de Linea") 
# herramienta que se usa para  crear gráficos util para estadistica
año=[1920 ,1922 ,1924 ,1926,1928, 1930 ,1932, 1934 ,1936, 1938 ,1940, 1942 ,1944, 1946 ,1948, 1950 ,1952, 1954,1956 ,1958, 1960 ,1962 ,1964, 1966 ,1968, 1970 ,1972, 1974 ,1976 ,1978 ,1980, 1982,1984 ,1986, 1988, 1990 ,1992, 1994 ,1996, 1998, 2000, 2002 ,2004 ,2006 ,2008, 2010,2012, 2014 ,2016 ,2018 ,2020, 2022 ,2024, 2026 ,2028 ,2030, 2032 ,2034 ,2036, 2038,2040 ,2042, 2043 ,2043 ,2043 ,2043 ,2043, 2043, 2043 ,2043, 2043 ,2043 ,2043, 2043,2043, 2043, 2043 ,2043 ,2043 ,2043 ,2043, 2043, 2043 ,2043 ,2043 ,2043 ,2043, 2043,2043 ,2043, 2043 ,2043 ,2043 ,2043 ,2043, 2043, 2043 ,2043 ,2043 ,2043 ,2043, 2043,2043, 2043 ,2043 ,2043 ,2043 ,2043 ,2043, 2043, 2043 ,2043, 2043 ,2043 ,2043, 2043,2043 ,2043 ,2043 ,2043 ,2043 ,2043 ,2043, 2043, 2043 ,2043, 2043 ,2043 ,2043, 2043,2043 ,2043, 2043 ,2043, 2043 ,2043, 2043, 2043, 2043 ,2043, 2043 ,2043]
year=np.array(año)
pobla=[1.889923, 3.600523, 33.333216, 12.420476, 40.301927, 20.434176, 8.199783, 0.708573, 150.448339, 10.392226, 8.078314, 9.119152, 4.552198, 1.639131, 190.010647, 7.322858, 14.326203, 8.390505, 14.131858, 17.696293, 33.390141, 4.369038, 10.238807, 16.284741, 1318.683096, 44.22755, 0.71096, 64.606759, 3.80061, 4.133884, 18.013409, 4.493312, 11.416987, 10.228744, 5.46812, 0.496374, 9.319622, 13.75568, 80.264543, 6.939688, 0.551201, 4.906585, 76.511887, 5.23846, 61.083916, 1.454867, 1.688359, 82.400996, 22.873338, 10.70629, 12.572928, 9.947814, 1.472041, 8.502814, 7.483763, 6.980412, 9.956108, 0.301931, 1110.396331, 223.547, 69.45357, 27.499638, 4.109086, 6.426679, 58.147733, 2.780132, 127.467972, 6.053193, 35.610177, 23.301725, 49.04479, 2.505559, 3.921278, 2.012649, 3.193942, 6.036914, 19.167654, 13.327079, 24.821286, 12.031795, 3.270065, 1.250882, 108.700891, 2.874127, 0.684736, 33.757175, 19.951656, 47.76198, 2.05508, 28.90179, 16.570613, 4.115771, 5.675356, 12.894865, 135.031164, 4.627926, 3.204897, 169.270617, 3.242173, 6.667147, 28.674757, 91.077287, 38.518241, 10.642836, 3.942491, 0.798094, 22.276056, 8.860588, 0.199579, 27.601038, 12.267493, 10.150265, 6.144562, 4.553009, 5.447502, 2.009245, 9.118773, 43.997828, 40.448191, 20.378239, 42.292929, 1.133066, 9.031088, 7.554661, 19.314747, 23.174294, 38.13964, 65.068149, 5.701579, 1.056608, 10.276158, 71.158647, 29.170398, 60.776238, 301.139947, 3.447496, 26.084662, 85.262356, 4.018332, 22.211743, 11.746035, 12.311143]
pop=np.array(pobla)
# Imprime el la última fila de year y pop
print(max(year)) # max devuelve  el valor mas grande en una lista o array
print(max(pop))
# Importa matplotlib.pyplot como plt
import matplotlib.pyplot as plt
# Haz un gráfico de líneas: año en el eje x, pop en el eje y
plt.plot(year,pop)
# Muestra el gráfico con plt.show()
#plt.show()
#-----------------------------------------------------------------------------------------------------
gdp_cap=np.array([974.5803384, 5937.029525999999, 6223.367465, 4797.231267, 12779.37964, 34435.367439999995, 36126.4927, 29796.04834, 1391.253792, 33692.60508, 1441.284873, 3822.137084, 7446.298803, 12569.85177, 9065.800825, 10680.79282, 1217.032994, 430.0706916, 1713.778686, 2042.09524, 36319.23501, 706.016537, 1704.063724, 13171.63885, 4959.114854, 7006.580419, 986.1478792, 277.5518587, 3632.557798, 9645.06142, 1544.750112, 14619.222719999998, 8948.102923, 22833.30851, 35278.41874, 2082.4815670000003, 6025.374752000001, 6873.262326000001, 5581.180998, 5728.353514, 12154.08975, 641.3695236000001, 690.8055759, 33207.0844, 30470.0167, 13206.48452, 752.7497265, 32170.37442, 1327.60891, 27538.41188, 5186.050003, 942.6542111, 579.2317429999999, 1201.637154, 3548.3308460000003, 39724.97867, 18008.94444, 36180.78919, 2452.210407, 3540.651564, 11605.71449, 4471.061906, 40675.99635, 25523.2771, 28569.7197, 7320.880262000001, 31656.06806, 4519.461171, 1463.249282, 1593.06548, 23348.139730000003, 47306.98978, 10461.05868, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 12451.6558, 1042.581557, 1803.151496, 10956.99112, 11977.57496, 3095.7722710000003, 9253.896111, 3820.17523, 823.6856205, 944.0, 4811.060429, 1091.359778, 36797.93332, 25185.00911, 2749.320965, 619.6768923999999, 2013.977305, 49357.19017, 22316.19287, 2605.94758, 9809.185636, 4172.838464, 7408.905561, 3190.481016, 15389.924680000002, 20509.64777, 19328.70901, 7670.122558, 10808.47561, 863.0884639000001, 1598.435089, 21654.83194, 1712.472136, 9786.534714, 862.5407561000001, 47143.17964, 18678.31435, 25768.25759, 926.1410683, 9269.657808, 28821.0637, 3970.095407, 2602.394995, 4513.480643, 33859.74835, 37506.41907, 4184.548089, 28718.27684, 1107.482182, 7458.396326999999, 882.9699437999999, 18008.50924, 7092.923025, 8458.276384, 1056.380121, 33203.26128, 42951.65309, 10611.46299, 11415.80569, 2441.576404, 3025.349798, 2280.769906, 1271.211593, 469.70929810000007])
life_exp=np.array([43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 50.43, 80.653, 44.74100000000001, 50.651, 78.553, 72.961, 72.889, 65.152, 46.462, 55.322, 78.782, 48.328, 75.748, 78.273, 76.486, 78.332, 54.791, 72.235, 74.994, 71.33800000000001, 71.878, 51.57899999999999, 58.04, 52.947, 79.313, 80.657, 56.735, 59.448, 79.406, 60.022, 79.483, 70.259, 56.007, 46.388000000000005, 60.916, 70.19800000000001, 82.208, 73.33800000000001, 81.757, 64.69800000000001, 70.65, 70.964, 59.545, 78.885, 80.745, 80.546, 72.567, 82.603, 72.535, 54.11, 67.297, 78.623, 77.58800000000001, 71.993, 42.592, 45.678, 73.952, 59.443000000000005, 48.303, 74.241, 54.467, 64.164, 72.801, 76.195, 66.803, 74.543, 71.164, 42.082, 62.069, 52.906000000000006, 63.785, 79.762, 80.204, 72.899, 56.867, 46.859, 80.196, 75.64, 65.483, 75.53699999999999, 71.752, 71.421, 71.688, 75.563, 78.098, 78.74600000000001, 76.442, 72.476, 46.242, 65.528, 72.777, 63.062, 74.002, 42.568000000000005, 79.972, 74.663, 77.926, 48.159, 49.339, 80.941, 72.396, 58.556, 39.613, 80.884, 81.70100000000001, 74.143, 78.4, 52.517, 70.616, 58.42, 69.819, 73.923, 71.777, 51.542, 79.425, 78.242, 76.384, 73.747, 74.249, 73.422, 62.698, 42.38399999999999, 43.487])
# Imprime el último elemento de gdp_cap y life_exp
print(gdp_cap[-1])
print(life_exp[-1])
# Dibuja un gráfico lineal, gdp_cap en el eje x, life_exp en el eje y
plt.plot(gdp_cap, life_exp)
# Etiquetas y título
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
# Muestra el gráfico
plt.grid(True)
#plt.show()

#---------------------  GRÁFICOS CON DISPERCION --------------------------------- 
print("Gráficos Con Dispersión")
# Cambia el gráfico de líneas de abajo a un gráfico de dispersión
plt.scatter(gdp_cap, life_exp)
# Pon el eje x en una escala logarítmica
plt.xscale('log')
# Enseña la gráfica
#plt.show()

# personalizacion

# Diagrama de dispersión básico, escala logarítmica
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 
# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'
# Añadir etiquetas de eje
plt.ylabel(ylab)
plt.xlabel(xlab)
# Añadir título
plt.title(title)
# Definición de tick_val y tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
# Adaptar los ticks en el eje x
plt.xticks(tick_val,tick_lab)
# Dobla np_pop
pop=pop*2
col=['red', 'green', 'blue', 'blue', 'yellow', 'black', 'green', 'red', 'red', 'green', 'blue', 'yellow', 'green', 'blue', 'yellow', 'green', 'blue', 'blue', 'red', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'red', 'yellow', 'blue', 'blue', 'blue', 'yellow', 'blue', 'green', 'yellow', 'green', 'green', 'blue', 'yellow', 'yellow', 'blue', 'yellow', 'blue', 'blue', 'blue', 'green', 'green', 'blue', 'blue', 'green', 'blue', 'green', 'yellow', 'blue', 'blue', 'yellow', 'yellow', 'red', 'green', 'green', 'red', 'red', 'red', 'red', 'green', 'red', 'green', 'yellow', 'red', 'red', 'blue', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'blue', 'blue', 'yellow', 'red', 'green', 'blue', 'blue', 'red', 'blue', 'red', 'green', 'black', 'yellow', 'blue', 'blue', 'green', 'red', 'red', 'yellow', 'yellow', 'yellow', 'red', 'green', 'green', 'yellow', 'blue', 'green', 'blue', 'blue', 'red', 'blue', 'green', 'blue', 'red', 'green', 'green', 'blue', 'blue', 'green', 'red', 'blue', 'blue', 'green', 'green', 'red', 'red', 'blue', 'red', 'blue', 'yellow', 'blue', 'green', 'blue', 'green', 'yellow', 'yellow', 'yellow', 'red', 'red', 'red', 'blue', 'blue']
# Diagrama de dispersión
plt.scatter(x = gdp_cap, y = life_exp, s = pop, c = col, alpha = 0.8) # "s"  indica el tamaño del marcador; "c" especifica color; "alpha" con puntos coloreados según la población
# Personalizaciones adicionales
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
# Añadir la llamada a grid()
plt.grid(True) # grid  on/off sirve para activar o desactivar las cuadrícul
# Después de personalizar, mostrar la gráfica
#plt.show()

#------------------------ HISTOGRAMAS ----------------------------------------------
print("Histogramas")

# Crea histograma de datos life_exp
plt.hist(life_exp) # bins = 10 como  parámetro por defecto
# Visualiza el histograma
#plt.show()
plt.clf()
# Construye un histograma con 5 bins
plt.hist(life_exp,bins=5)
# Muestra y limpia la gráfica
#plt.show()
plt.clf()
# Construye histograma con 20 rangos
plt.hist(life_exp, bins=20)
# Muestra y limpia de nuevo
#plt.show()
plt.clf() # Limpiar lienzo de dibujo (clear figure)

#---------------------- DICCIONARIES (DICCIONARIOS) -----------------------------------
print("Dictionaries")

# Definición de países y capitales
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
# Obtén el índice de 'germany': ind_ger
ind_ger=countries.index("germany")
# Usa ind_ger para imprimir la capital de Alemania
print(capitals[ind_ger])
# A partir de un string en countries y capitals, crea un diccionario europe
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo', 'australia':'vienna' } 
# los diccionarios sirven  para asociar claves a valores:
# Imprime europe
print(europe)
# Imprime las llaves en europe
print(europe.keys())
# Imprime el valor que pertenece a la clave 'norway'
print(europe['norway'])
# Añade italy a europe
europe['italy']='rome'
# Imprime italy en europe
print('italy' in europe)
# Añade poland a europe
europe['poland']='warsaw'
# Imprime europe
print(europe)
# Cambia la capital de Alemania
europe['germany']='berlin'
# Elimina australia
del(europe['australia'])
# Imprime europe
print(europe)
#----------------------------------------------------------------------------------
# Diccionario de diccionarios
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
# Imprime la capital de Francia
print(europe['france']['capital'])
# Crea los datos del sub-diccionario
data={'capital':'rome', 'population':59.83}
# Añada datos a Europa con la clave 'italy'
europe['italy']=data
# Imprime europe
print(europe)

#------------------------------ PANDAS ---------------------------------------------

# Listas predefinidas
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
# Import pandas as pd
import pandas as pd
# Crea el diccionario my_dict con tres pares clave:valor: my_dict
my_dict={'country':names,'drives_right':dr,'cars_per_cap':cpc}
# Construye un DataFrame cars a partir de my_dict: cars
cars=pd.DataFrame(my_dict)
# Imprime cars
print(cars)
# Definición de row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
# Especifica las etiquetas de las filas de los coches
cars.index=row_labels
# Vuelve a imprimir cars
print(cars)
# Importa el archivo cars.csv data: cars
#cars=pd.read_csv("cars.csv", index_col=0) # es para importar un archivo en formato csv  que se encuentra en el mismo directorio, index_col=0 sirve para indentificar la columna 0 como el indice
# Imprime coches
print(cars)
# Imprime la columna country como Pandas Series
print(cars['country'])
# Imprime la columna country como Pandas DataFrame
print(cars[['country']])
# Imprime DataFrame con las columnas country y drives_right
print(cars[['country', 'drives_right']])
# Imprime las 3 primeras observaciones
print(cars.iloc[[0,1,2]])
# Imprime la cuarta, quinta y sexta observación
print(cars.iloc[[3,4,5]])
# Imprime la observación de Japón
print(cars.iloc[2]) # iloc sirve para  acceder por índices o filas
# Imprime las observaciones de Australia y Egipto
print(cars.loc[['AUS','EG']]) # loc sirve para  buscar por nombre de país
# Imprime el valor drives_right de Marruecos
print(cars.iloc[5],[2])
# Imprime el sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])
#------------------------------------------------------------------------------------------------
# Importa datos de cars
#import pandas as pd
#cars = pd.read_csv('cars.csv', index_col = 0)
# Extrae la columna drives_right como Series: dr
dr=cars["drives_right"]
# Usa dr para crear un subconjunto cars: sel
sel=cars[dr]
# Convierte el código en una sola línea
sel = cars[cars['drives_right']]
# Imprime sel
print(sel)
# Crea car_maniac: observaciones que tengan un cars_per_cap superior a 500
cpc=cars["cars_per_cap"]
many_cars=cpc>500
car_maniac=cars[many_cars]
# Imprime car_maniac
print(car_maniac)

# Crea medium: observaciones con cars_per_cap entre 100 y 500
cpc=cars["cars_per_cap"]
between=np.logical_and(cpc>100, cpc<500) 
medium=cars[between]
# Imprime medium
print(medium)

#------------------ COMPARACIONES ------------------------------------------------

#------ igualdades ------------------------------
# Comparación de valores booleanos
True==False
# Comparación de números enteros
-5*15!=75
# Comparación de strings
"pyscript"=="PyScript"
# Compara un booleano con un entero
True==1

#----mayor que > & menor que  < ----
# Comparación de números enteros
x = -3 * 6
print(x>=-10)
# Comparación de strings
y = "test"
print("test"<=y)
# Comparación de valores booleanos
print(True>False)

#------ comparar matrices  ------------
# Crea matrices
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house mayor o igual a 18 
print(my_house>=18)
# my_house menos que your_house
print(my_house<your_house)

#------------------------- OPERADOERES BOOLEANOS --------------------------------------------
# Definir variables
my_kitchen = 18.0
your_kitchen = 14.0
# ¿my_kitchen más grande que 10 y menor que 18?
print(my_kitchen>10 and my_kitchen<18)
# ¿my_kitchen menor de 14 o mayor de 17?
print(my_kitchen<14 or my_kitchen>17)
# ¿El doble de my_kitchen es más pequeño que el triple de your_kitchen?
print(my_kitchen*2<your_kitchen*3)

#----------------------- OPERADORES BOOLEANOS CON NUMPY --------------------------------------
# Crear matrices
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house mayor de 18.5 o menor de 10
print(np.logical_or(my_house>18.5, my_house<10))
# Tanto my_house como your_house tienen un tamaño inferior a 11
print(np.logical_and(my_house<11 , your_house<11))

#---------------------------- CONDICIONALES  -------------------------------------------
area = 10.0
if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else:
    print("large")
    
# Definir variables
room = "kit"
area = 14.0
# if statement para room
if room == "kit" :
    print("looking around in the kitchen.")
# if statement para area
if area>15:
    print("big place!")
else:
    print("pretty small.")

#-------------------------------- BUCLE WHILE ----------------------------------------------------

# Inicializar offset
offset=8
# Código del bucle while
while offset!=0:
    print("correcting...")
    offset=offset-1
    print(offset)
# Código del bucle while
while offset != 0:
    print("correcting...")
    if offset>0 :
      offset=offset-1
    else :
      offset=offset+1
    print(offset)
    
#------------------- BUCLE FOR -------------------------------------------------------------------

# lista: areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Código para el bucle for
for height in areas:  # height sirve para  iterar en cada elemento de la lista 'areas'
    print(height)
    
# Cambio de bucle para usar enumerate() y actualizar print()
for index, area in enumerate(areas) :
    print("room " + str(index) + ": "+ str(area))
    
# Lista de listas «house»
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]
# Construir un bucle for desde cero
for casas in house:
    x=casas[0]
    y=casas[1]
    print("the "+  x + " is " + str(y)+ " sqm")

#--------------------- BUCLES PARA DICCIONARIOS Y MATRIZ NUMPY ----------------------
#------- BUCLE PARA DICCIONARIOS ------------------------------
# Definición de diccionario
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
# Iterar sobre europe
for x, y in europe.items():
    print("the capital of ", x, " is ", y)
#------ BUCLE PARA  UNA MATRIZ CON NUMPY -----------------------
np_height=np.array(areas)   # Convertir a numpy array
np_baseball=np.array(areas+areas) 
# Loop «for»  sobre np_height 
for x in np_height:
    print(x ,"inches")
# Loop «for»  sobre np_baseball
for x in np.nditer(np_baseball):
    print(x)

#------------------------------------------- BUCLE SOBRE PANDAS (DATAFRAMES) ---------------------------------------------

# Importar datos de «cars»
import pandas as pd
#cars = pd.read_csv('cars.csv', index_col = 0)
# Iterar sobre filas de coches
for lab, row in cars.iterrows():
    print(lab)
    print(row)
# Adapta el bucle for
for lab, row in cars.iterrows() :
    print(lab+": "+str(row["cars_per_cap"]))
# Código para bucle que añade columna COUNTRY
for lab,row in cars.iterrows():
    cars.loc[lab,"COUNTRY"]= row["country"].upper()
# Imprime cars
print(cars)
# otra forma de iterar  en pandas es con apply
# Usa .apply(str.upper)
cars["COUNTRY"]=cars["country"].apply(str.upper)
print(cars)

#------------------------------------------- RANDOM NUMBERS ---------------------------------------------------------------

# Importa numpy como np
# Establece la semilla
np.random.seed(123)
# Genera e imprime flotadores aleatorios
print(np.random.rand())

# Usa randint() para simular un dado
print(np.random.randint(1,7))
# Usa randint() de nuevo
print(np.random.randint(1,7))

#------ juego del dado -----------
# Paso inicial
step = 50
# Tira los dados
dice=np.random.randint(1,7)
# Terminar la construcción de control
if dice <= 2 :
    step = step - 1
elif dice<=5:
    step =step+1
else:
    step = step + np.random.randint(1,7)
# Print out dice and step
print(dice)
print(step)

#----------------------------------- RANDOM WALK -------------------------------------------------------------

# Inicializar random_walk
random_walk=[0]
# Completa el ___
for x in range(100) :
    # Establece step: último elemento en random_walk
    step=random_walk[x]
    # Tira los dados
    dice = np.random.randint(1,7)
    # Determina el siguiente paso
    if dice <= 2:
        step=max(0,step-1)
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    # añade next_step a random_walk
    random_walk.append(step)
# Imprime random_walk
print(random_walk)

# NumPy se importa, la semilla se establece
# Inicialización
random_walk = [0]
for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    random_walk.append(step)
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Plot random_walk
plt.plot(random_walk)
# Muestra la gráfica
plt.show()

#----------------------- DISTRIBUTION --------------------------------------------------

# NumPy se importa; la semilla se establece
# Inicializar all_walks (no cambies esta línea)
all_walks = []
# Simular caminata aleatoria cinco veces
for i in range(5) :
    # Código de antes
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    # Añadir random_walk a all_walks
    all_walks.append(random_walk)
# Print all_walks
print(all_walks)

# numpy y matplotlib importados, semilla establecida
# Inicializar y rellenar todos los paseos
all_walks = []
for i in range(5) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)
# Convertir all_walks a la matriz NumPy: np_aw
np_aw=np.array(all_walks)
# Traza np_aw y muestralo
plt.plot(np_aw)
plt.show()
# Despeja la cifra
plt.clf()
# Transponer np_aw: np_aw_t
np_aw_t=np.transpose(np_aw)
# Trazar np_aw_t y mostra
plt.plot(np_aw_t)
plt.show()

# numpy y matplotlib importados, seed establecida
# Simula «random walk» 500 veces
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
# Crear y trazar np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
# Selecciona la última fila de np_aw_t: ends
ends = np_aw_t[-1,:]
# Trazar histograma de «ends», visualiza el gráfico
plt.hist(ends)
plt.show()