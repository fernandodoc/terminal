import streamlit as st
from backend.api.mailer import enviar_dados_ao_especialista

def render_portfolio_vision():
    # --- ESTILIZAÇÃO (CSS) ---
    st.markdown("""
        <style>
        .portfolio-header {
            background: linear-gradient(90deg, #161b22 0%, #0d1117 100%);
            padding: 40px;
            border-radius: 15px;
            border-left: 8px solid #58a6ff;
            margin-bottom: 30px;
        }
        .contact-card {
            background-color: #1c2128;
            padding: 30px;
            border-radius: 10px;
            border: 1px solid #30363d;
            margin-top: 40px;
        }
        .highlight {
            color: #58a6ff;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- VISÃO ESTRATÉGICA ---
    st.markdown("""
        <div class="portfolio-header">
            <h1>💼 Gestão de Portfólio de Elite</h1>
            <p style='font-size: 1.2rem; line-height: 1.6;'>
                A construção de um patrimônio superior a <span class="highlight">R$ 300.000,00</span> exige mais do que a simples escolha de ativos. 
                Requer uma arquitetura financeira que equilibre <b>Otimização de Rentabilidade</b>, <b>Eficiência Fiscal</b> e a <b>Proteção de Legado</b>.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎯 O Tripé da Gestão Profissional")
        st.write("""
        1. **Eficiência Fiscal:** Minimizar o impacto tributário para acelerar o crescimento composto.
        2. **Blindagem Patrimonial:** Proteção contra riscos sistêmicos e jurisdicionais.
        3. **Transmissão de Legado:** Planejamento sucessório inteligente para evitar burocracia onerosa.
        """)

    with col2:
        st.markdown("### ⚖️ O Papel do Especialista")
        st.info("""
        Um profissional certificado atua como um filtro técnico, removendo o viés emocional e aplicando modelos matemáticos de fronteira eficiente.
        
        **A tecnologia fornece os dados, mas o estrategista fornece a direção.**
        """)

    st.markdown("---")

    # --- FORMULÁRIO DE CONTATO (DENTRO DA DIV ESTILIZADA) ---
    st.markdown("<div class='contact-card'>", unsafe_allow_html=True)
    st.subheader("🚀 Solicitar Diagnóstico de Portfólio")
    st.write("Agende uma consultoria técnica para estruturar sua carteira de forma profissional.")

    # Início do Formulário
    with st.form("contact_professional", clear_on_submit=False):
        c1, c2 = st.columns(2)
        nome = c1.text_input("Nome Completo")
        email = c2.text_input("E-mail Estratégico")
        
        c3, c4 = st.columns(2)
        telefone = c3.text_input("WhatsApp para Contato")
        faixa_patrimonial = c4.selectbox("Patrimônio Estimado", [
            "R$ 300k - R$ 1M", 
            "R$ 1M - R$ 5M", 
            "Acima de R$ 5M"
        ])
        
        mensagem = st.text_area("Objetivo Principal (ex: Sucessão, Renda, Alocação Global)")
        
        submit_contact = st.form_submit_button("Enviar Dados ao Especialista")
        
        if submit_contact:
            # Esse print VAI aparecer no seu log do Manage App se o botão funcionar
            print("🚀 BOTÃO PRESSIONADO: Iniciando processo de envio...") 
            
            if nome and email and telefone:
                dados_lead = {
                    "Nome": nome,
                    "Email": email,
                    "WhatsApp": telefone,
                    "Patrimonio": faixa_patrimonial,
                    "Mensagem": mensagem
                }
                
                with st.spinner("Conectando ao especialista..."):
                    sucesso = enviar_dados_ao_especialista(dados_lead)
                    # Outro print para rastrear o resultado
                    print(f"📊 RESULTADO DO ENVIO: {sucesso}")
                
                if sucesso:
                    st.success(f"Excelente, {nome}! Seus dados foram enviados.")
                    st.balloons()
                else:
                    st.error("Erro no envio. Verifique os logs do sistema.")
            else:
                st.error("Campos obrigatórios ausentes.")

