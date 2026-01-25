import streamlit as st

def render_education_module():
    st.markdown("""
        <style>
        .edu-header {
            background: linear-gradient(90deg, #0f172a 0%, #1e293b 100%);
            padding: 30px;
            border-radius: 12px;
            border-left: 8px solid #3b82f6;
            margin-bottom: 25px;
        }
        .edu-card {
            background-color: #1c2128;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #30363d;
            height: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="edu-header">
            <h1 style='color: white;'>🎓 Hub de Educação e Estratégia</h1>
            <p style='color: #94a3b8; font-size: 1.1rem;'>Conceitos avançados para a gestão de grandes patrimônios.</p>
        </div>
    """, unsafe_allow_html=True)

    # --- TRÊS PILARES DO INVESTIDOR DE ELITE ---
    st.subheader("💡 Pilares do Wealth Management")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="edu-card">
            <h4>🧠 Finanças Comportamentais</h4>
            <p>Entenda como o viés da <b>Aversão à Perda</b> e o <b>Efeito Manada</b> podem destruir o patrimônio em momentos de volatilidade.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="edu-card">
            <h4>⚖️ Asset Allocation</h4>
            <p>A estratégia mais importante. 90% do retorno de longo prazo vem da alocação correta entre classes de ativos, não do <i>stock picking</i>.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="edu-card">
            <h4>🛡️ Gestão de Risco</h4>
            <p>Aprenda a diferença entre <b>Risco de Mercado</b> e <b>Risco de Liquidez</b>. Para grandes volumes, a saída é tão importante quanto a entrada.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --- SEÇÃO DE CONTEÚDO EXPANSÍVEL ---
    st.subheader("📚 Guia de Estratégias")

    with st.expander("📊 A Curva de Juros e seu Investimento"):
        st.write("""
        Entender a curva de juros (Yield Curve) é o que diferencia o investidor profissional do amador. 
        Quando a curva 'empina', o mercado espera inflação e juros altos. Quando ela 'achata', pode indicar recessão.
        """)
        st.info("Dica: Use o módulo de Títulos Públicos para ver como a marcação a mercado reage a essas mudanças.")

    with st.expander("📉 Ciclos de Mercado (Howard Marks)"):
        st.write("""
        "Não podemos prever o futuro, mas podemos nos preparar para o ciclo". 
        Aprender a identificar se estamos no topo ou no fundo do ciclo ajuda a evitar aportes em momentos de euforia excessiva.
        """)
    
    # --- Seção Links Cursos e Educação Financeira
    def render_education_module():
    # ... (mantenha seu código anterior de cabeçalho e cards)

        st.markdown("---")
    st.subheader("🔗 Biblioteca de Recursos e Cursos Oficiais")
    st.write("Acesse as principais plataformas de educação financeira e instituições do mercado:")

    # Organização em Colunas para melhor visualização
    col_links1, col_links2 = st.columns(2)

    with col_links1:
        st.markdown("#### 🏛️ Institucionais e Reguladores")
        st.link_button("🎓 Cursos B3", "https://edu.b3.com.br/", use_container_width=True)
        st.link_button("🏦 Cursos Banco Central", "https://www.bcb.gov.br/cidadaniafinanceira/cursos", use_container_width=True)
        st.link_button("📚 Livros Oficiais CVM", "https://www.gov.br/investidor/pt-br/educacional/publicacoes-educacionais/livros-cvm/teste", use_container_width=True)
        st.link_button("🛡️ Portal do Investidor (Gov)", "https://www.gov.br/investidor/pt-br/investir", use_container_width=True)
        st.link_button("🏫 Educação Financeira na Escola", "https://www.edufinanceiranaescola.gov.br/", use_container_width=True)
        st.link_button("🏛️ Museu da Bolsa (MUB3)", "https://mub3.org.br/", use_container_width=True)

    with col_links2:
        st.markdown("#### 📈 Estratégia e Prática")
        st.link_button("💰 Guia Tesouro Direto", "https://www.tesourodireto.com.br/como-investir/conteudo", use_container_width=True)
        st.link_button("🌍 BlackRock: Construção de Portfólio", "https://www.blackrock.com/br/educacao/portfolio-construcao", use_container_width=True)
        st.link_button("🔍 Tipos de Investimentos (CVM)", "https://www.gov.br/investidor/pt-br/investir/tipos-de-investimentos", use_container_width=True)
        st.link_button("📖 Educação Financeira CVM", "https://www.gov.br/cvm/pt-br/assuntos/educacao", use_container_width=True)
        st.link_button("🌐 OpenLearn (Cursos Gratuitos Internacionais)", "https://www.open.edu/openlearn/free-courses/full-catalogue", use_container_width=True)

    st.markdown("---")
    st.info("💡 **Dica do Especialista:** O conhecimento é o único ativo que não sofre marcação a mercado.")

    # --- FOOTER ---
    st.markdown("---")
    st.caption("ℹ️ Este hub é atualizado regularmente com teses de investimento e conceitos de economia moderna.")
