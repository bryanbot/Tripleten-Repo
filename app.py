import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

#Header
st.header("Sprint 5: Herramientas de desarrollo de software")

#hist_button = st.button('Construir histograma') # crear un botón

#if hist_button: # al hacer clic en el botón
    # escribir un mensaje
#    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
#    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
#    st.plotly_chart(fig, use_container_width=True)

# Casillas de verificación para elegir el tipo de gráfico
option_histogram = st.checkbox('Histograma')
option_scatter = st.checkbox('Gráfico de Dispersión')

# Generar gráfico basado en la selección del usuario
if option_histogram:
    st.subheader("Histograma")
    fig_hist_1 = px.histogram(car_data, x='price', title='Distribución de Precios')
    st.plotly_chart(fig_hist_1)
    #Segundo histograma
    fig_hist_2 = px.histogram(car_data, x="odometer", title='Distribución del Odómetro')
    st.plotly_chart(fig_hist_2, use_container_width=True)

if option_scatter:
    st.subheader("Gráfico de Dispersión: Precio vs Año del Modelo")
    fig_scatter = px.scatter(car_data, x='model_year', y='price', 
                             title='Precio vs Año del Modelo',
                             labels={'model_year': 'Año del Modelo', 'price': 'Precio'})
    st.plotly_chart(fig_scatter)