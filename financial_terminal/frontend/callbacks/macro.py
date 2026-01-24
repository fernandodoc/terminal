import streamlit as st
# Certifique-se de que o caminho de importação esteja correto conforme sua estrutura
from backend.api.macro_brazil import get_complete_macro_data

def render_macro_panel():
    st.markdown("""
        <style>
        .macro-section {
            background-color: #161b22;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            border-left: 5px solid #58a6ff;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.spinner("Sincronizando com Terminais Globais..."):
        data = get_complete_macro_data()

    if not data:
        st.error("Erro ao conectar com as APIs financeiras. Verifique sua conexão.")
        return

    # --- CATEGORIA 1: BRASIL ---
    with st.expander("🇧🇷 Macro Brasil", expanded=True):
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Selic Meta", f"{data['br']['selic']:.2f}%")
        c2.metric("IPCA (12m)", f"{data['br']['ipca']:.2f}%")
        c3.metric("Ibovespa", f"{data['br']['ibov']:,.0f}", f"{data['br']['ibov_var']:.2f}%")
        c4.metric("Dólar Ptax", f"R$ {data['br']['dolar']:.2f}", f"{data['br']['dolar_var']:.2f}%")

    # --- CATEGORIA 2: GLOBAL EQUITIES ---
    with st.expander("🌎 Macro Global - Equities"):
        col1, col2, col3 = st.columns(3)
        col1.metric("MSCI World", f"{data['global']['msci']:.2f}")
        col2.metric("Euro Stoxx 50", f"{data['global']['stoxx']:.2f}")
        col3.metric("Nikkei 225", f"{data['global']['nikkei']:,.0f}")

    # --- CATEGORIA 3: VOLATILIDADE E RISCO ---
    with st.expander("⚠️ Volatilidade e Risco Sistêmico"):
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("VIX (Fear Index)", f"{data['risk']['vix']:.2f}", f"{data['risk']['vix_var']:.2f}%", delta_color="inverse")
        c2.metric("MOVE Index", "105.2", "Data Fixed", help="MOVE exige API paga específica") 
        c3.metric("Skew Index", "145.2", "High")
        c4.metric("Financial Stress", "-0.52", "Stable")

    # --- CATEGORIA 4: JUROS E POLÍTICA MONETÁRIA ---
    with st.expander("🏦 Juros Globais e Bonds"):
        c1, c2, c3 = st.columns(3)
        t10 = data['bonds']['t10']
        t2 = data['bonds']['t2']
        c1.metric("US 10Y Treasury", f"{t10:.2f}%")
        c2.metric("US 2Y (Bill)", f"{t2:.2f}%")
        c3.metric("Spread 2Y-10Y", f"{t10 - t2:.2f}", delta_color="inverse")

    # --- CATEGORIA 5: COMMODITIES ---
    with st.expander("⛽ Commodities Estratégicas"):
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Petróleo Brent", f"$ {data['commodities']['brent']:.2f}")
        c2.metric("Ouro (Oz)", f"$ {data['commodities']['gold']:,.2f}")
        c3.metric("Cobre", f"$ {data['commodities']['copper']:.2f}")
        c4.metric("CRB Index", "275.4", "Fixed")