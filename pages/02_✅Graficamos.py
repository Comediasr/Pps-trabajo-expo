import streamlit as st
import pandas as pd
import plotly.express as px

aeropuertos = pd.read_csv('ar-airports.csv')
st.title("Gráficos")

# Gráfico de barras
st.subheader("Gráfico de barras")

filtro = aeropuertos['region_name'].value_counts().reset_index()
filtro.columns = ['Provincia', 'Cantidad']

fig = px.bar(
    filtro,
    x='Cantidad',
    y='Provincia',
    title="Cantidad de Aeropuertos por Provincia"
)

st.plotly_chart(fig)
st.markdown("Este gráfico de **barras** nos muestra la cantidad de aeropuertos por provincia. Como podemos observar, gran parte de los aeropuertos se encuentran en la provincia de **Buenos Aires**. También podemos ver una cantidad considerable de aeropuertos en provincias como **Córdoba** y **Santa Fe**. Por otro lado, tenemos provincias que cuentan con pocos aeropuertos, como **San Juan**, **La Rioja** y **Jujuy**.")

# Gráfico de torta
st.subheader("Gráfico de torta")

filtro = aeropuertos['type'].value_counts().reset_index()
filtro.columns = ['Tipo', 'Cantidad']

fig = px.pie(
    filtro,
    names='Tipo',
    values='Cantidad',
    title="Porcentajes de tipos de Aeropuertos"
)

st.plotly_chart(fig)
st.markdown("Este gráfico de **torta** nos muestra los porcentajes correspondientes a cada tipo de aeropuerto. Como podemos observar, un gran porcentaje corresponde a los aeropuertos **pequeños**, que son los que predominan en el mapa. También podemos ver una proporción considerable de **helipuertos**. Por otro lado, existen algunos tipos que ni siquiera se pueden distinguir a simple vista en el gráfico, debido a su bajo porcentaje, como los aeropuertos **grandes** o los puertos para **globos aerostáticos**.")
