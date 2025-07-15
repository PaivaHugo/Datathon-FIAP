import streamlit as st
import requests
import datetime
import time

st.title("Análise de candidatos para vagas de trabalho")

@st.dialog("Resultado da avaliação do candidato")
def result(status):
    if status.lower() == "aprovado":
        st.success("Candidato :green[APROVADO]", icon="✅")
    elif status.lower() == "reprovado":
        st.error("Candidato :red[REPROVADO]", icon="❌")
    else:
        st.warning("Resultado INCONCLUSÍVO", icon="⚠️")


with st.form("form"):
    ###
    ### DADOS DA VAGA ###
    ###
    st.write("Dados da vaga")

    col1, col2 = st.columns(2)
    
    with col1:
        titulo_vaga = st.text_input("Título da vaga:")
        vaga_sap = st.radio("Vaga SAP?", ["Não", "Sim"], horizontal=True)
        vaga_pcd = st.radio("Vaga PCD?", ["Não", "Sim"], horizontal=True)
        principais_atividades = st.text_input("Principais atividades:")

    with col2:
        tipo_contratacao = st.text_input("Tipo de contratação:")
        area_atuação = st.text_input("Área de atuação:")
        competencias_tecnicas_comportamentais = st.text_input("Competências técnicas e comportamentais:")
        habilidades_comportamentais = st.text_input("Habilidades comportamentais necessárias:")


    ###
    ### DADOS DO CANDIDATO ###
    ###
    st.markdown("---")
    st.write("Dados do Candidato")
    
    curriculo = st.text_input("Currículo do candidato:", )
    
    col3, col4 = st.columns(2)

    with col3:
        titulo_profissional = st.text_input("Título profissional:")
        candidato_pcd = st.radio("Candidato PCD?", ["Não", "Sim"], horizontal=True)


    with col4:
        objetivo_profissional = st.text_input("Objetivo profissional:")
        remuneracao = st.number_input("Remuneração:")


    area_atuacao = st.text_input("Area de atuação:")
    conhecimento_tecnico = st.text_input("Conhecimento técnico:")
    cargo_atual = st.text_input("Cargo atual:")
    comentario = st.text_input("Comentário:")
    nivel_profissional = st.selectbox("Nível Profissional:", [
        "Auxiliar",  "Assistente", "Trainee", "Aprendiz", "Júnior", "Pleno", "Sênior", "Especialista", "Analista", "Líder", "Coordenador", "Supervisor", "Gerente"
        ])
    
    nivel_academico = st.selectbox("Nível Acadêmico:", [
        "Ensino Fundamental Completo", "Ensino Médio Incompleto", "Ensino Médio Completo",
        "Ensino Técnico Cursando", "Ensino Técnico Incompleto", "Ensino Técnico Completo",
        "Ensino Superior Cursando", "Ensino Superior Incompleto", "Ensino Superior Completo",
        "Pós Graduação Cursando", "Pós Graduação Completo",
        "Mestrado Cursando",  "Pós Graduação Incompleto", "Mestrado Completo"
       ])
    

    col5, col6 = st.columns(2)
    with col5:
        nivel_ingles = st.selectbox("Nível de inglês:", ["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"])
    
    with col6:
        nivel_espanhol = st.selectbox("Nível de espanhol:", ["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"])
    
    outro_idioma = st.text_input("Outro idioma:")

    instituicao_ensino_superior = st.text_input("Instituição de ensino superior:")
    cursos = st.text_input("Cursos:")
    certificacoes = st.text_input("Certificações:")
    outras_certificacoes = st.text_input("Outras certificações:")



    submitted = st.form_submit_button("Avaliar candidato")

    if submitted:
        with st.spinner("Avaliando candidato...", show_time=True):
            time.sleep(5)
            result("aprovado")