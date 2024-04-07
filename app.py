import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

#Header
st.header("Sprint 5: Herramientas de desarrollo de software")

# Casillas de verificación para elegir el tipo de gráfico
option_histogram = st.checkbox('Histograma')
option_scatter = st.checkbox('Gráfico de Dispersión')

# Generar gráfico basado en la selección del usuario
if option_histogram:
    #Primer histograma
    st.subheader("Gráfico de Histograma")
    fig_hist_1 = px.histogram(car_data, x='price', title='Distribución de Precios')
    st.plotly_chart(fig_hist_1, use_container_width=True)
    #Segundo histograma
    fig_hist_2 = px.histogram(car_data, x="odometer", title='Distribución del Odómetro')
    st.plotly_chart(fig_hist_2, use_container_width=True)

if option_scatter:
    #Primer gráfico de dispersión
    st.subheader("Gráfico de Dispersión")
    fig_scatter_1 = px.scatter(car_data, x='model_year', y='price', 
                             title='Precio vs Año del Modelo',
                             labels={'model_year': 'Año del Modelo', 'price': 'Precio'})
    st.plotly_chart(fig_scatter_1)
    #Segundo gráfico de dispersión
    fig_scatter_2 = px.scatter(car_data, x='days_listed', y='odometer', 
                                title='Odómetro vs Días en lista',
                                labels={'days_listed': 'Días en lista', 'odometer': 'Odómetro'})
    st.plotly_chart(fig_scatter_2)