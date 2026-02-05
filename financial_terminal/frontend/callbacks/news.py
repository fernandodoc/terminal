import streamlit as st

def render_news_portal():
    """Renderiza o Portal de Inteligência com UI/UX de alta performance."""
    
    # CSS Avançado: Estilo Profissional com Glassmorphism leve
    st.markdown("""
        <style>
        .news-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 12px;
            padding: 10px 0px;
        }
        .news-card {
            background: linear-gradient(145deg, #1e293b, #0f172a);
            padding: 18px;
            border-radius: 8px;
            border: 1px solid #334155;
            text-align: center;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 80px;
            text-decoration: none !important;
        }
        .news-card:hover {
            border-color: #fbbf24; /* Dourado para alinhar com seu branding de elite */
            transform: translateY(-3px);
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);
            background: #1e293b;
        }
        .news-link {
            color: #f1f5f9 !important;
            font-weight: 500;
            font-size: 15px;
            text-decoration: none !important;
            font-family: 'Inter', sans-serif;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("📰 Sala de Inteligência")
    st.markdown("""
        <p style='color: #94a3b8; font-size: 1.1rem; margin-top: -15px;'>
            Acesso direto às principais fontes de dados e terminais de notícias globais.
        </p>
    """, unsafe_allow_html=True)

    # --- ORGANIZAÇÃO EM TABS (Melhor UX para não poluir a tela) ---
    tab_fund, tab_br, tab_global = st.tabs([
        "🔍 Fundamentos & Dados", 
        "🇧🇷 Terminais Brasil", 
        "🌎 Terminais Globais"
    ])

    # --- TAB 1: FUNDAMENTOS ---
    with tab_fund:
        st.markdown("<div class='news-grid'>", unsafe_allow_html=True)
        fund_data = [
            ("OpenBB", "https://openbb.co/solutions/"),
            ("StatusInvest", "https://statusinvest.com.br/"),
            ("Fundamentus", "https://www.fundamentus.com.br/"),
            ("Brasil Indicadores", "https://brasilindicadores.com.br/"),
            ("Instituto Assaf", "https://www.institutoassaf.com.br/"),
            ("ADVFN", "https://br.advfn.com/"),
            ("Investidor10", "https://investidor10.com.br/"),
            ("CVM", "https://cvmweb.cvm.gov.br/"),
            ("B3 Empresas", "https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm"),
            ("World Bank", "https://data360.worldbank.org/en/economy/BRA"),
            ("Economatica", "https://www.economatica.com/"),
            ("Valor Data", "https://valor.globo.com/valor-data/"),
            ("USA Census", "https://www.census.gov/econ/qfr/index.html"),
            ("Dividend Kings", "https://www.dividend.com/dividend-kings/"),
            ("Trading Economics", "https://tradingeconomics.com/api/")   
        ]
        
        for name, url in fund_data:
            st.markdown(f"""
                <a href="{url}" target="_blank" class="news-card">
                    <span class="news-link">{name}</span>
                </a>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- TAB 2: BRASIL ---
    with tab_br:
        st.markdown("<div class='news-grid'>", unsafe_allow_html=True)
        br_news = [
            ("Valor Econômico", "https://valor.globo.com/"),
            ("Bloomberg Línea", "https://www.bloomberglinea.com.br"),
            ("InfoMoney", "https://www.infomoney.com.br/"),
            ("Money Times", "https://www.moneytimes.com.br/"),
            ("CNN Money", "https://www.cnnbrasil.com.br/money/"),
            ("InvestNews", "https://investnews.com.br/"),
            ("Investing BR", "https://br.investing.com/")
        ]
        for name, url in br_news:
            st.markdown(f"""
                <a href="{url}" target="_blank" class="news-card">
                    <span class="news-link">{name}</span>
                </a>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- TAB 3: GLOBAL ---
    with tab_global:
        st.markdown("<div class='news-grid'>", unsafe_allow_html=True)
        int_news = [
            ("Financial Times", "https://www.ft.com/"),
            ("Bloomberg", "https://www.bloomberg.com/markets"),
            ("Reuters", "https://www.reuters.com/"),
            ("MarketWatch", "https://www.marketwatch.com/"),
            ("The Economist", "https://www.economist.com/"),
            ("Barron's", "https://www.barrons.com/"),
            ("Investopedia", "https://www.investopedia.com/"),
            ("NY Times Finance", "https://www.nytimes.com/section/business")
        ]
        for name, url in int_news:
            st.markdown(f"""
                <a href="{url}" target="_blank" class="news-card">
                    <span class="news-link">{name}</span>
                </a>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.caption("🔒 **Nota de Segurança:** Todos os links abrem em abas externas para garantir a integridade da sua sessão atual.")





