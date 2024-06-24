import streamlit as st
import requests
# import json

# Configuração da página Streamlit
st.set_page_config(page_title="SprintHub API - Listar Oportunidades de Lead")

# Título da aplicação
st.title("SprintHub API - Listar Oportunidades de Lead")

# Instruções de uso
st.markdown("""
## Instruções de Uso
1. Preencha o ID do Lead que você deseja buscar.
2. Insira o identificador da sua instância.
3. Forneça seu API Token.
4. Insira o Bearer Token para autenticação.
5. Clique em "Buscar Oportunidades" para ver os resultados.
""")

# Campos de entrada
lead_id = st.text_input("ID do Lead")
instance = st.text_input("Identificador da Instância")
api_token = st.text_input("API Token", type="password")
bearer_token = st.text_input("Bearer Token", type="password")

# Botão para fazer a requisição
if st.button("Buscar Oportunidades"):
    # Verificar se todos os campos foram preenchidos
    if lead_id and instance and api_token and bearer_token:
        # Construir a URL
        url = f"https://sprinthub-api-master.sprinthub.app/listopportunitysleadcomplete/{lead_id}?i={instance}"

        # Configurar os headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer_token}",
            "apitoken": api_token
        }

        try:
            # Fazer a requisição GET
            response = requests.get(url, headers=headers)

            # Verificar o status da resposta
            if response.status_code == 200:
                # Exibir os resultados
                opportunities = response.json()
                st.success("Oportunidades encontradas com sucesso!")
                st.balloons()
                st.json(opportunities)
            else:
                st.error(f"Erro na requisição: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Ocorreu um erro: {str(e)}")
    else:
        st.warning("Por favor, preencha todos os campos.")

