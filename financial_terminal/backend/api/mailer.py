import requests

def enviar_dados_ao_especialista(dados):
    # CERTIFIQUE-SE de que a URL termina com o ID do seu formulário
    # Exemplo: https://formspree.io/f/mqkvpkn
    FORMSPREE_URL = "https://formspree.io/f/xgolwpkw"

    # Headers explicitos ajudam o servidor do Streamlit a passar a requisição
    headers = {
        "Accept": "application/json"
    }
    
    try:
        # Adicionamos headers para garantir que a API entenda que é um formulário
        response = requests.post(
            FORMSPREE_URL, 
            data=dados,
            timeout=10 # Evita que o site fique travado se a conexão cair
        )
        
        # O Formspree retorna 200 se for sucesso
        return response.status_code == 200
    except Exception as e:
        # Isso imprimirá o erro real no seu terminal do VS Code para debug
        print(f"Erro detalhado na conexão: {e}")
        return False
