import yfinance as yf
from bcb import sgs
import pandas as pd

def get_complete_macro_data():
    """Busca dados reais para todas as categorias do painel macro."""
    try:
        # --- DADOS BRASIL (BCB & B3) ---
        # Selic Meta (432), IPCA 12m (13522)
        df_bcb = sgs.get({'selic': 432, 'ipca': 13522}, last=1)
        
        # Tickers Globais e Locais
        tickers = {
            "ibov": "^BVSP",
            "dolar": "USDBRL=X",
            "msci_world": "URTH",
            "stoxx50": "FEZ",
            "nikkei": "^N225",
            "vix": "^VIX",
            "brent": "BZ=F",
            "gold": "GC=F",
            "copper": "HG=F",
            "t10": "^TNX", # 10Y Treasury Yield
            "t2": "^IRX"    # 13-week bill (proxy p/ taxa curta) ou use tickers específicos
        }
        
        data = yf.download(list(tickers.values()), period="2d")['Close']
        
        # Consolidação
        results = {
            "br": {
                "selic": df_bcb['selic'].iloc[-1],
                "ipca": df_bcb['ipca'].iloc[-1],
                "ibov": data["^BVSP"].iloc[-1],
                "ibov_var": ((data["^BVSP"].iloc[-1] / data["^BVSP"].iloc[-2]) - 1) * 100,
                "dolar": data["USDBRL=X"].iloc[-1],
                "dolar_var": ((data["USDBRL=X"].iloc[-1] / data["USDBRL=X"].iloc[-2]) - 1) * 100,
            },
            "global": {
                "msci": data["URTH"].iloc[-1],
                "stoxx": data["FEZ"].iloc[-1],
                "nikkei": data["^N225"].iloc[-1]
            },
            "risk": {
                "vix": data["^VIX"].iloc[-1],
                "vix_var": ((data["^VIX"].iloc[-1] / data["^VIX"].iloc[-2]) - 1) * 100
            },
            "bonds": {
                "t10": data["^TNX"].iloc[-1],
                "t2": data["^IRX"].iloc[-1]
            },
            "commodities": {
                "brent": data["BZ=F"].iloc[-1],
                "gold": data["GC=F"].iloc[-1],
                "copper": data["HG=F"].iloc[-1]
            }
        }
        return results
    except Exception as e:
        return None