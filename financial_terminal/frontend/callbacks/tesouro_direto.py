import streamlit as st

def render_tesouro_direto():
    # Estilização Profissional
    st.markdown("""
        <style>
        .tesouro-header {
            background: linear-gradient(90deg, #003366 0%, #004080 100%);
            padding: 30px;
            border-radius: 12px;
            border-left: 8px solid #ffcc00; /* Dourado Tesouro */
            margin-bottom: 25px;
        }
        .concept-card {
            background-color: #1c2128;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #30363d;
            height: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- CABEÇALHO ---
    st.markdown("""
        <div class="tesouro-header">
            <h1 style='color: white;'>🏦 Investimento em Títulos Públicos</h1>
            <p style='color: #e6e6e6; font-size: 1.1rem;'>Acesse a plataforma oficial do Tesouro Nacional para garantir o Risco Soberano do seu portfólio.</p>
        </div>
    """, unsafe_allow_html=True)

    # --- EXPLICAÇÃO TÉCNICA ---
    st.markdown("### O que é o Tesouro Direto?")
    st.write("""
    O Tesouro Direto é um programa do Tesouro Nacional desenvolvido para permitir a venda de títulos públicos federais para pessoas físicas. 
    Ao adquirir um título, você está emprestando dinheiro para o Estado Brasileiro em troca de uma rentabilidade acordada.
    """)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="concept-card">
            <h4>🛡️ Segurança</h4>
            <p>Considerado o investimento de <b>menor risco</b> da economia, por ser garantido pelo Governo Federal.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="concept-card">
            <h4>💧 Liquidez</h4>
            <p>O Tesouro Nacional garante a <b>recompra diária</b> dos títulos, permitindo o resgate quando necessário.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="concept-card">
            <h4>📈 Variedade</h4>
            <p>Opções <b>Pós-fixadas</b> (Selic), <b>Prefixadas</b> ou <b>Híbridas</b> (IPCA+) para cada objetivo.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --- DIRECIONAMENTO ---
    st.markdown("### 🚀 Operacionalização")
    st.info("""
    Para realizar a compra ou venda de títulos, você será redirecionado para o portal oficial do **Tesouro Direto**. 
    Lá, você poderá simular rentabilidades e conferir as taxas atualizadas do dia.
    """)

    # Botão de Acesso Direto
    url_tesouro = "https://www.tesourodireto.com.br/"
    st.link_button("Ir para o Portal do Tesouro Direto", url_tesouro, type="primary", use_container_width=True)

    st.markdown("---")
    st.caption("⚠️ **Nota do Especialista:** Títulos com vencimento longo estão sujeitos à **Marcação a Mercado**. Consulte um especialista em investimentos para entender o impacto da curva de juros no seu patrimônio atual. Se precisar da minha ajuda, conte comigo. Fernando (ANCORD, C-PRO I, C-PRO R).")