
import streamlit as st
import pandas as pd
import plotly.express as px

# Título principal de la app
st.title('Análisis de vehículos en EE.UU.')

# Encabezado de sección
st.header('Exploración interactiva del conjunto de datos')

# Leer el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Vista previa de los datos
st.subheader('Vista previa del conjunto de datos')
st.write(car_data.head())

# Botón para construir histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el odómetro de los vehículos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: precio vs año del modelo')
    fig2 = px.scatter(car_data, x='model_year', y='price', color='condition')
    st.plotly_chart(fig2, use_container_width=True)