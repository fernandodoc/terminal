import streamlit as st

def render_news_portal():
    """Renderiza os cards de acesso aos jornais e portais financeiros."""
    
    # Estilização local para os cards de notícias
    st.markdown("""
        <style>
        .news-card {
            background-color: #161b22;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #30363d;
            text-align: center;
            height: 120px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            transition: 0.3s;
            margin-bottom: 15px;
        }
        .news-card:hover {
            border-color: #58a6ff;
            background-color: #1f2937;
        }
        .news-link {
            text-decoration: none;
            color: #58a6ff;
            font-weight: bold;
            font-size: 18px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.subheader("📰 Sala de Análise")
    st.caption("O ponto de convergência entre informação, análise e capital.")
    
    # --- SEÇÃO NACIONAL ---
    # --- SEÇÃO FUNDAMENTOS ---
    st.markdown("#### Informações e fundamentos")
    br_col1, br_col2, br_col3, br_col4 = st.columns(4)
    
    br_news = [
        ("OpenBB", "https://openbb.co/solutions/"),
        ("Fundamentus", "https://www.fundamentus.com.br/"),
        ("B3", "https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm"),
        ("CVM", "https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAb.aspx?TipoConsult=c"),
        ("Data World Bank", "https://data360.worldbank.org/en/economy/BRA"),
        ("StatusInvest", "https://statusinvest.com.br/"),
        ("Investidor10", "https://investidor10.com.br/"),
        ("ADVFN", "https://br.advfn.com/"),
        ("Investing BR", "https://br.investing.com/equities"),
        ("Economatica", "https://www.economatica.com/"),
        ("Valor Data", "https://valor.globo.com/valor-data/"),
        ("InvestSite", "https://www.investsite.com.br/"),
        ("Instituto Assaf", "https://www.institutoassaf.com.br/"),
        ("USA Census Bureau", "https://www.census.gov/econ/qfr/index.html")
    ]

    cols = [br_col1, br_col2, br_col3, br_col4]
    for i, (name, url) in enumerate(br_news):
        with cols[i % 4]:
            st.markdown(f"""
                <div class="news-card">
                    <a href="{url}" target="_blank" class="news-link">{name}</a>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    # --- estruturando
    st.markdown("#### Brasil")
    br_col1, br_col2, br_col3, br_col4 = st.columns(4)
    
    br_news = [
        ("InfoMoney", "https://www.infomoney.com.br/"),
        ("Valor Econômico", "https://valor.globo.com/"),
        ("Money Times", "https://www.moneytimes.com.br/"),
        ("InvestNews", "https://investnews.com.br/"),
        ("Investing BR", "https://br.investing.com/"),
        ("bloomberg Línea", "https://www.bloomberglinea.com.br"),
        ("CNN Money", "https://www.cnnbrasil.com.br/money/")
    ]

    cols = [br_col1, br_col2, br_col3, br_col4]
    for i, (name, url) in enumerate(br_news):
        with cols[i % 4]:
            st.markdown(f"""
                <div class="news-card">
                    <a href="{url}" target="_blank" class="news-link">{name}</a>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    # --- estruturando
    # --- SEÇÃO INTERNACIONAL ---
    st.markdown("#### 🌎 Global")
    int_col1, int_col2, int_col3, int_col4 = st.columns(4)
    
    int_news = [
        ("Financial Times", "https://www.ft.com/"),
        ("Bloomberg", "https://www.bloomberg.com/markets"),
        ("The Economist", "https://www.economist.com/"),
        ("MarketWatch", "https://www.marketwatch.com/"),
        ("Investopedia", "https://www.investopedia.com/"),
        ("Reuters", "https://www.reuters.com/"),
        ("NY Times Finance", "https://www.nytimes.com/"),
        ("Barron's", "https://www.barrons.com/"),
        ("Investor's Business Daily", "https://www.investors.com/")
    ]

    cols_int = [int_col1, int_col2, int_col3, int_col4]
    for i, (name, url) in enumerate(int_news):
        with cols_int[i % 4]:
            st.markdown(f"""
                <div class="news-card">
                    <a href="{url}" target="_blank" class="news-link">{name}</a>
                </div>

            """, unsafe_allow_html=True)


