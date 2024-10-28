import requests
import streamlit as st

def connect_to_data_sources(character_number):
    # API endpoint
    api_url = f"https://swapi.dev/api/people/{character_number}/"

    # Make HTTP request
    response = requests.get(api_url)

    # Check if request is successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Display data
        st.write("Informations principales")
        name = data.get("name")
        height = data.get("height")
        birth_year = data.get("birth_year")
        gender = data.get("gender")

        st.write(f"nom : {name}")
        st.write(f"taille : {height}")
        st.write(f"année de naissance : {birth_year}")
        st.write(f"genre : {gender}")

        st.write("Informations complètes")

        st.json(data)


input_character_number = st.text_input("Entrez le numéro d'un personnage pour obtenir ses informations :")

if input_character_number:
    connect_to_data_sources(input_character_number)