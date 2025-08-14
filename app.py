import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Configuración inicial
st.set_page_config(
    page_title="Análisis Exploratorio Interactivo",
    layout="wide"
)

st.title("📊 Análisis Exploratorio Interactivo con Streamlit")
st.write("Genera datos aleatorios y visualízalos de forma dinámica.")

# Generación de datos
st.sidebar.header("Configuración de Datos")
num_filas = st.sidebar.slider("Número de filas", 5, 50, 10)
num_columnas = st.sidebar.slider("Número de columnas", 2, 6, 3)

np.random.seed(42)
data = np.random.randint(10, 100, size=(num_filas, num_columnas))
column_names = [f"Columna_{i+1}" for i in range(num_columnas)]
df = pd.DataFrame(data, columns=column_names)

# Mostrar datos
st.subheader("📄 Datos Generados")
st.dataframe(df)

# Checkbox para estadísticas
if st.checkbox("Mostrar estadísticas descriptivas"):
    st.subheader("📊 Estadísticas Descriptivas")
    st.write(df.describe())

# Selección de columnas y tipo de gráfico
st.sidebar.header("Configuración de Gráficos")
columnas_seleccionadas = st.sidebar.multiselect(
    "Selecciona columnas para visualizar", df.columns, default=df.columns[0]
)

tipo_grafico = st.sidebar.selectbox(
    "Tipo de gráfico", ["Barras", "Líneas", "Dispersión (Scatter)"]
)

# Visualización
if columnas_seleccionadas:
    st.subheader(f"📈 Visualización - {tipo_grafico}")
    if tipo_grafico == "Barras":
        fig = px.bar(df, y=columnas_seleccionadas, title="Gráfico de Barras")
    elif tipo_grafico == "Líneas":
        fig = px.line(df, y=columnas_seleccionadas, markers=True, title="Gráfico de Líneas")
    else:
        if len(columnas_seleccionadas) >= 2:
            fig = px.scatter(
                df, x=columnas_seleccionadas[0], y=columnas_seleccionadas[1],
                size_max=10, title="Gráfico de Dispersión"
            )
        else:
            st.warning("Selecciona al menos dos columnas para el gráfico de dispersión.")
            fig = None
    
    if fig:
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Selecciona al menos una columna para visualizar.")
