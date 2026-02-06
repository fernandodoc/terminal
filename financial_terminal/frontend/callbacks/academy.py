import streamlit as st

def render_academy_module():
    # Estilização para os cards de curso
    st.markdown("""
        <style>
        .course-card {
            background-color: #1c2128;
            padding: 25px;
            border-radius: 12px;
            border: 1px solid #30363d;
            height: 350px;
            transition: transform 0.3s ease;
        }
        .course-card:hover {
            border-color: #eab308;
            transform: translateY(-5px);
        }
        .level-badge {
            background-color: rgba(234, 179, 8, 0.1);
            color: #eab308;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
            border: 1px solid rgba(234, 179, 8, 0.3);
        }
        .course-title {
            font-size: 1.4rem;
            font-weight: bold;
            margin-top: 15px;
            color: #ffffff;
        }
        .course-desc {
            color: #8b949e;
            font-size: 0.95rem;
            margin-top: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🎓 Academia de Inteligência Financeira")
    st.write("Masterclasses exclusivas para investidores que buscam o próximo nível de sofisticação patrimonial.")

    # --- CATEGORIAS ---
    tabs = st.tabs(["🚀 Iniciando no High-End", "📊 Estratégias Avançadas", "🌍 Alocação Global & Sucessão"])

    with tabs[0]:
       # --- RESUMO ESTRATÉGICO DA TRILHA ---
        st.markdown("""
            <div style="background-color: rgba(88, 166, 255, 0.05); 
                        padding: 20px; 
                        border-radius: 10px; 
                        border-left: 4px solid #eab308; 
                        margin-bottom: 30px;">
                <p style="font-size: 1.1rem; line-height: 1.5; color: #c9d1d9; margin: 0;">
                    Não é sobre investir mais, é sobre <b>investir melhor</b>. Esta trilha foi desenhada para o investidor 
                    que saiu da fase de acumulação e agora precisa de uma <b>arquitetura de proteção e inteligência fiscal</b> 
                    para perpetuar seu capital.
                </p>
            </div>
        """, unsafe_allow_html=True)

        col_a, col_b = st.columns(2)
        col_c, col_d = st.columns(2)
        

        with col_a:
            st.markdown("""
                <div class="course-card">
                    <span class="level-badge">FUNDAMENTAL</span>
                    <div class="course-title">Arquitetura de Portfólio</div>
                    <p class="course-desc">
                        Aprenda os princípios de alocação de ativos usados por Family Offices. 
                        Entenda como balancear liquidez, risco e retorno para patrimônios acima de R$ 300k.
                    </p>
                    <hr style='border-color: #30363d'>
                    <small><b>Módulos:</b> 6 aulas • <b>Tempo:</b> 2h 30min</small>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Acessar Trilha de Arquitetura", key="c1"):
                st.info("Módulo disponível para clientes selecionados.")
        
        with col_b:
            st.markdown("""
                <div class="course-card">
                    <span class="level-badge">PSICOLOGIA</span>
                    <div class="course-title">Finanças Comportamentais</div>
                    <p class="course-desc">
                        Domine os vieses cognitivos que destroem o patrimônio. 
                        Aprenda a controlar o medo e a ganância através de métodos quantitativos.
                    </p>
                    <hr style='border-color: #30363d'>
                    <small><b>Módulos:</b> 5 aulas • <b>Tempo:</b> 3h 00min</small>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Acessar Comportamental", key="btn_comp"):
                st.info("Módulo disponível para clientes selecionados.")

        # Próxima linha de cursos
        st.write("") # Espaçador

        with col_c:
            st.markdown("""
                <div class="course-card">
                    <span class="level-badge">ESSENCIAL</span>
                    <div class="course-title">Eficiência Fiscal na Prática</div>
                    <p class="course-desc">
                        Onde os investidores mais perdem dinheiro: Impostos. 
                        Como otimizar o ganho líquido através de produtos isentos e estruturas inteligentes.
                    </p>
                    <hr style='border-color: #30363d'>
                    <small><b>Módulos:</b> 4 aulas • <b>Tempo:</b> 1h 45min</small>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Acessar Trilha Fiscal", key="c2"):
                st.info("Módulo disponível para clientes selecionados.")
        
        with col_d:
            st.markdown("""
                <div class="course-card">
                    <span class="level-badge">GESTÃO</span>
                    <div class="course-title">Organização Financeira de Alto Nível</div>
                    <p class="course-desc">
                        Gestão de fluxo de caixa complexo e consolidação de múltiplos ativos. 
                        Organize sua vida financeira para a máxima eficiência tributária.
                    </p>
                    <hr style='border-color: #30363d'>
                    <small><b>Módulos:</b> 4 aulas • <b>Tempo:</b> 2h 00min</small>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Acessar Organização", key="btn_org"):
                st.info("Módulo disponível para clientes selecionados.")

    with tabs[1]:
        st.markdown("### ⚙️ Métodos Quantitativos e Valuation")
        st.info("Conteúdo focado para investidores que desejam entender a matemática por trás das melhores escolhas.")
        # Adicionar cards de Valuation e Renda Fixa High-Yield aqui

    with tabs[2]:  # Nível 0
        st.markdown("### ✈️ Internacionalização de Capital") # Nível 1 (4 espaços)
        
        # Resumo Estratégico
        st.markdown("""
            <div style="background-color: rgba(88, 166, 255, 0.05); 
                        padding: 20px; 
                        border-radius: 10px; 
                        border-left: 4px solid #eab308; 
                        margin-bottom: 30px;">
                <p style="font-size: 1.1rem; line-height: 1.5; color: #c9d1d9; margin: 0;">
                    🛡️ <b>Preservação Transgeracional:</b> "A verdadeira gestão patrimonial transcende fronteiras 
                    e gerações. Esta trilha aborda a diversificação em moeda forte e as estruturas jurídicas 
                    necessárias para garantir que o seu <b>legado</b> seja transmitido com máxima eficiência e segurança."
                </p>
            </div>
        """, unsafe_allow_html=True) # Nível 1

        # Criando as colunas DENTRO da aba (Nível 1)
        col_e, col_f = st.columns(2)

        with col_e: # Nível 1
            st.markdown("""
                <div class="course-card">
                    <span class="level-badge">OFFSHORE</span>
                    <div class="course-title">Diversificação Global</div>
                    <p class="course-desc">
                        Como estruturar uma carteira internacional em moeda forte. 
                        Acesso a mercados globais e proteção de poder de compra.
                    </p>
                    <hr style='border-color: #30363d'>
                    <small><b>Módulos:</b> 5 aulas</small>
                </div>
            """, unsafe_allow_html=True) # Nível 2 (8 espaços)
            
            if st.button("Acessar Alocação Global", key="btn_global"): # Nível 2
                st.info("Conteúdo exclusivo para investidores qualificados e profissionais.")

        with col_f: # Nível 1
            st.markdown("""
                <div class="course-card">
                    <span class="level-badge">LEGACY</span>
                    <div class="course-title">Planejamento Sucessório</div>
                    <p class="course-desc">
                        O uso de Holdings e Trusts. Como evitar o inventário oneroso 
                        e garantir que a sucessão ocorra de forma fluida.
                    </p>
                    <hr style='border-color: #30363d'>
                    <small><b>Módulos:</b> 7 aulas</small>
                </div>
            """, unsafe_allow_html=True) # Nível 2
            
            if st.button("Acessar Planejamento Sucessório", key="btn_succession"): # Nível 2
                st.info("Módulo disponível para clientes selecionados.")
        

    # --- SEÇÃO DE MENTORIA ---
    st.markdown("---")
    col_m, col_t = st.columns([2, 1])
    with col_m:
        st.subheader("💡 Mentoria Individualizada")
        st.write("""
            Além do conteúdo técnico, os investidores recebem acompanhamento individual para 
            alinhar sua gestão patrimonial a objetivos complexos, garantindo segurança jurídica, 
            eficiência sucessória e performance ajustada ao risco.
        """)
    with col_t:
        if st.button("Saber mais sobre Mentoria"):
            st.toast("Redirecionando para o contato...")
