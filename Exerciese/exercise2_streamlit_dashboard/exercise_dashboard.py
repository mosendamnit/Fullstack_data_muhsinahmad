import pandas as pd
import streamlit as st
from pathlib import Path
import plotly.express as px




def read_data():
    data_ptah = Path(__file__).parents[2] / "data"
    df = pd.read_csv (data_ptah / "supahcoolsoft.csv" )
    return df

def cal_summary(df):

    total_count = df.shape[0]
    average_age = df["Age"].mean()
    average_salary = df["Salary_SEK"].mean()


    summary_df = pd.DataFrame({
        'Metrics': ['Total Count', 'Average Age', 'Average Salary'],
        'Value': [total_count, average_age, average_salary]
    })

    return summary_df



def layout():
    df = read_data()
    st.markdown("# Data Frame")
    st.dataframe(df)

    # Basic statistics on employees (total count, average age, average salary
    st.markdown("## Basic statistics on employees (total count, average age, average salary")
    summary_df = cal_summary(df)
    st.table(summary_df)


    # Show a table with employee details
    st.markdown("## Show a table with employee details")
    st.dataframe(df)


    # Bar chart showing number of employees accross departments
    st.markdown("## Bar chart showing number of employees accross departments")
    department_summary = df.groupby('Department')
    department_count = department_summary.size()
    st.bar_chart(department_count)


    # histogram of salary distribution
    st.markdown("## histogram of salary distribution ")
    salary_dist = df["Salary_SEK"]
    st.bar_chart(salary_dist)


    # Box plot of salaries by department
    st.markdown("# Box plot of salaries by department")
    extract_depart_salary = df[["Department" , "Salary_SEK"]]
    fig = px.box(extract_depart_salary , x='Department' , y='Salary_SEK')
    st.plotly_chart(fig)


    # Histogram of age distribution
    st.markdown("## Histogram of age distribution ")
    age_dict = df["Age"]
    st.bar_chart(age_dict)


# Box plot of ages by department

    st.markdown("## Box plot of ages by department ")
    extract_depart_age = df[["Department" , "Age"]]
    fig = px.box(extract_depart_age , x= "Age" , y= "Department")
    st.plotly_chart(fig)


if __name__ == "__main__":
    layout()