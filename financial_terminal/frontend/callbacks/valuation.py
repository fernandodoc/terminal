import streamlit as st
import math
from backend.api.valuation import get_fundamentus_data

def render_valuation_analysis():
    st.markdown("### 🔍 Terminal de Valuation & Fundamentos")
    st.info("📊 **Data Engine:** Conexão direta com a base de dados do Fundamentus.")
    
    with st.form("valuation_form"):
        col1, col2 = st.columns([3, 1])
        ticker = col1.text_input("Digite o Ticker (ex: MGLU3, VALE3)", value="MGLU3").upper()
        submit = st.form_submit_button("Executar Análise")

    if submit:
        with st.spinner(f"Processando dados de {ticker}..."):
            data = get_fundamentus_data(ticker)
        
        if "Erro" in data:
            st.error(data["Erro"])
        else:
            # --- CABEÇALHO ---
            st.subheader(f"📊 {data.get('Papel')} | {data.get('Empresa')}")
            st.caption(f"Setor: {data.get('Setor')} | Subsetor: {data.get('Subsetor')} | Balanço: {data.get('Últ balanço processado')}")

            # --- LINHA 1: INDICADORES DE PREÇO (MARKET) ---
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Cotação", f"R$ {data.get('Cotação')}")
            m2.metric("P/L", data.get('P/L'))
            m3.metric("P/VP", data.get('P/VP'))
            m4.metric("Div. Yield", data.get('Div. Yield'))

            # --- LINHA 2: RENTABILIDADE E EFICIÊNCIA ---
            st.markdown("---")
            e1, e2, e3, e4 = st.columns(4)
            e1.metric("ROE", data.get('ROE'))
            e2.metric("ROIC", data.get('ROIC'))
            e3.metric("Margem Líquida", data.get('Marg. Líquida'))
            e4.metric("Margem EBIT", data.get('Marg. EBIT'))

            # --- SEÇÃO ESPECIAL: VALOR INTRÍNSECO (O DIFERENCIAL DO ADVISOR) ---
            st.markdown("### 💎 Estimativas de Valor Justo")
            v_col1, v_col2 = st.columns(2)

            # Lógica para cálculo de Graham
            try:
                lpa = float(data.get('LPA').replace(',', '.'))
                vpa = float(data.get('VPA').replace(',', '.'))
                cotacao_atual = float(data.get('Cotação').replace(',', '.'))
                
                # Fórmula de Graham: Raiz(22.5 * LPA * VPA)
                if lpa > 0 and vpa > 0:
                    preco_graham = math.sqrt(22.5 * lpa * vpa)
                    upside = ((preco_graham / cotacao_atual) - 1) * 100
                    v_col1.metric("Preço Justo (Graham)", f"R$ {preco_graham:.2f}", f"{upside:.2f}% Upside")
                else:
                    v_col1.warning("Graham: Incalculável (LPA ou VPA negativo)")
            except:
                v_col1.error("Erro no cálculo de Graham")

            # Lógica para Método de Bazin
            try:
                dy_text = data.get('Div. Yield').replace('%', '').replace(',', '.')
                dy_decimal = float(dy_text) / 100
                # Bazin sugere: (Dividendo por ação nos últimos 12m) / 0.06
                # Vamos estimar o dividendo pago: DY * Cotação
                dpa = dy_decimal * cotacao_atual
                if dpa > 0:
                    preco_bazin = dpa / 0.06
                    v_col2.metric("Preço Teto (Bazin)", f"R$ {preco_bazin:.2f}", help="Baseado em um Yield de 6%")
                else:
                    v_col2.info("Bazin: Sem dividendos relevantes")
            except:
                v_col2.error("Erro no cálculo de Bazin")

            # --- DADOS DE BALANÇO (EXPANDER) ---
            with st.expander("📂 Detalhes do Balanço Patrimonial"):
                b1, b2, b3 = st.columns(3)
                b1.write(f"**Patrimônio Líquido:** R$ {data.get('Patrim. Líq')}")
                b1.write(f"**Ativo Total:** R$ {data.get('Ativo')}")
                
                b2.write(f"**Dívida Bruta:** R$ {data.get('Dív. Bruta')}")
                b2.write(f"**Dívida Líquida:** R$ {data.get('Dív. Líquida')}")
                
                b3.write(f"**Valor de Mercado:** R$ {data.get('Valor de mercado')}")
                b3.write(f"**Valor da Firma (EV):** R$ {data.get('Valor da firma')}")

            # --- OSCILAÇÕES ---
            st.markdown("##### 📉 Desempenho Histórico")
            o1, o2, o3, o4, o5 = st.columns(5)
            o1.metric("2025", data.get('2025', 'N/A'))
            o2.metric("2024", data.get('2024', 'N/A'))
            o3.metric("2023", data.get('2023', 'N/A'))
            o4.metric("2022", data.get('2022', 'N/A'))
            o5.metric("2021", data.get('2021', 'N/A'))