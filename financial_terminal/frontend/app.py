import sys
import os

# Adiciona a pasta 'financial_terminal' ao sistema para o Python achar a pasta 'backend'
# O '..' sobe uma pasta a partir de 'frontend'
current_dir = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.join(current_dir, '..'))

if root_path not in sys.path:
    sys.path.append(root_path)

# Adiciona a raiz do projeto (elite-pro) ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from layout import apply_custom_style, render_header
from callbacks.news import render_news_portal
from callbacks.macro import render_macro_panel
from callbacks.calculators import render_advanced_calculators
from callbacks.calculadora_cidadao import render_calculadora_cidadao
from callbacks.stocks import render_stocks_analysis
from callbacks.financial_health import render_financial_health
from callbacks.compound_interest import render_compound_interest
from callbacks.fiis import render_fiis_analysis
from callbacks.etfs import render_etfs_analysis
from callbacks.dividends import render_dividends_analysis
from callbacks.funds import render_funds_analysis
from callbacks.backtesting import render_backtesting_analysis
from callbacks.stock_exchange import render_stock_exchange
from callbacks.portfolio import render_portfolio_vision
from callbacks.tesouro_direto import render_tesouro_direto
from callbacks.valuation import render_valuation_analysis
from callbacks.previdencia import render_previdencia
from callbacks.educacao import render_education_module

# Configuração Global
st.set_page_config(
    page_title="Financial Terminal Pro",
    layout="wide",
    page_icon="📈"
)

def main():
    apply_custom_style()
    
    # --- SIDEBAR NAVEGAÇÃO ---
    st.sidebar.markdown("<h1 style='text-align: center;'>🛡️</h1>", unsafe_allow_html=True)
    st.sidebar.title("em desenvolvimento")
    
    # Mapeamento atualizado com ETFs e FIIs
    menu_options = {
        "📰 Portais": "news",
        "🏛️ Bolsa de Valores": "stock_exchange",
        "🌎 Macro": "macro",
        "🧮 Simulador de Liberdade": "calculators",
        "🏛️ Calculadora Cidadão": "calc_cidadao",
        "💼 Contrate um especialista": "portfolio",
        "🔍 Valuation": "valuation",
        "🏥 Saúde Financeira": "financial_health",
        "⏳ Juros Compostos": "compound_interest",
        "📊 Ações": "stocks",
        "🏢 FIIs": "fiis",          # Nova navegação
        "🌍 ETFs": "etfs",          # Nova navegação
        "🏦 Fundos": "funds",
        "💰 Dividendos": "dividends",
        "🏦 Títulos Públicos": "tesouro_direto",
        "🛡️ Previdência": "previdencia",
        "🧪 Backtesting": "backtesting",
        "🎓 Educação Financeira": "educacao"
    }

    if 'page' not in st.session_state:
        st.session_state.page = 'news'

    for label, page_code in menu_options.items():
        if st.sidebar.button(label, use_container_width=True):
            st.session_state.page = page_code

    # --- RENDERIZAÇÃO DO CONTEÚDO ---
    render_header()
    
    current_page = st.session_state.page

    # Switch case atualizado
    if current_page == "news":
        st.subheader("Informação estruturada. Insumo para sua decisão.")
        st.caption("Menos ruído e mais contexto para decisões melhores.")
        render_news_portal()# Os cards aparecem logo abaixo do título
    elif current_page == "stock_exchange":
        st.subheader("Bolsa de valores")
        render_stock_exchange()
    elif current_page == "macro":
        st.subheader("Painel Macroeconômico Global & Brasil")
        render_macro_panel()
    elif current_page == "calculators":
        st.subheader("🧮 Calculadoras Avançadas de Patrimônio")
        render_advanced_calculators()
    elif current_page == "calc_cidadao":
        render_calculadora_cidadao()
    elif current_page == "portfolio":
        st.subheader("Análise de Carteira Elite")
        render_portfolio_vision()
    elif current_page == "valuation":
        st.subheader("Análise de Valuation")
        render_valuation_analysis()
    elif current_page == "financial_health":
        st.subheader("Check-up de Saúde Financeira")
        render_financial_health()
    elif current_page == "compound_interest":
        st.subheader("Simulador de Longo Prazo")
        render_compound_interest()
    elif current_page == "stocks":
        st.subheader("Stock Picker & Análise Fundamentalista")
        render_stocks_analysis()
    elif current_page == "fiis":
        st.subheader("Real Estate Intelligence (FIIs) - Yield & P/VP")
        render_fiis_analysis()
    elif current_page == "etfs":
        st.subheader("Global & Factor ETFs Selection")
        render_etfs_analysis()
    elif current_page == "funds":
        st.subheader("Screening de Fundos de Investimento")
        render_funds_analysis()
    elif current_page == "dividends":
        st.subheader("Mapa de Dividendos e Yield On Cost")
        render_dividends_analysis()
    elif current_page == "tesouro_direto":
        render_tesouro_direto()
    elif current_page == "previdencia":
        render_previdencia()
    elif current_page == "backtesting":
        st.subheader("Laboratório de Estratégias (Backtest)")
        render_backtesting_analysis()
    elif current_page == "educacao":
        render_education_module()


    st.sidebar.markdown("---")
    st.sidebar.caption("Sessão Ativa: Fernando | Especialista em Investimentos")
    st.sidebar.caption("Versão: 1.0.0-PRO")

if __name__ == "__main__":

    main()







