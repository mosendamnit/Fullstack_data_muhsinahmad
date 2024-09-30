import streamlit as st 
from frontend.kpi import ContentKPI , DeviceKPI , GeoKPI
from frontend.graphs import ViewsTrend , OperativeViews , GeograficViews


device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
operative_views = OperativeViews()
geo_kpi = GeoKPI()
geografic_viewer = GeograficViews()



def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    content_kpi.display_content()
    views_graph.display_plot()
    device_kpi.operative_views()
    operative_views.plot_display()
    geo_kpi.viewsPer_geografi()
    geografic_viewer.display_geoViewers()

if __name__ == "__main__":
    layout()