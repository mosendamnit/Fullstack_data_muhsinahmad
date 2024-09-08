import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


def read_data():
    data_path = Path(__file__).parents[1]/ "data"
    df = pd.read_csv (data_path / "cleaned_yh_region.csv" , index_col=0 , parse_dates=[0])
    df.index = df.index.year
    return df

def layout():
    df = read_data()
    df_reset = df.reset_index(names=["year"]).style.format({"year" : lambda x: f"{x}"})


    st.markdown("# YH dashboard")
    
    st.markdown("This data shows number of started education per region and per year ")
    st.markdown("## Raw data")



    st.dataframe(df_reset)

    st.markdown("## Trens per Region ")
    region = st.selectbox("Choose a region" , df.columns)
    #print(region)

    region_status = df[region].describe()

    cols = st.columns(4)

    stats = ("min" , "50%" , "max")
    labels = ("min", "median", "max")


    for col , stat , label in zip (cols , stats ,labels):

        with col:
            st.metric(label=label , value= region_status[stat])


    fig = px.line(
        data_frame= df,
        x = df.index,
        y= df[region],
        title = f"Started education in {region} 2007-2023"
    )

    fig.update_traces(line=dict(width=3))
    fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
    st.plotly_chart(fig)





if __name__ == '__main__':
    layout()


