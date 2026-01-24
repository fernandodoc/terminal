import yfinance as yf

def get_fund_data(ticker):
    """Busca dados de FIIs, ETFs e Fundos via Ticker."""
    try:
        ticker_search = ticker.strip().upper()
        # Se for um ticker curto (ex: HGLG11), adiciona .SA para a B3
        if not ticker_search.endswith(".SA") and len(ticker_search) <= 7:
            ticker_search = f"{ticker_search}.SA"
            
        fund = yf.Ticker(ticker_search)
        # Tenta pegar os dados brutos (fast_info é mais rápido que info)
        info = fund.info
        
        if not info or ('regularMarketPrice' not in info and 'previousClose' not in info):
            return {"Erro": f"Ativo '{ticker}' não encontrado. Use o Ticker da B3 (ex: MXRF11)."}

        price = info.get('regularMarketPrice') or info.get('previousClose') or 0
        
        return {
            "Nome": info.get("longName", "N/A"),
            "Cotação": price,
            "DY": info.get("yield", 0) * 100 if info.get("yield") else "N/A",
            "P/VP": info.get("priceToBook", "N/A"),
            "Performance_12m": info.get("fiftyTwoWeekChange", 0) * 100,
            "Resumo": info.get("longBusinessSummary", "Descrição indisponível.")
        }
    except Exception as e:
        return {"Erro": f"Erro na base: {str(e)}"}

# Criamos uma função vazia ou de aviso para o CNPJ não dar erro de import
def get_fund_by_cnpj(cnpj):
    return {"Erro": "Consulta por CNPJ direto na CVM indisponível. Utilize o Ticker do fundo."}