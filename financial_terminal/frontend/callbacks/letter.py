import streamlit as st

def render_manager_letter():
    st.title("✉️ Repositório de Cartas dos Gestores")
    st.write("Acompanhe a visão das maiores mentes do mercado financeiro nacional e internacional.")

    # Organização por Categorias (UX: Facilita a busca do cliente)
    cat1, cat2, cat3, cat4 = st.tabs([
        "🏆 Gestoras (Brasil)", 
        "🌍 Global", 
        "🏦 Bancos & Cooperativas", 
        "🔍 Research & Análise"])

    with cat1:
        st.subheader("Asset Management Brasil")
        # Criando uma grade 3xN
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.link_button("🛡️ Kinea", "https://www.kinea.com.br/blog/categoria/carta-do-gestor/", use_container_width=True)
            st.link_button("🐆 Guepardo", "https://www.guepardoinvest.com.br/cartas-da-gestora/", use_container_width=True)
            st.link_button("📜 Bahia Asset", "https://www.bahiaasset.com.br/carta-do-gestor/", use_container_width=True)
            st.link_button("💎 Constellation", "https://constellation.com.br/documentos-relevantes/", use_container_width=True)
            st.link_button("🏦 Vinland", "https://www.vinlandcap.com/midia-e-imprensa", use_container_width=True)
            st.link_button("📈 Pátria Investimentos", "https://www.patria.com/", use_container_width=True)
            
            
        with col2:
            st.link_button("🏦 ARX Investimentos", "https://www.arxinvestimentos.com.br/pt/communication.html", use_container_width=True)
            st.link_button("🐻 Alaska Asset Management", "https://www.alaska-asset.com.br/cartas/", use_container_width=True)
            st.link_button("⚖️ Absolute", "https://absoluteinvestimentos.com.br/fundos/", use_container_width=True)
            st.link_button("🟢 Verde Asset", "https://www.verdeasset.com.br/#/performance", use_container_width=True)
            st.link_button("🌐 Vinci Partners", "https://www.vincipartners.com/", use_container_width=True)
            st.link_button("📈 Ibiúna", "https://www.ibiunainvest.com.br/fundos/", use_container_width=True)
            
        with col3:
            st.link_button("🏢 Kapitalo", "https://www.kapitalo.com.br/cartas-do-gestor", use_container_width=True)
            st.link_button("💼 Gávea Investimentos", "https://www.gaveainvest.com.br/multimercados-macro-global/", use_container_width=True)
            st.link_button("🚀 Adam Capital", "https://adamcapital.com.br/documentos/relatorios-e-call/", use_container_width=True)
            st.link_button("📊 Legacy Capital", "https://legacycapital.com.br/cartas-e-calls-mensais/", use_container_width=True)
            st.link_button("📌 Opportunity", "https://www.opportunity.com.br/QuemSomos/Asset", use_container_width=True)
            st.link_button("🏙️ RBR Asset Management", "https://www.rbrasset.com.br/", use_container_width=True)

    with cat2:
        st.subheader("Global & Outras Teses")
        colA, colB = st.columns(2)
        
        with colA:
            st.link_button("🌎 BlackRock Insights", "https://www.blackrock.com/corporate/insights/blackrock-investment-institute/publications/weekly-commentary", use_container_width=True)
            st.link_button("🇺🇸 Oaktree (Howard Marks)", "https://www.oaktreecapital.com/insights", use_container_width=True)
            st.link_button("💰 Goldman Sachs Asset Management", "https://www.goldmansachs.com", use_container_width=True)
            st.link_button("💼 Fidelity Investments", "https://www.fidelity.com", use_container_width=True)
            st.link_button("🌍 UBS Asset Management", "https://www.ubs.com", use_container_width=True)
            st.link_button("🇫🇷 Amundi", "https://www.amundi.com", use_container_width=True)

        with colB:
             st.link_button("💹 J.P. Morgan", "https://am.jpmorgan.com/br/pt/asset-management/adv/insights/", use_container_width=True)
             st.link_button("🔍 Bridgewater", "https://www.bridgewater.com/research-and-insights", use_container_width=True)
             st.link_button("📊 Vanguard Group", "https://www.vanguard.com", use_container_width=True)
             st.link_button("🏢 State Street Global Advisors", "https://www.ssga.com", use_container_width=True)
             st.link_button("📈 Capital Group", "https://www.capitalgroup.com", use_container_width=True)
             st.link_button("💡 Allianz Global Investors", "https://www.allianzgi.com", use_container_width=True)

        
    with cat3:
        st.subheader("Grandes Conglomerados Financeiros")
        colB1, colB2 = st.columns(2)
        
        with colB1:
            st.link_button("🟡 BB Asset", "https://www.bbasset.com.br/", use_container_width=True)
            st.link_button("🟠 Itaú Asset", "https://www.itauassetmanagement.com.br/", use_container_width=True)
            st.link_button("🔴 Bradesco Asset", "https://www.bradescoasset.com.br/", use_container_width=True)
            st.link_button("🔵 CAIXA Asset", "https://www.caixa.gov.br/caixa-asset/Paginas/default.aspx", use_container_width=True)
            
        with colB2:
            st.link_button("🔴 Santander Asset", "https://www.santanderassetmanagement.com.br/", use_container_width=True)
            st.link_button("💎 BTG Asset", "https://www.btgpactual.com/asset-management/", use_container_width=True)
            st.link_button("🏦 Safra Asset", "https://www.safra.com.br/safra-asset/", use_container_width=True)
            st.link_button("🌾 Sicredi Gestão", "https://www.sicredi.com.br/site/asset/", use_container_width=True)
    
    with cat4:
        st.subheader("Casas de Análise")
        colR1, colR2 = st.columns(2)
        
        with colR1:
            st.markdown("##### Estratégia e Valor")
            st.link_button("💎 Nord Research", "https://nordresearch.com.br/conteudo/", use_container_width=True)
            st.link_button("☀️ Suno Research", "https://www.suno.com.br/artigos/", use_container_width=True)
            st.link_button("📈 Levante", "https://www.levanteideias.com.br/blog/", use_container_width=True)
            

            
        with colR2:
            st.markdown("##### Análise")
            st.link_button("🔍 Eleven Financial", "https://elevenfinancial.com", use_container_width=True)
            st.link_button("📊 Empiricus", "https://empiricus.com.br/conteudo/", use_container_width=True)
            st.link_button("🎯 Capitalizo", "https://capitalizo.com.br/blog/", use_container_width=True)
            

            
    st.markdown("---")
    st.info("💡 Dica de ouro: Fique atento à primeira quinzena de cada mês. A leitura das cartas da Kinea, Kapitalo, Guepardo, Alaska, Bahia e outras, permite uma visão profunda e diversificada, essencial para compreender as nuances do cenário macroeconômico brasileiro.")
