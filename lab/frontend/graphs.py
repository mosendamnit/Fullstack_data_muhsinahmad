from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st 

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)

# create more graphs here

class OperativeViews:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.operativesystem_per_view").df
        st.markdown(" See plot between Operativesystem againist Viewers")
        print(self.df)


    def plot_display(self):
        fig = px.line(self.df , x = "Datum" , y = "Visningar")
        st.plotly_chart(fig)