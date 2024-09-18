import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor






def read_data():
    data_path = Path(__file__).parents[2] / "data"
    df = pd.read_csv(data_path / "IceCreamData.csv")
    return df

def layout():

    df = read_data()
    st.markdown("# Ice Cream Predication App")
    df[["Temperature" , "Revenue"]] = df[["Temperature" , "Revenue"]].round(2)
    st.dataframe(df)


    fig = px.scatter(df , x= "Temperature" , y="Revenue")
    st.plotly_chart(fig)


    st.markdown("## Predict the revenue on the base of Temperature")

    df =df.set_index("Temperature")
    user_input = st.number_input("Enter the temperature ")

    if user_input in df.index :
        result = df.loc[user_input , "Revenue"]
        st.write(f"The reveneu will be {result}")
    else:
        st.write("Try again")


    st.markdown("## Use Random forest regression to preict the revenue")

    x = df["Temperature"].values
    y = df["Revenue"].values

    model = RandomForestRegressor(n_estimators=5)
    model.fit(x , y)


    user_input_pred = st.number_input("Enter the temperature" , value=0.0 )
    user_input_reshaped = [[user_input_pred]]

    prediction = model.predict(user_input_reshaped)

    st.write(f"Prediction revenue based on random forest {prediction[0]}")


if __name__ == "__main__":
    layout()

