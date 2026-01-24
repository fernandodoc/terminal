import streamlit as st

def render_calculadora_cidadao():
    # Estilização para o módulo
    st.markdown("""
        <style>
        .calc-header {
            background-color: #161b22;
            padding: 25px;
            border-radius: 10px;
            border-left: 5px solid #f3d007; /* Amarelo BCB */
            margin-bottom: 20px;
        }
        .info-box {
            background-color: #1c2128;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #30363d;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- CABEÇALHO ---
    st.markdown("""
        <div class="calc-header">
            <h1>🏛️ Calculadora do Cidadão</h1>
            <p style='font-size: 1.1rem;'>Acesso direto à ferramenta oficial do Banco Central do Brasil para correções financeiras.</p>
        </div>
    """, unsafe_allow_html=True)

    # --- O QUE É ---
    st.markdown("### O que é esta ferramenta?")
    st.write("""
    A **Calculadora do Cidadão** é um aplicativo interativo, mantido pelo **Banco Central**, que permite simular situações do cotidiano financeiro. 
    Para um investidor de alto nível, ela é essencial para validar:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        * **Correção de Valores:** Atualização de montantes por índices como IPCA, IGPM, SELIC e TR.
        * **Investimentos:** Simulação de depósitos regulares e rendimentos de poupança.
        """)
    with col2:
        st.markdown("""
        * **Crédito e Financiamento:** Cálculo de prestações fixas e valor financiado.
        * **Poder de Compra:** Visualização real do impacto inflacionário em patrimônios históricos.
        """)

    st.markdown("---")

    # --- BOTÃO DE REDIRECIONAMENTO ---
    st.markdown("""
        <div class="info-box" style="text-align: center;">
            <h4>Utilize o simulador oficial para correções por índices</h4>
            <p>Você será direcionado para o portal do Banco Central para realizar cálculos com fé pública.</p>
    """, unsafe_allow_html=True)
    
    # Botão Streamlit para o link oficial
    url_bcb = "https://www3.bcb.gov.br/CALCIDADAO/publico/corrigirPorIndice.do?method=corrigirPorIndice"
    st.link_button("Ir para Calculadora do Cidadão (BCB)", url_bcb, type="primary")
    
    st.markdown("</div>", unsafe_allow_html=True)

    st.info("💡 **Dica do Especialista:** Use esta ferramenta para entender porque manter capital parado em conta corrente destrói o patrimônio no longo prazo devido ao IPCA.")