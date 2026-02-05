import streamlit as st
import yfinance as yf
import pandas as pd
import requests

@st.cache_data(ttl=3600)
def get_fund_data(ticker):
    """Busca dados de FIIs e ETFs via Yahoo Finance."""
    try:
        t = ticker.strip().upper()
        ticker_sa = f"{t}.SA" if not t.endswith(".SA") else t
        asset = yf.Ticker(ticker_sa)
        
        # Coleta info e histórico
        info = asset.info
        history = asset.history(period="1y")

        if history.empty:
            return {"Erro": f"Ticker {t} não encontrado ou sem dados na B3."}

        # Preço atual e Performance
        price_current = history['Close'].iloc[-1]
        price_start = history['Close'].iloc[0]
        perf_12m = ((price_current / price_start) - 1) * 100

        return {
            "Nome": info.get("longName", t),
            "Cotação": price_current,
            "DY": (info.get("dividendYield", 0) * 100) if info.get("dividendYield") else 0,
            "P/VP": info.get("priceToBook", 0),
            "Performance_12m": perf_12m,
            "Resumo": info.get("longBusinessSummary", "Resumo estratégico não disponível.")
        }
    except Exception as e:
        return {"Erro": "Conexão instável com a B3. Tente novamente."}

@st.cache_data(ttl=86400) # Cache de 24h
def get_fund_by_cnpj(cnpj):
    # Limpeza do CNPJ
    cnpj_clean = "".join(filter(str.isdigit, str(cnpj)))
    
    if len(cnpj_clean) != 14:
        return {"Erro": "CNPJ inválido. Digite os 14 números."}
    
    try:
        # Rota estável para dados cadastrais de fundos CVM
        url = f"https://brasilapi.com.br/api/cvm/fundos/v1/{cnpj_clean}"
        response = requests.get(url, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "razao_social": data.get("razao_social", "Nome não disponível"),
                "classe": data.get("classe", "Não informada"),
                "pl_estrategia": float(data.get("patrimonio_liquido", 0) or 0),
                "valor_cota": float(data.get("valor_cota", 0) or 0),
                "num_cotistas": int(data.get("numero_cotistas", 0) or 0),
                "gestor": data.get("gestor", "Consultar lâmina"),
                "administrador": data.get("administrador", "Consultar lâmina"),
                "taxa_adm": data.get("taxa_administracao", "N/A")
            }
        else:
            return {"Erro": f"Fundo não localizado (Status {response.status_code})."}
            
    except Exception as e:
        # Evite mensagens genéricas, retorne o erro real para debug
        return {"Erro": "Conexão com a base CVM interrompida. Tente novamente."}
