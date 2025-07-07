import streamlit as st
import requests
import datetime

st.title("Análise de candidatos para vagas de trabalho")

user_input = {
    "cod_vaga": None,
    "candidato_pcd": None,
    "data_nascimento": None,
    "email": None,
    "objetivo_profissional": None,
    "nivel_profissional": None,
    "nivel_academico": None,
    "nivel_ingles": None,
    "nivel_espanhol": None,
    "area_atuação": None
    }


with st.form("form"):
    # Campo de código da vaga
    cod_vaga = st.text_input("Código da vaga:")

    # Campo de opção PCD
    candidato_pcd = st.radio("Candidato PCD?", ["Não", "Sim"])

    # Campo de data de nascimento
    data_nascimento = st.date_input("Data de nascimento:", datetime.date(2025, 1, 1))
    data_str = data_nascimento.strftime("%Y-%m-%d")

    # Campo de email
    email = st.text_input("E-mail:")

    # Campo de Objetivo Profissional
    objetivo_profissional = st.text_input("Objetivo profissional:")

    # Campo de Nível Profissional
    nivel_profissional = st.text_input("Nível profissional:")

    # Campo de Nível Acadêmico
    nivel_academico = st.selectbox("Nível Acadêmico:", ["Fundamental Incompleto", "Fundamental Completo", "Médio Incompleto", "Médio Completo", "Superior Incompleto", "Superior Completo"])

    # Campo de Nível de Inglês
    nivel_ingles = st.selectbox("Nível de inglês:", ["Nenhum", "Básico", "Intermediário", "Avançado"])

    # Campo de Código da Vaga
    nivel_espanhol = st.selectbox("Nível de espanhol:", ["Nenhum", "Básico", "Intermediário", "Avançado"])

    # Campo de Área de atuação
    area_atuação = st.text_input("Área de atuação:")


    
    submitted = st.form_submit_button("Enviar")


    # user_input["data"] = data_str
    # response = requests.post(
    #     url="http://api:5002/predict",
    #     json=user_input
    # )

    # if response.status_code == 200:
    #     result = response.json()
    #     st.success(f"Previsão do preço do barril de petróleo: {result['data']['prediction']}")
    # else:
    #     st.error("Erro ao fazer a previsão!")