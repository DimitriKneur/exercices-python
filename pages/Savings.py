import streamlit as st

def savings():
    # Input pour le montant initial
    try:
        initial_amount = st.number_input("Quel est le montant total que vous souhaitez investir ?", min_value=0.0, format="%.2f")
        duration = st.number_input("Combien d'années allez-vous investir cet argent ?", min_value=0.0, format="%.0f")
        interest_rate = st.number_input("À quel taux d'intérêt souhaiteriez-vous investir ? (sous forme décimale, par exemple 10% --> 0.10)", min_value=0.0, max_value=1.0, format="%.2f")
        
        # Vérification des valeurs négatives ou des taux supérieurs à 1
        if initial_amount < 0 or duration < 0 or interest_rate < 0:
            st.error("Veuillez entrer uniquement des valeurs positives.")
        elif interest_rate > 1:
            st.error("Veuillez entrer le taux d'intérêt sous forme décimale (par exemple 10% --> 0.10).")
        else:
            # Calcul du montant total si les valeurs sont valides
            total = initial_amount * (1 + interest_rate) ** duration
            st.success("Le montant total que vous aurez après avoir déposé {:.2f} € pour une durée de {} ans sera de {:.2f} €.".format(initial_amount, duration, total))
    
    except ValueError:
        st.error("Veuillez entrer uniquement des nombres.")

# Appel de la fonction de calcul d'épargne
savings()
