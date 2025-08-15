import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración inicial
st.set_page_config(
    page_title="Análisis de Datos de Salud - Colombia",
    layout="wide"
)

st.title("🏥 Análisis Exploratorio Interactivo de Datos de Salud en Colombia")
st.write(
    """
    Este dashboard genera un conjunto de datos simulados sobre indicadores de salud en Colombia.
    Los datos son aleatorios y solo con fines de demostración.
    """
)

# Simulación de datos de salud
np.random.seed(42)
num_filas = 500
columnas_salud = [
    "Edad",
    "Sexo",  # M/F
    "Peso (kg)",
    "Altura (cm)",
    "IMC",
    "Presión Sistólica",
    "Presión Diastólica",
    "Glucosa (mg/dL)",
    "Colesterol (mg/dL)",
    "Enfermedad Crónica"  # Sí/No
]

# Datos numéricos aleatorios
data = {
    "Edad": np.random.randint(18, 90, num_filas),
    "Sexo": np.random.choice(["Masculino", "Femenino"], num_filas),
    "Peso (kg)": np.random.randint(45, 110, num_filas),
    "Altura (cm)": np.random.randint(150, 200, num_filas),
    "IMC": np.round(np.random.uniform(18, 35, num_filas), 1),
    "Presión Sistólica": np.random.randint(90, 180, num_filas),
    "Presión Diastólica": np.random.randint(60, 120, num_filas),
    "Glucosa (mg/dL)": np.random.randint(70, 200, num_filas),
    "Colesterol (mg/dL)": np.random.randint(120, 300, num_filas),
    "Enfermedad Crónica": np.random.choice(["Sí", "No"], num_filas)
}

df = pd.DataFrame(data)

# Mostrar tabla
st.subheader("📄 Datos de Salud Simulados")
st.dataframe(df)

# Checkbox para estadísticas
if st.checkbox("Mostrar estadísticas descriptivas"):
    st.subheader("📊 Estadísticas Descriptivas")
    st.write(df.describe(include="all"))

# Sidebar para seleccionar columnas y gráficos
st.sidebar.header("Configuración de Visualización")
columnas_seleccionadas = st.sidebar.multiselect(
    "Selecciona columnas para visualizar",
    options=df.columns,
    default=["Edad"]
)

tipo_grafico = st.sidebar.selectbox(
    "Tipo de gráfico",
    ["Barras", "Líneas", "Dispersión (Scatter)", "Histograma"]
)

# Generar gráfico
if columnas_seleccionadas:
    st.subheader(f"📈 Visualización - {tipo_grafico}")

    fig = None
    if tipo_grafico == "Barras":
        fig = px.bar(df, y=columnas_seleccionadas, title="Gráfico de Barras")
    elif tipo_grafico == "Líneas":
        fig = px.line(df, y=columnas_seleccionadas, markers=True, title="Gráfico de Líneas")
    elif tipo_grafico == "Dispersión (Scatter)":
        if len(columnas_seleccionadas) >= 2:
            fig = px.scatter(df, x=columnas_seleccionadas[0], y=columnas_seleccionadas[1],
                             color="Sexo", title="Gráfico de Dispersión")
        else:
            st.warning("Selecciona al menos dos columnas para gráfico de dispersión.")
    elif tipo_grafico == "Histograma":
        fig = px.histogram(df, x=columnas_seleccionadas[0], color="Sexo", barmode="overlay",
                           title="Histograma")

    if fig:
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Selecciona al menos una columna para visualizar.")

# Opción para descargar datos
st.sidebar.header("Descargar Datos")
csv = df.to_csv(index=False).encode("utf-8")
st.sidebar.download_button(
    label="📥 Descargar CSV",
    data=csv,
    file_name="datos_salud_colombia.csv",
    mime="text/csv"
)
