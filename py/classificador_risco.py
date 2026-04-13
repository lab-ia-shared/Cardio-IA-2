import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from pathlib import Path

# 1. Configurando o caminho do arquivo
pasta_projeto = Path(r"C:\Users\nicoa\OneDrive\Desktop\Cardio IA fase 2\docs") #IMPORTANTE: TROQUE O CAMINHO PARA O DA PASTA ONDE FORAM SALVOS OS ARQUIVOS
ARQUIVO_CSV = pasta_projeto / "triagem_risco.csv"

def treinar_classificador(caminho_csv):
    print("🤖 Iniciando Treinamento do Classificador CardioIA...\n")
    
    # Carregando o dataset
    df = pd.read_csv(caminho_csv)
    
    # 2. Separando as features (X = frases) e os labels (y = risco)
    X = df['frase']
    y = df['situacao']
    
    # 3. Aplicando o TF-IDF
    vectorizer = TfidfVectorizer(ngram_range=(1,2))
    X_vetorizado = vectorizer.fit_transform(X)
    
    # 4. Dividindo os dados (80% para treinar a IA, 20% para testar se ela aprendeu)
    X_train, X_test, y_train, y_test = train_test_split(X_vetorizado, y, test_size=0.2, random_state=42)
    
    # 5. Escolhendo e treinando o Modelo (Árvore de Decisão)
    modelo = DecisionTreeClassifier(random_state=42)
    modelo.fit(X_train, y_train)
    print("✅ Modelo treinado com sucesso!\n")
    
    # 6. Avaliando o desempenho do modelo
    previsoes = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, previsoes)
    
    print("-" * 40)
    print("📊 RESULTADOS DA AVALIAÇÃO:")
    print(f"Acurácia do Modelo: {acuracia * 100:.2f}%\n")
    print("Relatório Detalhado:")
    print(classification_report(y_test, previsoes))
    print("-" * 40)
    
    return modelo, vectorizer

def testar_modelo_ao_vivo(modelo, vectorizer):
    """Permite testar o modelo com novas frases no terminal."""
    print("\n🩺 Teste a Triagem Automatizada (Digite 'sair' para encerrar)")
    while True:
        nova_frase = input("\nDigite o relato do paciente: ")
        if nova_frase.lower() == 'sair':
            break
            
        # Transforma a nova frase em números usando o mesmo padrão do treinamento
        frase_vetorizada = vectorizer.transform([nova_frase])
        
        # Faz a predição
        risco = modelo.predict(frase_vetorizada)[0]
        
        if risco == "alto risco":
            print(f"🚨 ALERTA: Paciente classificado como ALTO RISCO. Encaminhar para emergência!")
        else:
            print(f"🟢 Classificação: BAIXO RISCO. Encaminhar para triagem comum.")

# === EXECUÇÃO DO SCRIPT ===
if __name__ == "__main__":
    try:
        # Treina e avalia o modelo
        modelo_treinado, vetorizador = treinar_classificador(ARQUIVO_CSV)
        
        # Inicia o modo interativo ara você testar o modelo
        testar_modelo_ao_vivo(modelo_treinado, vetorizador)
        
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo {ARQUIVO_CSV} não foi encontrado.")
        print("Verifique se o caminho da pasta_projeto está correto.")
