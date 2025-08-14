import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuración inicial de la página
st.set_page_config(
    page_title="Análisis Exploratorio de Datos Aleatorios",
    layout="centered"
)

st.title("📊 Análisis Exploratorio de Datos Aleatorios")
st.write("Esta aplicación genera un conjunto de datos aleatorios y muestra visualizaciones de barras y líneas.")

# Generar datos aleatorios
st.subheader("Generar Datos")
num_filas = st.slider("Número de filas:", min_value=5, max_value=50, value=10)
num_columnas = st.slider("Número de columnas:", min_value=2, max_value=5, value=3)

np.random.seed(42)
data = np.random.randint(10, 100, size=(num_filas, num_columnas))
column_names = [f"Columna_{i+1}" for i in range(num_columnas)]
df = pd.DataFrame(data, columns=column_names)

# Mostrar tabla de datos
st.subheader("Datos Generados")
st.dataframe(df)

# Estadísticas descriptivas
st.subheader("Estadísticas Descriptivas")
st.write(df.describe())

# Visualización de Barras
st.subheader("📉 Gráfico de Barras")
columna_barras = st.selectbox("Selecciona columna para gráfico de barras:", df.columns)
fig_bar, ax_bar = plt.subplots()
df[columna_barras].plot(kind='bar', ax=ax_bar, color='skyblue')
ax_bar.set_title(f"Gráfico de Barras - {columna_barras}")
ax_bar.set_xlabel("Índice")
ax_bar.set_ylabel("Valor")
st.pyplot(fig_bar)

# Visualización de Líneas
st.subheader("📈 Gráfico de Líneas")
columna_lineas = st.selectbox("Selecciona columna para gráfico de líneas:", df.columns)
fig_line, ax_line = plt.subplots()
df[columna_lineas].plot(kind='line', ax=ax_line, marker='o', color='green')
ax_line.set_title(f"Gráfico de Líneas - {columna_lineas}")
ax_line.set_xlabel("Índice")
ax_line.set_ylabel("Valor")
st.pyplot(fig_line)

st.success("✅ Análisis completado.")
