# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
# leer el archivo csv
netflix_df=pd.read_csv("netflix_data.csv", index_col=0)
# filtrar  tv show para tener el resto de las peliculas
netflix_subset = netflix_df[netflix_df['type'] != 'TV Show']
# crear dataframe con las columnas desde titulo hasta duracion
netflix_movies =pd.DataFrame(netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']])
# Filtrar películas que duren menos de 60 minutos
short_movies = netflix_movies.loc[netflix_movies['duration'] < 60]
# Lista para almacenar los colores asignados
colores = []
# Iterar sobre las filas del DataFrame
for index, fila in netflix_movies.iterrows():
    # Obtener el género de la película
    genero = fila['genre']
    # Asignar un color según el género
    if genero == 'Children':
        colores.append('blue')
    elif genero == 'Documentaries':
        colores.append('green')
    elif genero == 'Stand-Up':
        colores.append('yellow')
    else:
        colores.append('red')  # Para todo lo demás    
# Mostrar los primeros colores asignados
print(colores[:])  # Mostrar los primeros 10 colores como ejemplo
# Inicializar un objeto de figura matplotlib
fig = plt.figure()
# Crear un diagrama de dispersión
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colores, alpha=0.8)
# Etiquetas de los ejes x e y
plt.xlabel('AÑO DE LANZAMINETO')
plt.ylabel('DURACIÓN (min)')
# Título del diagrama de dispersión
plt.title('DURACION DE LA PELICULA POR AÑO DE ESTRENO')
# Mostrar el diagrama de dispersión
plt.show()