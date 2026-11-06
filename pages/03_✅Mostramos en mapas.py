
#Mapas
import folium
import streamlit as st
from streamlit_folium import folium_static, st_folium
import pandas as pd
#Lo que hace esto es crear el mapa base que vamos a usar, el title toma el mapa base del pais y el ATTR da las atribuciones del territorio, ejemplo el nombre de las islas malvinas se usa correctamente y no se pone falklands
def generar_mapa():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )
    
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m


aeropuertos = pd.read_csv('ar-airports.csv')
st.title("Distribución de los tipos de aeropuertos")
mapa = generar_mapa()

colores = {
    'large_airport': 'red',
    'medium_airport': 'orange',
    'small_airport': 'green',
    'closed': 'gray',
    'heliport': 'blue',
    'balloonport': 'purple'
}

#esta funcion lo que hace es agregar las marcas, los 2 primeros row toman las cordenadas que se van a usar (las del dataset), el tercer row lo que hace es que cuando el usuario seleccione un marcador va a mostrar el dato de la columna de ese aeropuerto, este caso el nombre (name)
def agregar_marca_aerop(row):
    
    folium.Marker(
        [row['latitude_deg'], row['longitude_deg']],
        popup=row['name'],
        icon=folium.Icon(color=colores.get(row['type'], 'black'))
        #añade lo previo al mapa base
        ).add_to(mapa)

#el ac1 y ac2 lo que hace es que crea 2 columnas en streamlit, el AC1 los marcadores que se ven en la pagina y el AC2 el mapa
ac1,ac2 = st.columns([0.3, 0.7])
#Lo de abajo son los filtros parar ver en el mapa, el ac1 checkbox crea el filtro si se marca da true si no da false
r_areas = ac1.checkbox("Grandes")
#el if comprueba si el filtro esta seleccionado, si es true filtra la columna requerida y su respectivo dato, el apply ejecuta la funcion y muestra cada fila que cumpla con lo filtrado, el axis 1 hace que esto se aplique fila por fila
if r_areas:
    a_larg = aeropuertos[aeropuertos['type']=='large_airport']
    a_larg.apply(agregar_marca_aerop, axis=1)
r_parques = ac1.checkbox("Medianos")
if r_parques:
    a_med = aeropuertos[aeropuertos['type']=='medium_airport']
    a_med.apply(agregar_marca_aerop, axis=1)
r_monu = ac1.checkbox("Pequeños")
if r_monu:
    a_small = aeropuertos[aeropuertos['type']=='small_airport']
    a_small.apply(agregar_marca_aerop, axis=1)
r_closed = ac1.checkbox("Cerrados")
if r_closed:
    a_closed = aeropuertos[aeropuertos['type']=='closed']
    a_closed.apply(agregar_marca_aerop, axis=1)
r_helipuerto = ac1.checkbox("Helipuertos")
if r_helipuerto:
    a_helipuerto = aeropuertos[aeropuertos['type']=='heliport']
    a_helipuerto.apply(agregar_marca_aerop, axis=1)
r_balloon = ac1.checkbox("Globos Aerostaticos")
if r_balloon:
    a_balloon = aeropuertos[aeropuertos['type']=='balloonport']
    a_balloon.apply(agregar_marca_aerop, axis=1) 
#Este with lo que hace es que muestra el mapa en la pagina (st folium), mientras que el key es un identificado del propio mapa dentro de la pagina
with ac2:
    st_folium(mapa, key='aeropuertos')

st.markdown("En esta parte de la página podemos ver cómo están distribuidos los distintos tipos de aeropuertos mediante un **mapa interactivo**. Para facilitar la visualización, el usuario puede elegir qué tipo de aeropuerto quiere que se muestre utilizando los filtros disponibles en el mapa.")
st.markdown("Como podemos observar, hay una gran cantidad de aeropuertos **pequeños**, especialmente en la provincia de **Buenos Aires**. Por otro lado, algunos tipos, como los aeropuertos **grandes** y los puertos para **globos aerostáticos**, solo se encuentran en la provincia de Buenos Aires.")