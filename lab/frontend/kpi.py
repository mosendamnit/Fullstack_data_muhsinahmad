import streamlit as st
from utils.query_database import QueryDatabase

class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")

        kpis = {
            "videor": len(df),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum(),
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))
        st.dataframe(df)
class DeviceKPI:
    def __init__(self) -> None:
        self._device = QueryDatabase("SELECT * FROM marts.operativesystem_per_view").df

    def operative_views(self):
        df = self._device
        st.markdown("## KPI for Operative System")

        
        kpis = {
            "operative system" : len(df["Operativsystem"].unique()),
            "Visningar": df["Total_Visningar"].sum(),
            "Visning Timmar": df["Total_Visningstid_timmar"].unique().sum(),
        }

        
        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col:
                st.metric(kpi, round(kpis[kpi]))

        st.dataframe(df)

class GeoKPI:
    def __init__(self):
        self._geografi = QueryDatabase("SELECT * FROM marts.views_per_geografi; ").df 

    def viewsPer_geografi(self):
        df = self._geografi
        st.markdown("## Viewers Per State")

        start_date = df["Datum"].min()
        end_date = df["Datum"].max()


        Kpis = {
            "Date" : f"{start_date} to {end_date}",
            "Total_Views" : df["Total_Viewers"].sum()
        }

        for col, kpi in zip(st.columns(len(Kpis)), Kpis):
            with col:
                st.metric(kpi, (Kpis[kpi]))

        st.dataframe(df)