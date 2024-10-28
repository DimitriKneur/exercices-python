import streamlit as st

# Initialisation des vies en session
if 'lives' not in st.session_state:
    st.session_state.lives = 3

# Message de bienvenue
st.write("Bienvenue dans notre quiz !")
st.write("Vous avez 3 vies.")
st.write("")

# Question 1
if st.session_state.lives > 0:
    st.write("Question 1 : Combien de fois l'équipe de France de football a-t-elle remporté la Coupe du Monde ?")
    question1 = st.text_input("Votre réponse pour la Question 1", key="q1")
    if question1:
        st.write(f"Votre réponse : {question1}")
        if question1 != "2":
            st.session_state.lives -= 1
            st.write(f"Désolé, il vous reste {st.session_state.lives} vies.")
        if st.session_state.lives == 0:
            st.write("Oh non, vous avez perdu le quiz...")
        elif question1 == "2":
            st.write("Bonne réponse ! Passons à la question suivante.")

# Question 2
if st.session_state.lives > 0 and question1 == "2":
    st.write("Question 2 : En quelle année Apple a-t-elle été fondée ?")
    question2 = st.text_input("Votre réponse pour la Question 2", key="q2")
    if question2:
        st.write(f"Votre réponse : {question2}")
        if question2 != "1976":
            st.session_state.lives -= 1
            st.write(f"Désolé, il vous reste {st.session_state.lives} vies.")
        if st.session_state.lives == 0:
            st.write("Oh non, vous avez perdu le quiz...")
        elif question2 == "1976":
            st.write("Bonne réponse ! Passons à la question suivante.")

# Question 3
if st.session_state.lives > 0 and question1 == "2" and question2 == "1976":
    st.write("Question 3 : Qui a fondé SpaceX ?")
    question3 = st.text_input("Votre réponse pour la Question 3", key="q3")
    if question3:
        st.write(f"Votre réponse : {question3}")
        if question3.lower() != "elon musk":
            st.session_state.lives -= 1
            st.write(f"Désolé, il vous reste {st.session_state.lives} vies.")
        if st.session_state.lives == 0:
            st.write("Oh non, vous avez perdu le quiz...")
        elif question3.lower() == "elon musk":
            st.write("Félicitations, vous avez gagné le quiz !")
