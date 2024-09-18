import streamlit as st
from components.data import MedalsSummer , Countries
from components.metrics import Metrics , MedalsCountry 
from components.graphs import SwedishSummerGraphs

medals_df = MedalsSummer()
metrics = Metrics()
swedish_graph = SwedishSummerGraphs()
countries = Countries()


def layout():
    st.markdown("# Summer olympics dashboard")
    st.markdown(
        """
        This dashboard shows 124 years of olympic data. In this demo, only summer olympics will be shown.
        The source of the dataset comes from here https://www.kaggle.com/datasets/nitishsharma01/olympics-124-years-datasettill-2020
        
        """
    )

    metrics.country_medals_top_5()

    st.markdown("## Medall Filter Country")
    selected_country = st.selectbox("Select a Country" , options= countries.noc)
    MedalsCountry(selected_country).display_medals()



    st.markdown("## Medal per sport in Sweden")
    swedish_graph.bar_medal_sport()


    st.markdown("## Medal per Athlete in Sweden (top 10)")
    swedish_graph.bar_medal_athlete_top10()


if __name__ == "__main__":
    layout()
















