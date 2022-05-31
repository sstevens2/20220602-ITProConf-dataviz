import streamlit as st
import pandas as pd
import plotly.express as px

# set up the app with wide view preset and a title
st.set_page_config(layout = "wide")
st.title("Interact with Gapminder Data")

# read in the tidy gapminder data
df = pd.read_csv("Data/gapminder_tidy.csv")
# filter the data to only Oceania gdpPercap values
df_filtered = df.query("continent=='Oceania' & metric=='gdpPercap'")

# creating the plot
title = "GDP for countries in Oceania"
fig = px.line(df_filtered, x = "year", y = "value", color = "country", title = title, labels={"value": "GDP Percap"})
st.plotly_chart(fig)

# Line of text describing the plot 
st.markdown("This plot shows the GDP Per Capita for countries in Oceania.")


# Challenge - Display the data table used to create the plot
st.dataframe(df_filtered)
