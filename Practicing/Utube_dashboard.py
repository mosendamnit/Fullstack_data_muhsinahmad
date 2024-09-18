import pandas as pd
import streamlit as st
import plotly.express as px
import os 
import warnings
warnings.filterwarnings("ignore")


st.set_page_config(page_title="Superstore", page_icon=" :bar_chart", layout="wide")


st.title(" :bar_chart: Sample SuperStore EDA") 

fl = st.file_uploader(" :file_folder: Upload a file" , type=(["csv" , "txt","xlsx", "xls"]))

if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename )

else:
    os.chdir("/Users/user/Projects/Fullstack_data_muhsinahmad/data")
    df = pd.read_csv("Sample-Superstore.csv")

# Get two column for startdata and Enddate

col1 , col2 = st.columns((2))

df["Order Date"] = pd.to_datetime(df["Order Date"])


# Getting the start and End date

startDate = pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Starte Date" , startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End date" , endDate))

df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()
