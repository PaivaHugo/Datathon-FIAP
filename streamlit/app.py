import streamlit as st
import random
import joblib
import pandas as pd

from sentence_transformers import SentenceTransformer
from utils import *

# Carrega o modelo salvo
@st.cache_resource
def carregar_modelo():
    return joblib.load("streamlit/modelo.joblib")

# Carrega o modelo salvo
@st.cache_resource
def carregar_modelo_embeddings():
    return SentenceTransformer('neuralmind/bert-base-portuguese-cased')

@st.dialog("Resultado da avaliação do candidato")
def result(predict):
    if predict >= 0.6:
        st.success(f"Candidato :green[APROVADO] (confiança: {predict:.2f})", icon="✅")
    elif predict < 0.6:
        st.error(f"Candidato :red[REPROVADO] (confiança: {predict:.2f})", icon="❌")
    else:
        st.warning("Resultado INCONCLUSÍVO", icon="⚠️")

def embbed_selected_columns(df, colunas):
    print("Iniciando a geração de embeddings")
    for col in colunas:
        text = df[col].tolist()
        embeddings = embedding_model.encode(text)

        df[col] = list(embeddings)

    return df



def simular_dados():
    st.session_state.vaga_sap = random.choice(["Não", "Sim"])
    st.session_state.vaga_pcd = random.choice(["Não", "Sim"])
    st.session_state.nivel_profissional_vaga = random.choice([
        "Auxiliar",  "Assistente", "Trainee", "Aprendiz", "Júnior", "Pleno", "Sênior", "Especialista", "Analista", "Líder", "Coordenador", "Supervisor", "Gerente"
        ])
    st.session_state.tipo_contratacao = random.choice([" ", "Cooperado", "CLT Full", "PJ/Autônomo", "Estagiário", ""])
    st.session_state.area_atuacao_vaga = random.choice([" ", "TI - Desenvolvimento/Programação-", "Recursos Humanos-", "TI - Arquitetura-", "Financeira/Controladoria-"])
    st.session_state.nivel_academico_vaga = random.choice([
        "Ensino Fundamental Completo", "Ensino Médio Incompleto", "Ensino Médio Completo",
        "Ensino Técnico Cursando", "Ensino Técnico Incompleto", "Ensino Técnico Completo",
        "Ensino Superior Cursando", "Ensino Superior Incompleto", "Ensino Superior Completo",
        "Pós Graduação Cursando", "Pós Graduação Completo",
        "Mestrado Cursando",  "Pós Graduação Incompleto", "Mestrado Completo"
       ])
    st.session_state.nivel_ingles_vaga = random.choice(["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"])
    st.session_state.nivel_espanhol_vaga = random.choice(["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"])
    st.session_state.outro_idioma_vaga = random.choice([" " ,"Alemão", "Português", "Italiano", "Francês"])
    st.session_state.principais_atividades = random.choice([" ", "Anallista de negócios", "Oracle Retail SIM specialist - SME", "03 vagas SAP MM FSR 4531\nInglês fluente"])
    st.session_state.competencias_tecnicas_comportamentais = random.choice([
        " ",
        "Requisitos: experiência em provisão/deferimento.",
        "Possibilidade para viagens Rio de Janeiro (verificar com os profissionais durante o processo seletivo)",
        "More than 5 years retail experience Oracle technologies ORSIM\nPortuguese should be mandatory if Brazil location"
        ])
    st.session_state.habilidades_comportamentais = random.choice(["Não", " ", "Valor até R$ 90,00 hora"])

    st.session_state.titulo_profissional = random.choice([" ", "Scrum", "Analista de Sistemas/Analista Programador", "programação"])
    st.session_state.candidato_pcd = random.choice(["Não", "Sim"])
    st.session_state.remuneracao = random.choice([0, 85, 150, 40, 25])
    st.session_state.area_atuacao_candidato = random.choice([" ", "Marketing-", "TI - Desenvolvimento/Programação-", "Gestão e Alocação de Recursos de TI-TI - Processos e Negócios-", "Administrativa-Financeira/Controladoria-"])
    # st.session_state.conhecimento_tecnico = random.choice([])
    st.session_state.cargo_atual = random.choice([" ", "Analista Programador (a)", "Analista Desenvolvedor", "Consultor (a) SAP MM Sênior"])
    st.session_state.nivel_profissional_candidato = random.choice([
        "Auxiliar",  "Assistente", "Trainee", "Aprendiz", "Júnior", "Pleno", "Sênior", "Especialista", "Analista", "Líder", "Coordenador", "Supervisor", "Gerente"
        ])
    st.session_state.nivel_academico_candidato = random.choice([
        "Ensino Fundamental Completo", "Ensino Médio Incompleto", "Ensino Médio Completo",
        "Ensino Técnico Cursando", "Ensino Técnico Incompleto", "Ensino Técnico Completo",
        "Ensino Superior Cursando", "Ensino Superior Incompleto", "Ensino Superior Completo",
        "Pós Graduação Cursando", "Pós Graduação Completo",
        "Mestrado Cursando",  "Pós Graduação Incompleto", "Mestrado Completo"
       ])
    st.session_state.nivel_ingles_candidato = random.choice(["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"])
    st.session_state.nivel_espanhol_candidato = random.choice(["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"])
    st.session_state.outro_idioma_candidato = random.choice([" ", "Alemão", "Português", "Italiano", "Francês"])
    st.session_state.instituicao_ensino_superior = random.choice([
        " ",
        "FIAP (Faculdade de Informática e Administração Paulista) São Paulo – SP.",
        "Universidade Mackenzie",
        "UFF",
        "MG -> Universidade Federal de Alfenas - UNIFAL"
        ])
    st.session_state.cursos = random.choice([" ", "Relações Públicas", "Análise de Sistemas & Tecnologia da Informação", "Gestão de Negócios", "Publicidade"])
    # st.session_state.certificacoes = random.choice([])
    # st.session_state.outras_certificacoes = random.choice([])

