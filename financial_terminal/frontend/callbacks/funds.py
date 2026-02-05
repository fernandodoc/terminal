import streamlit as st
from backend.api.funds import get_fund_data

def render_funds_analysis():
    # Estilização para métricas e títulos
    st.markdown("""
        <style>
        [data-testid="stMetricValue"] { font-size: 1.8rem; color: #fbbf24; }
        .fund-header {
            background: linear-gradient(90deg, #1e293b 0%, #0f172a 100%);
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #fbbf24;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("### 🏢 Central de Inteligência de Fundos")
    st.caption("Análise institucional de FIIs e ETFs listados na B3.")

    # Sidebar ou Coluna estreita para busca (Melhor UX que formulário largo)
    with st.container():
        col_search, col_empty = st.columns([1, 2])
        with col_search:
            ticker = st.text_input("Ticker do Ativo", value="HGLG11", help="Ex: HGLG11, IVVB11, XPLG11").upper().strip()
            # Botão fora do form para resposta mais rápida ao clique
            btn_analisar = st.button("🔍 Analisar Ativo", use_container_width=True)

    if btn_analisar or ticker:
        with st.spinner(f"Processando dados de {ticker}..."):
            try:
                data = get_fund_data(ticker)
                
                if not data or "Erro" in data:
                    st.error(f"⚠️ {data.get('Erro', 'Erro inesperado ao buscar dados.')}")
                    st.info("Dica: Verifique se o ticker está correto ou tente novamente em instantes.")
                    return

                # Header do Fundo
                st.markdown(f"""
                    <div class="fund-header">
                        <h2 style='margin:0; color:white;'>{ticker} | {data.get('Nome', 'Fundo Selecionado')}</h2>
                        <span style='color:#94a3b8;'>Dados atualizados via Terminal de Elite</span>
                    </div>
                """, unsafe_allow_html=True)

                # Grid de Métricas Principais
                m1, m2, m3, m4 = st.columns(4)
                
                # Cotação com Delta (Variação) se disponível
                m1.metric("Cotação Atual", f"R$ {data['Cotação']:.2f}")
                
                # Dividend Yield com lógica de cor
                dy = data.get('DY', 0)
                m2.metric("Dividend Yield (12m)", f"{dy:.2f}%" if dy else "N/A")
                
                # P/VP com interpretação visual
                pvp = data.get('P/VP', 0)
                delta_pvp = "Desconto" if pvp < 1 else "Ágio" if pvp > 1 else "Preço Justo"
                m3.metric("P/VP", f"{pvp:.2f}" if pvp else "N/A", delta=delta_pvp, delta_color="normal")
                
                # Performance
                perf = data.get('Performance_12m', 0)
                m4.metric("Performance (12m)", f"{perf:.2f}%")

                st.markdown("---")

                # Seção de Detalhes e Tese
                tab_resumo, tab_tecnico = st.tabs(["📖 Tese de Investimento", "📊 Indicadores Técnicos"])
                
                with tab_resumo:
                    st.markdown("#### Resumo Operacional")
                    st.write(data.get('Resumo', 'Descrição não disponível no momento.'))
                
                with tab_tecnico:
                    st.write("Dados detalhados de liquidez e composição de carteira serão exibidos aqui.")

            except Exception as e:
                st.error("Ocorreu um erro na comunicação com a base de dados.")
                st.caption(f"Detalhes técnicos: {str(e)}")

    st.markdown("---")
    st.caption("⚙️ Fonte: B3 / Provedores de Dados de Mercado via API.")
