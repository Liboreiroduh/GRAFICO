import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🎨 Custom CSS para fundo verde e estilização
st.markdown(
    """
    <style>
        .main {
            background-color: #007A33;
        }
        .block-container {
            padding: 2rem 2rem 2rem 2rem;
        }
        div[data-testid="stHeader"] {
            background-color: rgba(0,0,0,0);
        }
        div[data-testid="stSidebar"] {
            background-color: #005F27;
        }
        h1, h2, h3, h4, h5, h6 {
            color: white;
        }
        .stMarkdown p {
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎯 Título e introdução
st.title("🚀 Relatório de Migração - Ouro Plastic")
st.subheader("Foco: Energia Pura - Desconto Aplicado no Mercado Livre")

st.markdown("""
O Mercado Livre de Energia permite que empresas negociem diretamente seu fornecimento de energia, 
buscando **redução de custos, previsibilidade e sustentabilidade.**

Este relatório demonstra como a **Ouro Plastic obteve uma economia real de 12,41% sobre a energia ativa** 
ao migrar para o mercado livre de energia com a **Inti Energia**.
""")

st.markdown("---")

# 🔢 Dados principais
st.header("📊 Dados e Comparativos")

# Tabela comparativa
data = {
    'Cenário': ['Mercado Cativo', 'Mercado Livre'],
    'Custo Energia (R$)': [1906.46, 1669.50]
}
df = pd.DataFrame(data)

st.subheader("✅ Comparativo de Custo da Energia Ativa (5,3 MWh)")
st.table(df)

# 🔥 Gráfico de barras
st.subheader("🔍 Comparativo Visual dos Custos")
fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(x='Cenário', y='Custo Energia (R$)', data=df, palette=['#B22222', '#32CD32'], ax=ax)
ax.bar_label(ax.containers[0], fmt='R$ %.2f', label_type='edge', fontsize=9)
ax.set_ylabel('Custo (R$)')
ax.set_title('Custo da Energia Ativa: Antes e Depois')
st.pyplot(fig)

# 🔥 Economia destacada
economia = 1906.46 - 1669.50
st.subheader("💰 Economia Mensal na Energia Ativa")
st.success(f"Economia Mensal: **R$ {economia:.2f} → Desconto de 12,41% na Energia Ativa (kWh)**")

st.markdown("---")

# 🚀 Cards resumidos
st.header("🧠 Resumo do Contrato")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Energia Contratada", value="5,3 MWh/mês")
    st.metric(label="Preço Mercado Cativo", value="R$ 359,52/MWh")
with col2:
    st.metric(label="Preço Mercado Livre", value="R$ 315,00/MWh")
    st.metric(label="Desconto sobre Energia", value="12,41%")

st.markdown("---")

# 🏛️ Storytelling e contexto
st.header("📖 Entendendo a Migração")

st.markdown("""
### 🏢 **Antes - Mercado Cativo**
- Pagava a energia ativa a **R$ 359,52/MWh**.
- Custo mensal da energia ativa: **R$ 1.906,46**.

### ⚡ **Depois - Mercado Livre**
- Energia contratada com preço fixo de **R$ 315,00/MWh**.
- Custo mensal da energia ativa: **R$ 1.669,50**.

### ✔️ **Desconto aplicado na energia ativa:** **12,41%**

Essa migração garante:
- 🔋 Menor custo na energia.
- 🌿 Energia incentivada (fonte limpa).
- 🚫 Proteção contra bandeiras tarifárias.
- 📅 Previsibilidade no preço até 2030.
""")

st.markdown("---")

# ⚖️ Riscos e obrigações
st.header("⚠️ Riscos e Condições")

st.markdown("""
### ❌ **Inadimplência**
- Desconexão da CCEE até regularização.
- Retorno ao mercado cativo **só após quitação total** e aviso prévio de **5 anos** (Resolução ANEEL nº 1.000/2021).

### 🛡️ **Segurança Contratual**
- A Inti Energia oferece **coobrigação sobre os recebíveis**, assegurando proteção na operação no mercado livre.
""")

st.markdown("---")

# ✅ Conclusão
st.header("✅ Conclusão Final")

st.markdown("""
A migração da Ouro Plastic para o Mercado Livre proporcionou uma **economia direta de 12,41% sobre a energia ativa (kWh)**, 
além de garantir previsibilidade financeira, sustentabilidade e alinhamento com as práticas ESG.

**Inti Energia - Energia inteligente, limpa e acessível.**
""")
