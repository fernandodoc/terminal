import streamlit as st
from backend.api.funds import get_fund_data, get_fund_by_cnpj

def render_funds_analysis():
    st.markdown("### 🏢 Central de Inteligência de Fundos")
    
    tab_listados, tab_cnpj = st.tabs(["📊 FIIs e ETFs (Ticker)", "🏦 Fundos de Investimento (CNPJ)"])

    with tab_listados:
        render_listados_section()

    with tab_cnpj:
        st.write("Consulte dados oficiais de lâmina e performance via base da CVM.")
        
        with st.container():
            col_search, _ = st.columns([1.5, 2])
            with col_search:
                cnpj_input = st.text_input("Digite o CNPJ do Fundo", placeholder="00.000.000/0000-00")
                btn_cnpj = st.button("🔍 Consultar CNPJ", use_container_width=True)

        if btn_cnpj and cnpj_input:
            with st.spinner("Acessando base da CVM..."):
                data_cnpj = get_fund_by_cnpj(cnpj_input)
                
                if "Erro" in data_cnpj:
                    st.error(data_cnpj["Erro"])
                else:
                    st.markdown(f"""
                        <div style="background-color: #1e293b; padding: 20px; border-radius: 10px; border-left: 5px solid #3b82f6; margin-bottom: 20px;">
                            <h3 style='margin:0; color:white;'>{data_cnpj['razao_social']}</h3>
                            <p style='color: #94a3b8; margin:0;'>CNPJ: {cnpj_input} | Classe: {data_cnpj['classe']}</p>
                        </div>
                    """, unsafe_allow_html=True)

                    c1, c2, c3 = st.columns(3)
                    c1.metric("Patrimônio Líquido", f"R$ {data_cnpj['pl_estrategia']:,.2f}")
                    c2.metric("Cota Atual", f"R$ {data_cnpj['valor_cota']:.4f}")
                    c3.metric("Investidores", f"{data_cnpj['num_cotistas']:,}")

                    with st.expander("📝 Detalhes do Fundo"):
                        st.write(f"**Gestor:** {data_cnpj['gestor']}")
                        st.write(f"**Administrador:** {data_cnpj['administrador']}")
                        st.write(f"**Taxa de Administração:** {data_cnpj['taxa_adm']}")

def render_listados_section():
    ticker = st.text_input("Ticker do Ativo", value="HGLG11", help="Ex: HGLG11, IVVB11, KNCR11").upper().strip()
    
    if st.button("Analisar Ticker", key="btn_ticker", use_container_width=True):
        with st.spinner(f"Buscando dados de {ticker}..."):
            data = get_fund_data(ticker)
            
            if "Erro" in data:
                st.error(data["Erro"])
            else:
                st.markdown(f"""
                    <div style="background-color: #1e293b; padding: 20px; border-radius: 10px; border-left: 5px solid #fbbf24; margin-bottom: 20px;">
                        <h3 style='margin:0; color:white;'>{data['Nome']}</h3>
                    </div>
                """, unsafe_allow_html=True)

                c1, c2, c3, c4 = st.columns(4)
                
                # --- Cotação ---
                val_cotacao = data.get('Cotação', 0)
                c1.metric("Cotação", f"R$ {val_cotacao:.2f}" if isinstance(val_cotacao, (int, float)) else "N/A")
                
                # --- Dividend Yield (Onde dava o erro) ---
                val_dy = data.get('DY', 0)
                c2.metric("DY (12m)", f"{val_dy:.2f}%" if isinstance(val_dy, (int, float)) else "N/A")
                
                # --- P/VP ---
                val_pvp = data.get('P/VP', 0)
                c3.metric("P/VP", f"{val_pvp:.2f}" if isinstance(val_pvp, (int, float)) else "N/A")
                
                # --- Performance ---
                val_perf = data.get('Performance_12m', 0)
                c4.metric("Perf. 12m", f"{val_perf:.2f}%" if isinstance(val_perf, (int, float)) else "N/A")
                
                with st.expander("📖 Tese de Investimento"):
                    st.write(data.get('Resumo', 'Resumo não disponível.'))
