# importar pandas
import pandas as pd
# importar numpy
import numpy as np

#----------------------------- FUNCTIONES PARA SACAR DATOS DE UN DATAFRAME -------------------------------------
# inportar homelessnes desde un archivo csv
homelessness=pd.read_csv("proyecto_peliculas_netflix\\netflix_data.csv", index_col=0);
# Imprime el encabezado de homelessness
# head is for  print the first 5 rows of a dataframe
print(homelessness.head())
# Imprime información sobre homelessness
# info is for  print information about the data, including number of non-null values and types
print(homelessness.info())
# Imprime la forma de homelessness
# shape is for  print the dimensions of the dataframe (rows x columns)
print(homelessness.shape)
# Imprime una descripción de homelessness
# describe is for   print statistical summary of numerical columns including mean, median, min, max, etc
print(homelessness.describe())
# Imprime los valores de homelessness
# values is for   print all values in the DataFrame
print(homelessness.values)
# Imprime el índice de la columnas de homelessness
# columns is for  return array of column labels
print(homelessness.columns)
# Imprime el índice de las filas de homelessness
# index is for   return array of row labels
print(homelessness.index)

#-------------------- ORDER AND SORTING (ORDENAR Y SUBDIVIDIR) --------------------------------------

# Ordena homelessness por individuals en orden por defecto de sort_values  es ascendente (de menor a mayor).
homelessness_ind = homelessness.sort_values("duration")
# Imprime las primeras filas
print(homelessness_ind.head())

# Ordena homelessness por family_members en orden descendente
homelessness_fam = homelessness.sort_values("duration", ascending=False)
# Imprime las primeras filas
print(homelessness_fam.head())

# Ordena homelessness por region, luego por family_members descendente
homelessness_reg_fam = homelessness.sort_values(["duration", "genre"], ascending=[True,False])
# Imprime las primeras filas
print(homelessness_reg_fam.head())

#---------- SUB-CONJUNTO DE COLUMNAS---------------
# Selecciona la columna individuals
individuals = homelessness["duration"]
print(individuals.head())

# Imprime el encabezado del resultado.
state_fam=homelessness[["duration", "genre"]]
print(state_fam.head())

#------------ SUB-CONJUNTO DE FILAS ---------------------------------
# Filtra las filas donde individuals es mayor a 10000
ind_gt_10k = homelessness[homelessness["duration"]>100]
# Imprime el resultado
print(ind_gt_10k)

# Filtra las filas donde la region es Mountain
mountain_reg = homelessness[homelessness["genre"]=="Dramas"]
# Imprime el resultado
print(mountain_reg)

# Filtra las filas donde family_members sea menor a 1000 y la region es Pacific
fam_lt_1k_pac = homelessness[(homelessness["duration"]<30)&(homelessness["genre"]=="Dramas")]
# Imprime el resultado
print(fam_lt_1k_pac)

#------------- SUB-CONJUNTO DE FILAS CON VARIABLES CATEGORICAS -------------------------------------
# Selecciona las filas en la region South Atlantic o Mid-Atlantic
south_mid_atlantic = homelessness[(homelessness["title"]=="ANIMA") | (homelessness["title"]== "Poacher")]
# Imprime el resultado
print(south_mid_atlantic)

# Los estados del desierto de Mojave
titulo = ["ANIMA", "Poacher", "Zoo", "Zubaan"]
# Filtra las filas en los estados del desierto de Mojave
condition=homelessness["title"].isin(titulo)
mojave_homelessness = homelessness[condition]
# Imprime el resultado
print(mojave_homelessness)

#------------ NEW COLUMNS (NUEVAS COLUMNAS) -------------------------------------------------------------
# Agrega la columna total de la duracion por 10
homelessness["total"]=homelessness["duration"]*10
# Agrega p_individuals como la proporción del total que son individuos
homelessness["p_duracion"]=homelessness["duration"]/ homelessness["total"]
# Imprime el resultado
print(homelessness)

# Crea la columna indiv_per_10k como individuos sin hogar por 10k pop estatal
homelessness["indiv_per_10k"] = 10000 * homelessness["duration"]/homelessness["total"]
# Crea el subconjunto de filas donde indiv_per_10k sea mayor que 20
high_homelessness = homelessness[homelessness["duration"]>20]
# Ordena high_homelessness de forma descendente por indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("type", ascending=False)
# Usando high_homelessness_srt, selecciona las columnas title and duration
result = high_homelessness_srt[["title", "duration"]]
# Imprime result
print(result)

#---------------------------- SUMMARY STATICTICS ( ESTADISTICAS DE RESUMEN )  ----------------------------
sales=pd.read_csv("proyecto_peliculas_netflix\\netflix_data.csv", index_col=0);
# Imprime el encabezado del DataFrame sales
print(sales.head())
# Imprime la información sobre el DataFrame sales
print(sales.info())
# Imprime la media de weekly_sales
print("La media es: ")
print(sales["duration"].mean())
# Imprime la mediana de weekly_sales
print("La mediana es: ")
print(sales["duration"].median())
# Imprime el máximo de la columna date
print(sales["duration"].max())
# Imprime el mínimo de la columna date
print(sales["duration"].min())
# Una función IQR personalizada
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
# Imprime IQR de la columna temperature_c
print(sales["duration"].agg(iqr))
# Una función IQR personalizada
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
# Actualiza el código para imprimir IQR de durationo and duration
print(sales[["duration", "duration"]].agg(iqr))
# Importa NumPy y crea una función IQR personalizada
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
# Actualiza el código para imprimir IQR y np.median de temperature_c, fuel_price_usd_per_l, y unemployment
print(sales[["duration", "duration"]].agg([iqr, np.median]))

# Ordena sales_1_1 por duracion
sales=sales.sort_values("duration")
# Obtén la suma acumulada de duration, y añádela como duration_1
sales["duration_1"] = sales["duration"].cumsum()
# Obtén el máximo acumulativo de duration y añádelo como duration_2
sales["duration_2"]=sales["duration"].cummax()
# Consulta las columnas que calculaste
print(sales[["duration", "duration_1", "duration_2"]])

#-------------------------- COUNTING (CONTEO) -----------------------------------------------------------
# resumir datos categoricos usando el conteo
# Elimina combinaciones duplicadas de store/type
store_types = sales.drop_duplicates(subset=["store","type"])
print(store_types.head())

# Elimina combinaciones duplicadas de store/department
store_depts = sales.drop_duplicates(subset=["store", "department"])
print(store_depts.head())

# Selecciona las filas donde is_holiday es True y elimina fechas duplicadas
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset="date")

# Imprime la columna date de holiday_dates
print(holiday_dates["date"])

# Cuenta el número de tiendas de cada type
store_counts = store_types["type"].value_counts()
print(store_counts)

# Obtén la proporción de tiendas de cada type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Cuenta el número de cada department y ordena
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print(dept_counts_sorted)

# Obtén la proporción de cada department y ordena
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)

#------------------ GROUPED SUMMARY STATISTICS (ESTADISTICAS RESUMIDAS AGRUPADAS)------------------------------------















