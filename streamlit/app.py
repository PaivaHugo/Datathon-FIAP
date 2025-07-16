import streamlit as st
import time
import random

st.title("Análise de candidatos para vagas de trabalho")

@st.dialog("Resultado da avaliação do candidato")
def result(status):
    if status.lower() == "aprovado":
        st.success("Candidato :green[APROVADO]", icon="✅")
    elif status.lower() == "reprovado":
        st.error("Candidato :red[REPROVADO]", icon="❌")
    else:
        st.warning("Resultado INCONCLUSÍVO", icon="⚠️")

def simular_dados():
    st.session_state.vaga_sap = random.choice(["Não", "Sim"])
    st.session_state.vaga_pcd = random.choice(["Não", "Sim"])
    st.session_state.nivel_profissional_vaga = random.choice([
        "Auxiliar",  "Assistente", "Trainee", "Aprendiz", "Júnior", "Pleno", "Sênior", "Especialista", "Analista", "Líder", "Coordenador", "Supervisor", "Gerente"
        ])
    st.session_state.tipo_contratacao = random.choice([" ", "Cooperado", "CLT Full", "PJ/Autônomo", "Estagiário", ""])
    st.session_state.area_atuação = random.choice([" ", "TI - Desenvolvimento/Programação-", "Recursos Humanos-", "TI - Arquitetura-", "Financeira/Controladoria-"])
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
    st.session_state.area_atuacao = random.choice([" ", "Marketing-", "TI - Desenvolvimento/Programação-", "Gestão e Alocação de Recursos de TI-TI - Processos e Negócios-", "Administrativa-Financeira/Controladoria-"])
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
    


st.markdown("---")
st.write("Simular dados")
st.button("Preencher dados aleatóriamente", on_click=simular_dados)
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
        
        area_atuação = st.text_input("Área de atuação:", key="area_atuação")
        habilidades_comportamentais = st.text_input("Habilidades comportamentais necessárias:", key="habilidades_comportamentais")
        nivel_espanhol_vaga = st.selectbox("Nível de espanhol da vaga:", ["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"], key="nivel_espanhol_vaga")
    
    principais_atividades = st.text_input("Principais atividades:", key="principais_atividades")
    outro_idioma_vaga = st.text_input("Outro idioma da vaga:", key="outro_idioma_vaga")

    ###
    ### DADOS DO CANDIDATO ###
    ###
    st.markdown("---")
    st.write("Dados do Candidato")
    
    col3, col4 = st.columns(2)

    with col3:
        titulo_profissional = st.text_input("Título profissional:", key="titulo_profissional")
        candidato_pcd = st.radio("Candidato PCD?", ["Não", "Sim"], horizontal=True, key="candidato_pcd")


    with col4:
        area_atuacao = st.text_input("Area de atuação:", key="area_atuacao")
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
    

    col5, col6 = st.columns(2)
    with col5:
        nivel_ingles_candidato = st.selectbox("Nível de inglês do candidato:", ["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"], key="nivel_ingles_candidato")
    
    with col6:
        nivel_espanhol_candidato = st.selectbox("Nível de espanhol do candidato:", ["Nenhum", "Básico", "Intermediário", "Avançado", "Fluente", "Técnico"], key="nivel_espanhol_candidato")
    
    outro_idioma_candidato = st.text_input("Outro idioma do candidato:", key="outro_idioma_candidato")

    instituicao_ensino_superior = st.text_input("Instituição de ensino superior:", key="instituicao_ensino_superior")
    cursos = st.text_input("Cursos:", key="cursos")
    certificacoes = st.text_input("Certificações:", key="certificacoes")
    outras_certificacoes = st.text_input("Outras certificações:", key="outras_certificacoes")



    submitted = st.form_submit_button("Avaliar candidato")

    if submitted:
        with st.spinner("Avaliando candidato...", show_time=True):
            time.sleep(5)
            result("aprovado")