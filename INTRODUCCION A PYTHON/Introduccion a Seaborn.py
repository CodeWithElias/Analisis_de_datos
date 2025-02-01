# Instalar seaborn
#pip install seaborn

# Import Matplotlib and Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
ladoX=[12,23,34,55,45,1,21,23,32,34]
ladoY=[12,23,34,55,45,1,21,23,55,87]
sns.scatterplot(x=ladoX, y=ladoY)

# Show plot (muestra el grafico)
#plt.show()

pf=pd.read_csv("proyecto_peliculas_netflix\\netflix_data.csv");
print(pf.head(10))

# Create a count plot with type in the x
sns.countplot(x="type", data=pf)

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="duration" , y="genre", 
                data=pf,
                hue="type",
                hue_order=["TV Show", "Movie"]
                )

# Show plot
plt.show()

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Movie": "red", "TV Show": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="genre", data=pf,
                hue="type",
                palette=palette_colors)

# Display plot
plt.show()