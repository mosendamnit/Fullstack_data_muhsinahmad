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

        # Corrected dictionary name and key (no space after 'Visning')
        kpis = {
            "operative system" : len(df["Operativsystem"].unique()),
            "Visningar": df["Visningar"].unique().sum(),
            "Visning Timmar": df["Visningstid (timmar)"].unique().sum(),
        }

        # Using the correct variable name 'kpis' in the for loop
        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col:
                st.metric(kpi, round(kpis[kpi]))

        st.dataframe(df)

