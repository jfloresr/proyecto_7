import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.read_csv("D:/Proyecto_TRIPLETEN/proyecto_7/vehicles_us.csv")

st.title('Dashboard de Vehiculos Usados')
st.write('Bienvenido a la Aplicacion')
st.header('Visualizaciones')

if st.button('Mostrar Histograma de Precios'):
    st.write("Distribucion de precios de vehiculos")
    fig=px.histogram(df,x="price",title='Distribucion de Precios',nbins=300)
    st.plotly_chart(fig,use_container_width=True)

if st.button('Mostrar Diagrama de Dispersion (Kilometraje vrs Precio)'):
    st.write('Relacion entre Kilometraje y Precio')
    fig=px.scatter(df,x='odometer',y='price',color="condition",title="Kilometraje vrs Precio")
    st.plotly_chart(fig,use_container_width=True)

columnas_dinamicas=st.selectbox('Selecciona la Columna para analizarla en el Histograma:',options=df.columns)

if st.button('Construir Histograma'):
    st.write(f"Histograma para la columna: {columnas_dinamicas}")
    fig=px.histogram(df,x=columnas_dinamicas, title=f"Distribuicion de Columna {columnas_dinamicas}")
    st.plotly_chart(fig,use_container_width=True)


