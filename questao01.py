import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'nomeServidor': ['Thamires', 'Carolini', 'Pryscilla'],
    'salario': [4000,8000,8000]
})

st.write("Criando uma tabela!")
st.write(df)
opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['nomeServidor'])

st.write('Você selecionou: ', opcao)

dadosFiltrados = df[df['nomeServidor'] == opcao]
st.write(dadosFiltrados)
