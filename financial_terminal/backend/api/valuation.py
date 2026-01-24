import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_fundamentus_data(ticker):
    """
    Versão Ultra-Robusta para extração do Fundamentus.
    """
    try:
        ticker = ticker.replace(".SA", "").strip().upper()
        url = f"https://www.fundamentus.com.br/detalhes.php?papel={ticker}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        
        with requests.Session() as s:
            response = s.get(url, headers=headers, timeout=15)
            # O Fundamentus usa ISO-8859-1, se o Python usar UTF-8 ele não acha nada
            response.encoding = 'ISO-8859-1' 
            
        if response.status_code != 200:
            return {"Erro": f"Erro de conexão: {response.status_code}"}

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # O Fundamentus organiza os dados em tabelas com a classe 'tabela'
        # Vamos buscar todas e extrair os dados
        tables = soup.find_all('table')
        
        if len(tables) < 5: # O site padrão tem 5 tabelas principais
            return {"Erro": f"Ticker '{ticker}' não retornou dados oficiais. Verifique o código."}

        data = {}
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all(['td'])
                # Percorre as células em pares (rótulo e valor)
                for i in range(len(cols)):
                    text = cols[i].text.strip().replace('?', '')
                    if text:
                        # Se for um rótulo (geralmente termina com ":" ou é seguido de um valor)
                        # Vamos mapear o conteúdo de forma sequencial
                        data[text] = cols[i+1].text.strip() if i+1 < len(cols) else ""
                        i += 1 # Pula para o próximo par

        # Limpeza específica para as chaves que o Streamlit vai buscar
        # O site às vezes coloca espaços ou caracteres invisíveis
        cleaned_data = {k.strip(): v.strip() for k, v in data.items() if k}
        
        return cleaned_data

    except Exception as e:
        return {"Erro": f"Falha sistêmica: {str(e)}"}