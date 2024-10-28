import streamlit as st

# Titre de l'application
st.title("Vérification de mot de passe")

# Champ de saisie pour le mot de passe
password = st.text_input("Entrez le mot de passe :", type="password")

# Vérification du mot de passe
if password:
    if password == 'jedha':
        st.success("Vous avez le bon mot de passe !")
    else:
        st.error("Mot de passe incorrect. Essayez à nouveau.")
