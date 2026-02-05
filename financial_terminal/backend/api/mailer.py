import requests
import json

def enviar_dados_ao_especialista(dados):
    # CERTIFIQUE-SE de que a URL termina com o ID do seu formulário
    # Exemplo: https://formspree.io/f/mqkvpkn
    FORMSPREE_URL = "https://formspree.io/f/xgolwpkw"

    # Headers explicitos ajudam o servidor do Streamlit a passar a requisição
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        # Enviamos como json=dados em vez de data=dados
        response = requests.post(
            FORMSPREE_URL, 
            json=dados, 
            headers=headers, 
            timeout=10
        )
        
        # Isso vai imprimir o log detalhado no seu "Manage App"
        print(f"FORMSPREE LOG: Status {response.status_code} | Resposta: {response.text}")
        
        return response.status_code == 200
    except Exception as e:
        print(f"FORMSPREE ERROR: {str(e)}")
        return False
