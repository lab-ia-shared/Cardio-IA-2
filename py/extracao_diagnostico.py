import pandas as pd
from pathlib import Path

def carregar_dados(caminho_txt, caminho_csv):
    """Carrega as frases dos pacientes e o mapa de conhecimento."""
    # Lendo as frases
    with open(caminho_txt, 'r', encoding='utf-8') as f:
        frases = [linha.strip() for linha in f if linha.strip()]
    
    # Carregando a ontologia com Pandas
    mapa = pd.read_csv(caminho_csv)
    return frases, mapa

def analisar_sintomas(frases, mapa):
    """Cruza as frases com o mapa de conhecimento para sugerir diagnósticos."""
    resultados = []
    
    for i, frase in enumerate(frases, 1):
        frase_lower = frase.lower()
        diagnostico_sugerido = "Nenhum diagnóstico conclusivo encontrado."
        sintomas_encontrados = []
        
        # Itera sobre cada linha do DataFrame
        for _, row in mapa.iterrows():
            s1 = str(row['sintoma_1']).lower()
            s2 = str(row['sintoma_2']).lower()
            
            # Verifica se pelo menos um dos sintomas mapeados está na frase
            if s1 in frase_lower or s2 in frase_lower:
                if s1 in frase_lower: sintomas_encontrados.append(s1)
                if s2 in frase_lower: sintomas_encontrados.append(s2)
                
                diagnostico_sugerido = row['doenca_associada']
                break # Para a busca ao achar uma correspondência forte
                
        resultados.append({
            'Paciente': f"Paciente {i}",
            'Relato': frase,
            'Sintomas Extraídos': ", ".join(sintomas_encontrados) if sintomas_encontrados else "Nenhum",
            'Diagnóstico Sugerido': diagnostico_sugerido
        })
        
    return resultados

# === EXECUÇÃO DO SCRIPT ===
if __name__ == "__main__":
    # 1. pasta exata onde os arquivos foram salvos
    pasta_projeto = Path(r"C:\Users\nicoa\OneDrive\Desktop\Cardio IA fase 2\docs") #IMPORTANTE: TROQUE O CAMINHO PARA O DA PASTA ONDE FORAM SALVOS OS ARQUIVOS
    
    # 2. procurando os arquivos na pasta
    ARQUIVO_TXT = pasta_projeto / "sintomas_pacientes.txt"
    ARQUIVO_CSV = pasta_projeto / "mapa_conhecimento.csv"
    
    print("Iniciando o Estetoscópio Digital CardioIA...\n")
    print(f"Buscando arquivos na pasta: {pasta_projeto}\n")
    
    try:
        # Passando os caminhos completos para a função
        frases_pacientes, mapa_conhecimento = carregar_dados(ARQUIVO_TXT, ARQUIVO_CSV)
        diagnosticos = analisar_sintomas(frases_pacientes, mapa_conhecimento)
        
        # Exibindo os resultados formatados
        for diag in diagnosticos:
            print(f"[{diag['Paciente']}]")
            print(f"Relato: '{diag['Relato']}'")
            print(f"🔍 Sintomas detectados: {diag['Sintomas Extraídos']}")
            print(f"🩺 Diagnóstico Sugerido: {diag['Diagnóstico Sugerido']}")
            print("-" * 60)
            
    except FileNotFoundError as e:
        print(f"❌ Erro: Arquivo não encontrado.")
        print(f"Verifique se os caminhos abaixo estão corretos e se os arquivos existem:")
        print(f"TXT: {ARQUIVO_TXT}")
        print(f"CSV: {ARQUIVO_CSV}")
