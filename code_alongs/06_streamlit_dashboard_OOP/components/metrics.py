import streamlit as st
from components.data import MedalsPerCountry

medals_per_countrty = MedalsPerCountry()

class Metrics:
    def country_medals_top_5(self):
        st.markdown("## Top 5 countries with most medals")
        cols = st.columns(5)

        for col , country , data in zip (cols , medals_per_countrty.summer_noc.index , medals_per_countrty.summer_noc ):
            with col:
                st.metric(label= country , value= data)


class MedalsCountry:
    def __init__(self , country) -> None:
        self.country = country
        self._medals_per_country = MedalsPerCountry()
        self._summer_medal_type = self._medals_per_country.summer_medals_type


    def _total(self):

        medals_series = self._medals_per_country.summer_noc

        st.metric(label= "Total medals" , value=medals_series[self.country])


    def display_medals(self):
        cols = st.columns(4)
        medals = (self._total, self._gold)



    def _gold(self):
        st.metric(
            label="Gold Medal" , value=self._summer_medal_type["Gold"][self.country]
        )


    def _silver(self):
        st.metric(
            label="Silver Medal" , value=self._summer_medal_type["Silver"][self.country]
        )


    def _bronze(self):
        st.metric(
            label="Bronze Medal" , value=self._summer_medal_type["Bronze"][self.country]
        )
        

