import streamlit as st
from backend.api.funds import get_fund_data

@st.cache_data(ttl=3600)
def render_funds_analysis():
    st.markdown("### 🏢 Central de Análise de Fundos (B3)")
    st.info("Para fundos imobiliários e ETFs, utilize o Ticker oficial (ex: HGLG11, IVVB11).")

    with st.form("fund_form"):
        ticker = st.text_input("Digite o Ticker", value="HGLG11").upper()
        submit = st.form_submit_button("Analisar Fundo")

    if submit:
        with st.spinner("Buscando dados institucionais..."):
            data = get_fund_data(ticker)
            
        if "Erro" in data:
            st.error(data["Erro"])
        else:
            st.subheader(f"{data['Nome']}")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Cotação", f"R$ {data['Cotação']:.2f}")
            
            dy = data['DY']
            c2.metric("DY (12m)", f"{dy:.2f}%" if isinstance(dy, float) else "N/A")
            
            pvp = data['P/VP']
            c3.metric("P/VP", f"{pvp:.2f}" if isinstance(pvp, (float, int)) else "N/A")
            
            c4.metric("Perf. 12m", f"{data['Performance_12m']:.2f}%")
            
            with st.expander("📖 Tese de Investimento"):

                st.write(data['Resumo'])
