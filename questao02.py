import streamlit as st
import pandas as pd

st.title('Localização das Comunidades Quilombolas (2022)')
df=pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

df.drop(columns=['Unnamed: 0'], inplace=True)
list = ['Lat_d', 'Long_d']
# convertendo para numeros
df[list] = df[list].apply(pd.to_numeric, errors='coerce')
estados = df['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     estados)
dadosFiltrados = df[df['NM_UF'] == estadoFiltro]
if st.checkbox('Mostrar tabela'):
  st.write(dadosFiltrados)
st.map(dadosFiltrados, latitude="Lat_d", longitude="Long_d")
