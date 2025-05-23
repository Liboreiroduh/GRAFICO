import streamlit as st
import pandas as pd
import plotly.express as px

# ======================= #
# 🎨 Layout e Configuração
st.set_page_config(page_title="Dashboard Ouro Plastic", layout="wide")

st.markdown(
    """
    <style>
        .main {background-color: #007A33;}
        div.block-container {padding: 1rem 2rem;}
        h1, h2, h3, h4, h5, h6 {color: white;}
        .stMarkdown p {color: white;}
    </style>
    """, unsafe_allow_html=True
)

# ======================= #
# 🔝 Header
st.title("🚀 Dashboard de Migração - Ouro Plastic")
st.subheader("Análise da Energia Ativa no Mercado Livre")

st.markdown("---")

# ======================= #
# 📊 Dados principais
cativo = 1906.46
livre = 1669.50
economia = cativo - livre
percentual = round((economia / cativo) * 100, 2)

# ======================= #
# 🔥 KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("⚡ Energia Contratada", "5,3 MWh/mês")
col2.metric("💰 Preço Cativo", "R$ 359,52/MWh")
col3.metric("🏷️ Preço Livre", "R$ 315,00/MWh")
col4.metric("🔻 Economia na Energia", f"{percentual}%", f"-R$ {economia:.2f}")

st.markdown("---")

# ======================= #
# 📈 Gráfico de Barras
df = pd.DataFrame({
    'Cenário': ['Mercado Cativo', 'Mercado Livre'],
    'Custo Energia (R$)': [cativo, livre]
})

fig = px.bar(
    df,
    x='Cenário',
    y='Custo Energia (R$)',
    color='Cenário',
    color_discrete_map={'Mercado Cativo': 'crimson', 'Mercado Livre': 'limegreen'},
    text_auto=True,
    title="Comparativo de Custo da Energia Ativa"
)

fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(255,255,255,1)',
    font_color='black'
)

st.plotly_chart(fig, use_container_width=True)

# ======================= #
# 📑 Tabela Comparativa
st.subheader("📄 Tabela Comparativa de Custos")
st.dataframe(df.set_index('Cenário'))

st.markdown("---")

# ======================= #
# ✔️ Benefícios
st.subheader("✔️ Benefícios da Migração")
st.info("""
- Economia direta de **12,41% sobre energia ativa (kWh)**.
- Preço fixo até 2030, sem bandeiras tarifárias.
- Energia limpa e incentivada (50% desconto na TUSD fio B).
- Previsibilidade financeira e segurança contratual.
""")

# ======================= #
# ⚠️ Riscos e Obrigações
st.subheader("⚠️ Riscos e Condições")
st.warning("""
- Inadimplência → Suspensão na CCEE.
- Retorno ao mercado cativo → Somente após quitar débitos e com aviso prévio de 5 anos (Resolução 1000/2021).
""")

# ======================= #
# ✅ Conclusão
st.subheader("✅ Conclusão")
st.success("""
A migração da Ouro Plastic trouxe uma economia direta sobre energia ativa, 
mantendo previsibilidade e alinhamento com energia sustentável.

**Inti Energia - Energia inteligente, limpa e acessível.**
""")