def simular_dados_aprovado():
    st.session_state.vaga_sap = "Não"
    st.session_state.vaga_pcd = "Não"
    st.session_state.nivel_profissional_vaga = "Sênior"
    st.session_state.tipo_contratacao = "CLT Full"
    st.session_state.area_atuacao_vaga = "TI - Desenvolvimento/Programação-"
    st.session_state.nivel_academico_vaga = "Ensino Superior Completo"
    st.session_state.nivel_ingles_vaga = "Avançado"
    st.session_state.nivel_espanhol_vaga = "Intermediário"
    st.session_state.outro_idioma_vaga = " "
    st.session_state.principais_atividades = " "
    st.session_state.competencias_tecnicas_comportamentais = " "
    st.session_state.habilidades_comportamentais = " "

    st.session_state.titulo_profissional = "Analista de Sistemas/Analista Programador"
    st.session_state.candidato_pcd = "Não"
    st.session_state.remuneracao = 150
    st.session_state.area_atuacao_candidato = "TI - Desenvolvimento/Programação-"
    # st.session_state.conhecimento_tecnico = random.choice([])
    st.session_state.cargo_atual = "Analista Programador (a)"
    st.session_state.nivel_profissional_candidato = "Sênior"
    st.session_state.nivel_academico_candidato = "Ensino Superior Completo"
    st.session_state.nivel_ingles_candidato = "Avançado"
    st.session_state.nivel_espanhol_candidato = "Intermediário"
    st.session_state.outro_idioma_candidato = " "
    st.session_state.instituicao_ensino_superior = " "
    st.session_state.cursos = "Análise de Sistemas & Tecnologia da Informação"
    # st.session_state.certificacoes = "Análise de Sistemas & Tecnologia da Informação"
    # st.session_state.certificacoes = random.choice([])
    # st.session_state.outras_certificacoes = random.choice([])  

def simular_reprovado():
    st.session_state.vaga_sap = "Não"
    st.session_state.vaga_pcd = "Sim"
    st.session_state.nivel_profissional_vaga = "Sênior"
    st.session_state.tipo_contratacao = "CLT Full"
    st.session_state.area_atuacao_vaga = "Recursos Humanos-"
    st.session_state.nivel_academico_vaga = "Ensino Superior Completo"
    st.session_state.nivel_ingles_vaga = "Avançado"
    st.session_state.nivel_espanhol_vaga = "Intermediário"
    st.session_state.outro_idioma_vaga = " "
    st.session_state.principais_atividades = " "
    st.session_state.competencias_tecnicas_comportamentais = " "
    st.session_state.habilidades_comportamentais = " "

    st.session_state.titulo_profissional = "Analista de Sistemas/Analista Programador"
    st.session_state.candidato_pcd = "Não"
    st.session_state.remuneracao = 150
    st.session_state.area_atuacao_candidato = "TI - Desenvolvimento/Programação-"
    # st.session_state.conhecimento_tecnico = random.choice([])
    st.session_state.cargo_atual = "Analista Programador (a)"
    st.session_state.nivel_profissional_candidato = "Júnior"
    st.session_state.nivel_academico_candidato = "Ensino Superior Incompleto"
    st.session_state.nivel_ingles_candidato = "Nenhum"
    st.session_state.nivel_espanhol_candidato = "Nenhum"
    st.session_state.outro_idioma_candidato = " "
    st.session_state.instituicao_ensino_superior = " "
    st.session_state.cursos = "Análise de Sistemas & Tecnologia da Informação"
    # st.session_state.certificacoes = random.choice([])
    # st.session_state.outras_certificacoes = random.choice([])

