import streamlit as st

def apply_custom_style():
    """
    Aplica o design 'Dark Professional' ao terminal.
    Focado em reduzir distrações e destacar dados.
    """
    st.markdown("""
        <style>
        /* Fundo principal */
        .stApp {
            background-color: #0b0e14;
            color: #e0e0e0;
        }
        
        /* Sidebar customizada */
        [data-testid="stSidebar"] {
            background-color: #161b22;
            border-right: 1px solid #30363d;
        }

        /* Botões de navegação lateral */
        .stButton>button {
            width: 100%;
            border-radius: 5px;
            background-color: #1f2937;
            color: white;
            border: 1px solid #30363d;
            transition: 0.3s;
        }

        .stButton>button:hover {
            border-color: #58a6ff;
            color: #58a6ff;
        }

        /* Estilização de métricas */
        [data-testid="stMetricValue"] {
            font-size: 24px;
            color: #58a6ff;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    """Cabeçalho padrão para todas as páginas"""
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("💎 OpenMacroBase")
        st.caption("Inteligência financeira para o seu dia a dia")
    with col2:
        st.write("") # Espaçador

        st.status("Market Open", state="running")
