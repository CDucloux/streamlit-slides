import streamlit as st
from streamlit.delta_generator import DeltaGenerator

st.set_page_config(page_icon="🐍", page_title="PyApp")
st.title("😎 Ma première app super stylée")

st.markdown("Du *markdown* dans l'app ? **Rien de plus simple !**")
st.markdown("- Lien vers [`streamlit`](https://streamlit.io/)")
st.markdown(
    """
    > Des couleurs ? :orange[orange], :red[rouge], :green[vert]
    """
)

st.code(
    """
    [[i for i in range(5)] for j in range(2)] 
    # Du code non-exécutable
    """,
    language="python",
)

st.divider()

st.header("Ajoutons du LaTeX")
st.subheader("Identité d'*Euler*", divider="blue")
st.latex("e^{i \pi} + 1 = 0")
st.caption(
    """
    L'identité d'*Euler* est souvent citée comme
    un exemple de beauté mathématique.
    """
)

fruit = st.selectbox(
    "Fruit",
    ("🍓 Fraise", "🍊 Orange", "🥭 Mangue", "🍌 Banane", "🍏 Pomme"),
    index=None,
    placeholder="Sélectionner un fruit",
)

bouton = st.button("Voir les détails du fruit sélectionné")

if bouton:
    st.write(f"T'as la dalle ! Tu veux manger une **{fruit}**")

with st.sidebar:
    prenom = st.text_input("🤠 Ecrire ton prénom *cow-boy* !")
    reussite = st.checkbox("Tu penses avoir ton année ?")
    note_pf = st.number_input(
        "Ta note en Concurrence et Innovation", min_value=0, max_value=10, step=1
    )
    epanouissement = st.select_slider("Ton épanouissement en master", range(11))

tab_1, tab_2, tab_3 = st.tabs(["🔎 Infos sur l'année", "📄 DataFrame", "📊 Graphiques"])


if prenom:
    with tab_1:
        if reussite:
            st.balloons()
            st.write(f"Félicitations pour ton année *{prenom}* ! 🎈")
        else:
            st.snow()
            st.write(f"**Aie Aie Aie heing**... 🥶 va falloir taffer *{prenom}*")

with st.sidebar:
    with st.expander("On regarde quelques messages ?"):
        st.info(f"Ton épanouissement en master : {epanouissement}/10", icon="👨‍🏫")
        st.error(f"Ta note en Concurrence et Innovation : {note_pf}", icon="👀")
        st.warning("Ceci est un avertissement générique", icon="⚠")
        st.success("Message de réussite.", icon="✅")

if not prenom:
    with tab_1:
        st.warning("Attention, sans prénom, on va pas y arriver...", icon="😶")

import polars as pl


@st.cache_data
def import_covid_usa(link: str) -> pl.DataFrame:
    """Fonction d'import des données optimisée."""
    return pl.read_csv(link)


df_covid = import_covid_usa(
    "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
)

with tab_2:
    st.dataframe(
        df_covid,
        hide_index=True,
        use_container_width=True,
        column_config={
            "date": st.column_config.DateColumn("📅 Date", format="DD/MM/YYYY")
        },
    )

with tab_3:
    st.subheader("Nombre de personnes mortes de COVID-19 *(Noël 2020)*")

    deaths_by_state_christmas = (
        df_covid.filter(pl.col("date") == "2020-12-25")
        .group_by("state")
        .agg(pl.col("deaths").sum())
    )

    st.bar_chart(deaths_by_state_christmas, x="state", y="deaths")

# st.image()  # à mettre