def limpar_dados():
    st.session_state.vaga_sap = "Não"
    st.session_state.vaga_pcd = "Não"
    st.session_state.nivel_profissional_vaga = "Auxiliar"
    st.session_state.tipo_contratacao = " "
    st.session_state.area_atuacao_vaga = " "
    st.session_state.nivel_academico_vaga = "Ensino Fundamental Completo"
    st.session_state.nivel_ingles_vaga = "Nenhum"
    st.session_state.nivel_espanhol_vaga = "Nenhum"
    st.session_state.outro_idioma_vaga = " "
    st.session_state.principais_atividades = " "
    st.session_state.competencias_tecnicas_comportamentais = " "
    st.session_state.habilidades_comportamentais = " "

    st.session_state.titulo_profissional = " "
    st.session_state.candidato_pcd = "Não"
    st.session_state.remuneracao = 0
    st.session_state.area_atuacao_candidato = " "
    st.session_state.conhecimento_tecnico = " "
    st.session_state.cargo_atual = " "
    st.session_state.nivel_profissional_candidato = "Auxiliar"
    st.session_state.nivel_academico_candidato = "Ensino Fundamental Completo"
    st.session_state.nivel_ingles_candidato = "Nenhum"
    st.session_state.nivel_espanhol_candidato = "Nenhum"
    st.session_state.outro_idioma_candidato = " "
    st.session_state.instituicao_ensino_superior = " "
    st.session_state.cursos = " "
    # st.session_state.certificacoes = random.choice([])
    # st.session_state.outras_certificacoes = random.choice([])

model = carregar_modelo()
embedding_model = carregar_modelo_embeddings()

st.title("Análise de candidatos para vagas de trabalho")

st.markdown("---")
with st.expander("Simular dados"):
    col1, col2 = st.columns(2)
    with col1:
        st.button("Simular candidato aprovado", on_click=simular_dados_aprovado, icon="✅")
        st.button("Simular candidato reprovado", on_click=simular_reprovado, icon="❌")
    with col2:
        st.button("Preencher com dados aleatórios", on_click=simular_dados, icon="🎲")
        st.button("Limpar formulário", on_click=limpar_dados, icon="🧹")

st.markdown("---")


