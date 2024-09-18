import streamlit as st
from components.data import SwedishSummerMedals


class SwedishSummerGraphs:
    def __init__(self) -> None:
        self.swe_medals = SwedishSummerMedals()

    def bar_medal_sport(self):
        data = self.swe_medals.per_sport
        st.bar_chart(data , x_label= "Sport" , y_label= "medal per sport")




    def bar_medal_athlete_top10(self):
        data = self.swe_medals.per_athlete.iloc[:10]
        st.bar_chart(data , x_label= "Athlete" , y_label= "medal per athlete")
