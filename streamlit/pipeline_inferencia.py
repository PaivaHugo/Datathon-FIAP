
import numpy as np
import pandas as pd
import re
import joblib
from keras.models import load_model

class PipelineInferência():
    def __init__(self):
        self.model = load_model('streamlit/modelo_mlp_aprovacao.h5')
        self. encoder = joblib.load('streamlit/encoder_categorias.joblib')
        self.scaler = joblib.load('streamlit/scaler_remuneracao.joblib')

    # Função utilitária para extrair remuneração
    def extrair_valor(self, texto):
        match = re.search(r'(\d+[\.,]?\d*)', str(texto))
        return float(match.group(1).replace(',', '.')) if match else 0.0

    def avalia_nivel_idioma_candidato_vs_vaga(self, nivel_vaga, nivel_candidato):
        # print(f'VG: {nivel_vaga}')
        # print(f'CAND: {nivel_candidato}')
        nivel_ingles = {
            0: 'Nenhum',
            1: 'Básico',
            2: 'Intermediário',
            3: 'Técnico',
            4: 'Avançado',
            5: 'Fluente'
        }
        
        n_vaga = 0
        n_candidato = 0
        for k, v in nivel_ingles.items():
            if nivel_vaga == v:
                n_vaga = k
                break
            
        for key, value in nivel_ingles.items():
            if nivel_candidato == "":
                n_candidato = 0
                break
            if nivel_candidato == value:
                n_candidato = key
                break

        if n_candidato >= n_vaga or ( n_vaga > n_candidato and (n_vaga - n_candidato) <= 2 ):
            return 1
        else:
            return 0
        
    def avalia_area_atuacao_candidato_vs_vaga(self, areas_vaga, areas_candidato):
        match_area = 0
        if areas_candidato != "":
            a_candidato = areas_candidato.split(",")

            
            for i in a_candidato:
                if i in areas_vaga:
                    match_area = 1
                    break
        return match_area

    def avalia_nivel_profissional_candidato_vs_vaga(self, nivel_vaga, nivel_candidato):
        nivel_profissional = {
        "": 0,
        "Trainee": 1,
        "Aprendiz": 2,
        "Auxiliar": 3, 
        "Estagiário": 4,
        "Assistente": 5,
        "Técnico de Nível Médio": 6,
        "Júnior": 7,
        "Pleno": 8,
        "Sênior": 9,
        "Analista": 10,
        "Especialista": 11,
        "Líder": 12,
        "Supervisor": 13,
        "Coordenador": 14,
        "Gerente": 15
        }
        if nivel_candidato == "" or nivel_profissional[nivel_candidato] >= nivel_profissional[nivel_vaga] :
            return 1
        else:
            return 0

    def avalia_nivel_academico_candidato_vs_vaga(self, nivel_vaga, nivel_candidato):
        nivel_academico = {
        '': 0,
        'Ensino Fundamental Incompleto': 1,
        'Ensino Fundamental Cursando': 2,
        "Ensino Fundamental Completo": 3,
        "Ensino Médio Incompleto": 4,
        'Ensino Médio Cursando': 5,
        "Ensino Médio Completo": 6,
        "Ensino Técnico Incompleto": 7,
        "Ensino Técnico Cursando": 8,
        "Ensino Técnico Completo": 9,
        "Ensino Superior Incompleto": 10,
        "Ensino Superior Cursando": 11,
        "Ensino Superior Completo": 12,
        "Pós Graduação Incompleto": 13,
        "Pós Graduação Cursando": 14,
        "Pós Graduação Completo": 15,
        'Mestrado Incompleto': 16,
        "Mestrado Cursando": 17, 
        "Mestrado Completo": 18,  
        'Doutorado Incompleto': 19, 
        'Doutorado Cursando': 20, 
        'Doutorado Completo': 21
        }
        # if nivel_candidato == nivel_vaga
        n_candidato = nivel_academico[nivel_candidato]
        n_vaga = nivel_academico[nivel_vaga]
        
        if nivel_candidato == "" or n_candidato >= n_vaga or ( n_vaga > n_candidato and (n_vaga - n_candidato) <= 2 ):
            return 1
        else:
            return 0

    # Função de predição para novo exemplo
    def prever_aprovacao(self, df_novo: pd.DataFrame):
        # Geração de texto composto
        df_novo = df_novo.T

        # Categóricos
        cat_cols = ['df_vg-vaga_sap', 'df_vg-vaga_especifica_para_pcd', 'df_vg-nivel profissional',
                    'df_vg-nivel_academico', 'df_vg-nivel_ingles', 'df_vg-nivel_espanhol',
                    'df_applics-pcd', 'df_applics-nivel_profissional', 'df_applics-nivel_academico',
                    'df_applics-nivel_ingles', 'df_applics-nivel_espanhol']
        X_cat = self.encoder.transform(df_novo[cat_cols].fillna(''))

        # Numérica
        df_novo['df_applics-remuneracao_num'] = df_novo['df_applics-remuneracao'].apply(self.extrair_valor)
        X_num = self.scaler.transform(df_novo[['df_applics-remuneracao_num']])

        # Matches
        df_novo["match_nivel_ingles"] = df_novo.apply(
        lambda row: self.avalia_nivel_idioma_candidato_vs_vaga(row['df_vg-nivel_ingles'], row['df_applics-nivel_ingles']), axis=1)

        df_novo["match_nivel_espanhol"] = df_novo.apply(
        lambda row: self.avalia_nivel_idioma_candidato_vs_vaga(row['df_vg-nivel_espanhol'], row['df_applics-nivel_espanhol']), axis=1)

        df_novo["match_area_atuacao"] = df_novo.apply(
        lambda row: self.avalia_area_atuacao_candidato_vs_vaga(row['df_vg-areas_atuacao'], row['df_applics-area_atuacao']), axis=1)

        df_novo["match_nivel_academico"] = df_novo.apply(
        lambda row: self.avalia_nivel_academico_candidato_vs_vaga(row['df_vg-nivel_academico'], row['df_applics-nivel_academico']), axis=1)

        df_novo["match_nivel_profissional"] = df_novo.apply(
        lambda row: self.avalia_nivel_profissional_candidato_vs_vaga(row['df_vg-nivel profissional'], row['df_applics-nivel_profissional']), axis=1)


        X_match = df_novo[['match_nivel_ingles','match_nivel_espanhol','match_area_atuacao','match_nivel_profissional','match_nivel_academico']].values

        # Concatenação final
        #X = np.concatenate([emb_vaga, emb_candidato, similaridade_vaga_candidato, X_cat, X_num, X_match], axis=1)
        X = np.concatenate([X_cat, X_num, X_match], axis=1)

        # Predição
        threshold=0.75
        probas = self.model.predict(X)
        classes = (probas > threshold).astype(int)

        return pd.DataFrame({"resultado": {
            'probabilidade_aprovacao': probas.ravel(),
            'classe_prevista': classes.ravel()
        }})

# if __name__ == '__main__':
#     df_exemplo = pd.read_json('teste6.json')
#     resultado = prever_aprovacao(df_exemplo)
#     print(resultado)
