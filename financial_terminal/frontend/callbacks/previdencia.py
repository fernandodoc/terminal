import streamlit as st

def render_previdencia():
    # Estilização Profissional
    st.markdown("""
        <style>
        .prev-header {
            background: linear-gradient(90deg, #1d2128 0%, #24292e 100%);
            padding: 30px;
            border-radius: 12px;
            border-left: 8px solid #2ea44f; /* Verde Previdência */
            margin-bottom: 25px;
        }
        .info-card {
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
        <div class="prev-header">
            <h1 style='color: white;'>🛡️ Previdência e Planejamento Sucessório</h1>
            <p style='color: #e6e6e6; font-size: 1.1rem;'>Estratégias de blindagem patrimonial e diferimento fiscal para o longo prazo.</p>
        </div>
    """, unsafe_allow_html=True)

    # --- PILARES DA PREVIDÊNCIA DE ELITE ---
    st.markdown("### Por que incluir Previdência no Portfólio?")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="info-card">
            <h4>📈 Diferimento Fiscal</h4>
            <p>No PGBL, você pode deduzir até 12% da sua renda bruta tributável, adiando o imposto e investindo o que seria pago ao Leão.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="info-card">
            <h4>⚰️ Sucessão Ágil</h4>
            <p>Os recursos de previdência não entram em inventário, garantindo liquidez imediata aos herdeiros (em média 15 a 30 dias).</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="info-card">
            <h4>📉 Tributação Regressiva</h4>
            <p>Após 10 anos, a alíquota de IR cai para apenas <b>10%</b>, a menor do mercado financeiro brasileiro.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --- SIMULADOR RÁPIDO DE CONCEITOS ---
    st.subheader("🔍 Guia de Escolha Estratégica")
    
    tab1, tab2 = st.tabs(["📊 PGBL vs VGBL", "📑 Progressiva vs Regressiva"])
    
    with tab1:
        col_p, col_v = st.columns(2)
        with col_p:
            st.success("**PGBL (Plano Gerador de Benefício Livre)**")
            st.write("- **Indicado para:** Quem faz declaração completa de IR.")
            st.write("- **Benefício:** Abatimento de até 12% da renda bruta.")
            st.write("- **Incidência de IR:** Sobre o valor total resgatado.")
        with col_v:
            st.info("**VGBL (Vida Gerador de Benefício Livre)**")
            st.write("- **Indicado para:** Isentos, declaração simplificada ou quem já atingiu os 12% no PGBL.")
            st.write("- **Benefício:** Funciona como um seguro de vida com sobrevivência.")
            st.write("- **Incidência de IR:** Apenas sobre o rendimento.")

    with tab2:
        st.markdown("""
        
        """)
        st.write("**Dica de Elite:** A tabela **Regressiva** é o grande trunfo para quem busca independência financeira, pois premia o investidor de longo prazo com a menor carga tributária possível.")

    st.markdown("---")
    
    # --- CTA E LINKS ---
    st.markdown("### 🚀 Próximos Passos")
    st.write("A escolha do fundo de previdência deve levar em conta a estratégia de alocação (Renda Fixa, Multimercado ou Ações).")
    


    st.caption("⚠️ **Aviso Legal:** Previdência Privada é um investimento de longo prazo. Resgates antecipados na tabela regressiva podem gerar alíquotas de até 35%. Consulte sempre seu especialista certificado. Se precisar da minha ajuda, conte comigo. Fernando (ANCORD, C-PRO I, C-PRO R).")