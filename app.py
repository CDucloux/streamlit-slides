import streamlit as st

st.set_page_config(page_icon="🐍", page_title="PyApp")

st.title("😎 Ma première app super stylée")

st.markdown(
    """
    Du *markdown* dans l'app ? **Rien de plus simple !**

    On peut aller à la ligne aussi. :)
    """
)

st.markdown(
    """
    > Des couleurs ? :orange[orange]
    """
)

st.code(
    "[[i for i in range(5)] for j in range(2)] #Du code non-exécutable",
    language="python",
)

st.divider()

st.header("Ajoutons du $\LaTeX$")
st.subheader("Identité d'*Euler*", divider="blue")
st.latex("e^{i \pi} + 1 = 0")
st.caption(
    "L'identité d'Euler est souvent citée comme un exemple de **beauté** mathématique. ✨"
)

fruit = st.selectbox(
    "Fruit",
    ("🍓 Fraise", "Pomme", "Banane", "Mangue", "Orange", "🍖 Viande"),
    index=None,
    placeholder="Sélectionner un fruit",
)

bouton = st.button("Voir les détails du fruit sélectionné")

if bouton:
    st.write(f"T'as la dalle ! Graille une **{fruit}** c'est une dinguerie")
tab_1, tab_2, tab_3 = st.tabs(["Infos sur l'année", "Dataframe", "Graphiques"])

colonne_1, colonne_2 = st.columns([0.3, 0.8])

with st.container(border=True):
    with colonne_1:
        st.write("contenu colonne 1")

with st.container(border=True):
    with colonne_2:
        st.write("contenu colonne 2")


with st.sidebar:
    prenom = st.text_input("😵 Ecris ton prénom")
    reussite = st.checkbox("Tu penses avoir ton année ?")
    note_pf = st.number_input(
        "Ta note en Concurrence & Innovation", min_value=0, max_value=5, step=1
    )

    epanouissement = st.select_slider("Ton épanouissement en master", range(11))


if prenom:
    with tab_1:
        if reussite:
            st.balloons()
            st.write(f"Bien joué pour ton année {prenom}")
        else:
            st.snow()
            st.write(f"Raté {prenom}")

with st.sidebar:
    with st.expander("On regarde quelques messages ?"):
        st.info(f"Ton épanouissement en master : {epanouissement}/10", icon="👨‍🏫")
        st.error(f"Ta note en Concurrence et Innovation : {note_pf}", icon="👀")
        st.warning("Ceci est un avertissement générique", icon="⚠")
        st.success("Message de réussite.", icon="✅")