with st.form("form"):
    ###
    ### DADOS DA VAGA ###
    ###
    st.write("Dados da vaga")

    col1, col2 = st.columns(2)
    
    with col1:
        vaga_sap = st.radio("Vaga SAP?", ["Não", "Sim"], horizontal=True, key="vaga_sap")
        
        nivel_profissional_vaga = st.selectbox("Nível profissional da vaga:", [
        "Auxiliar",  "Assistente", "Trainee", "Aprendiz", "Júnior", "Pleno", "Sênior", "Especialista", "Analista", "Líder", "Coordenador", "Supervisor", "Gerente"
        ], key="nivel_profissional_vaga")

        tipo_contratacao = st.text_input("Tipo de contratação:", key="tipo_contratacao")
        competencias_tecnicas_comportamentais = st.text_input("Competências técnicas e comportamentais:", key="competencias_tecnicas_comportamentais")
        nivel_ingles_vaga = st.selectbox("Nível de inglês da vaga:", ["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"], key="nivel_ingles_vaga")


    with col2:
        vaga_pcd = st.radio("Vaga PCD?", ["Não", "Sim"], horizontal=True, key="vaga_pcd")
        
        nivel_academico_vaga = st.selectbox("Nível Acadêmico da vaga:", [
            "Ensino Fundamental Completo", "Ensino Médio Incompleto", "Ensino Médio Completo",
            "Ensino Técnico Cursando", "Ensino Técnico Incompleto", "Ensino Técnico Completo",
            "Ensino Superior Cursando", "Ensino Superior Incompleto", "Ensino Superior Completo",
            "Pós Graduação Cursando", "Pós Graduação Completo",
            "Mestrado Cursando",  "Pós Graduação Incompleto", "Mestrado Completo"
            ], key="nivel_academico_vaga")
        
        area_atuacao_vaga = st.text_input("Área de atuação:", key="area_atuacao_vaga")
        habilidades_comportamentais = st.text_input("Habilidades comportamentais necessárias:", key="habilidades_comportamentais")
        nivel_espanhol_vaga = st.selectbox("Nível de espanhol da vaga:", ["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"], key="nivel_espanhol_vaga")
    
    principais_atividades = st.text_input("Principais atividades:", key="principais_atividades")
    outro_idioma_vaga = st.text_input("Outro idioma da vaga:", key="outro_idioma_vaga")

    ###
    ### DADOS DO CANDIDATO ###
    ###
    st.markdown("---")
    st.write("Dados do Candidato")
    
    col1, col2 = st.columns(2)

    with col1:
        titulo_profissional = st.text_input("Título profissional:", key="titulo_profissional")
        candidato_pcd = st.radio("Candidato PCD?", ["Não", "Sim"], horizontal=True, key="candidato_pcd")


    with col2:
        area_atuacao_candidato = st.text_input("Area de atuação:", key="area_atuacao_candidato")
        remuneracao = st.number_input("Remuneração:", key="remuneracao")


    conhecimento_tecnico = st.text_input("Conhecimento técnico:", key="conhecimento_tecnico")
    cargo_atual = st.text_input("Cargo atual:", key="cargo_atual")
    nivel_profissional_candidato = st.selectbox("Nível profissional do candidato:", [
        "Auxiliar",  "Assistente", "Trainee", "Aprendiz", "Júnior", "Pleno", "Sênior", "Especialista", "Analista", "Líder", "Coordenador", "Supervisor", "Gerente"
        ], key="nivel_profissional_candidato")
    
    nivel_academico_candidato = st.selectbox("Nível acadêmico do candidato:", [
        "Ensino Fundamental Completo", "Ensino Médio Incompleto", "Ensino Médio Completo",
        "Ensino Técnico Cursando", "Ensino Técnico Incompleto", "Ensino Técnico Completo",
        "Ensino Superior Cursando", "Ensino Superior Incompleto", "Ensino Superior Completo",
        "Pós Graduação Cursando", "Pós Graduação Completo",
        "Mestrado Cursando",  "Pós Graduação Incompleto", "Mestrado Completo"
       ], key="nivel_academico_candidato")
    

    col1, col2 = st.columns(2)
    with col1:
        nivel_ingles_candidato = st.selectbox("Nível de inglês do candidato:", ["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"], key="nivel_ingles_candidato")
    
    with col2:
        nivel_espanhol_candidato = st.selectbox("Nível de espanhol do candidato:", ["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"], key="nivel_espanhol_candidato")
    
    outro_idioma_candidato = st.text_input("Outro idioma do candidato:", key="outro_idioma_candidato")

    instituicao_ensino_superior = st.text_input("Instituição de ensino superior:", key="instituicao_ensino_superior")
    cursos = st.text_input("Cursos:", key="cursos")
    certificacoes = st.text_input("Certificações:", key="certificacoes")
    outras_certificacoes = st.text_input("Outras certificações:", key="outras_certificacoes")


    submitted = st.form_submit_button("Avaliar candidato")

    if submitted:
        with st.spinner("Avaliando candidato...", show_time=True):
            features = {
                    "df_vg-vaga_sap": vaga_sap,
                    "df_vg-tipo_contratacao": tipo_contratacao,
                    "df_vg-vaga_especifica_para_pcd": vaga_pcd,
                    "df_vg-nivel profissional": nivel_profissional_vaga,
                    "df_vg-nivel_academico": nivel_academico_vaga,
                    "df_vg-nivel_ingles": nivel_ingles_vaga,
                    "df_vg-nivel_espanhol": nivel_espanhol_vaga,
                    "df_vg-outro_idioma": outro_idioma_vaga,
                    "df_vg-areas_atuacao": area_atuacao_vaga,
                    "df_vg-principais_atividades": principais_atividades,
                    "df_vg-competencia_tecnicas_e_comportamentais": competencias_tecnicas_comportamentais,
                    "df_vg-habilidades_comportamentais_necessarias": habilidades_comportamentais,
                    "df_applics-titulo_profissional": titulo_profissional,
                    "df_applics-pcd": candidato_pcd,
                    "df_applics-area_atuacao": area_atuacao_candidato,
                    "df_applics-remuneracao": remuneracao,
                    "df_applics-conhecimentos_tecnicos": conhecimento_tecnico,
                    "df_applics-cargo_atual": cargo_atual,
                    "df_applics-nivel_profissional": nivel_profissional_candidato,
                    "df_applics-nivel_academico": nivel_academico_candidato,
                    "df_applics-nivel_ingles": nivel_ingles_candidato,
                    "df_applics-nivel_espanhol": nivel_espanhol_candidato,
                    "df_applics-outro_idioma": outro_idioma_candidato,
                    "df_applics-instituicao_ensino_superior": instituicao_ensino_superior,
                    "df_applics-cursos": cursos,
                    "df_applics-certificacoes": certificacoes,
                    "df_applics-outras_certificacoes": outras_certificacoes
                }

            features = embbed_selected_columns(features, features.columns)
            
            pred = model.predict(features)
            result(pred[0][0])