import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV
data = pd.read_csv('Customers.csv')

# Visualizar distribuciones de variables numéricas mediante histogramas
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
sns.histplot(data['Age'], kde=True, color='skyblue', bins=20)
plt.title('Distribución de Edades')

plt.subplot(2, 2, 2)
sns.histplot(data['Annual Income ($)'], kde=True, color='salmon', bins=20)
plt.title('Distribución de Ingresos Anuales')

plt.subplot(2, 2, 3)
sns.histplot(data['Spending Score (1-100)'], kde=True, color='green', bins=20)
plt.title('Distribución de Puntuación de Gasto')

plt.subplot(2, 2, 4)
sns.histplot(data['Work Experience'], kde=True, color='orange', bins=20)
plt.title('Distribución de Experiencia Laboral')

plt.tight_layout()
plt.show()

# Visualizar distribución de variables categóricas mediante diagramas de barras
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.countplot(x='Gender', data=data)
plt.title('Distribución de Género')

plt.subplot(1, 2, 2)
sns.countplot(x='Profession', data=data)
plt.title('Distribución de Profesión')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Calcular estadísticas descriptivas para las variables numéricas
stats_descriptivas = data.describe()

# Imprimir tabla de estadísticas descriptivas de manera bonita
styled_stats_descriptivas = stats_descriptivas.style.set_caption("Estadísticas Descriptivas").\
    background_gradient(cmap='coolwarm')

# Mostrar la tabla de estadísticas descriptivas
display(styled_stats_descriptivas)
