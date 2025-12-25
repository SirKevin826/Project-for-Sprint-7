import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de datos de anuncios de venta de coches en EE.UU.')
car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir diagrama de dispersión')

if scatter_button:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price", color="condition")
    st.plotly_chart(fig, use_container_width=True)
