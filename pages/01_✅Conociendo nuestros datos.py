import pandas as pd
import streamlit as st

aeropuertos =  pd.read_csv('ar-airports.csv')
st.title("Aeropuertos Dataset")
st.subheader("Acá podemos ver cómo está formado el conjunto de datos que estamos investigando, cuáles son sus columnas, qué tipos de datos contiene y cómo se dividen.")
filas, columnas = aeropuertos.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = aeropuertos.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')
    st.markdown("Como podemos ver, el conjunto de datos está formado por un total de **956** registros de aeropuertos, cuyos datos se distribuyen en **24** columnas.")
    
    
nombres_type = aeropuertos['type'].unique()
cant_type = len(aeropuertos['type'].unique())


with st.expander("¿Cuáles son los nombres de las columnas?"):
   
    st.write(aeropuertos.columns)
    st.markdown("Como podemos observar, los nombres de las columnas muestran que este conjunto de datos está registrado en inglés. Algunas son bastante obvias, como **name** o **type**, mientras que otras son más complejas, como **scheduled_service** o **gps_code**. En esta ocasión, solo nos vamos a centrar en las columnas type y region_name.")

with st.expander("¿Que datos tiene la columna type?(tipos de aeropuertos)"):
    st.write(nombres_type)
    st.markdown("En los conjuntos de datos existen columnas con datos **categóricos** y **no categóricos**. Las columnas con datos categóricos son aquellas que contienen uno o varios valores que se repiten, mientras que las no categóricas presentan valores que, generalmente, no se repiten.")
    st.write("Acá tenemos un ejemplo de una columna categórica. En este caso, podemos observar los distintos tipos de aeropuertos y cómo algunos valores se repiten dentro del conjunto de datos.")
    st.write("**Datos Extras**")
    st.write("Los aeropuertos pequeños (small_airport) son los más comunes del país y cuentan con una gran cantidad de registros dentro del conjunto de datos.")
    st.write("Los puertos para globos aerostáticos (balloonport) son los menos comunes, con un solo registro en el conjunto de datos, ubicado en la provincia de Buenos Aires.")
with st.expander("¿Cuántos son los valores únicos de la columna **type**?"):
    st.write(cant_type)
    st.write("Como ya vimos, esta columna contiene **datos categóricos**, lo que significa que sus valores se agrupan en distintas categorías(datos unicos). En este caso, cuenta con **6** categorías diferentes, que corresponden a los tipos de aeropuertos registrados en el conjunto de datos.")

        