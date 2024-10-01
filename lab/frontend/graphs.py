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


class OperativeViews:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.operativesystem_per_view").df
        print(self.df)


    def plot_display(self):
        fig = px.bar(self.df , x = "Operativsystem" , y = "Total_Visningar")
        st.markdown("## See plot between Operativesystem againist Total Visningar")
        st.plotly_chart(fig)


class GeograficViews:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_geografi").df
        print(self.df)

    def display_geoViewers(self):
        fig = px.line( self.df , x = "Datum" , y = "Total_Viewers")
        st.markdown("## Total views againist as per viewers from respective State")
        st.plotly_chart(fig)