import streamlit as st
import pandas as pd
import plotly.express as px

# set up the app with wide view preset and a title
st.set_page_config(layout = "wide")
st.title("Interact with Gapminder Data")

# read in the tidy gapminder data
df = pd.read_csv("Data/gapminder_tidy.csv")

# list of possible continents
continent_list = list(df['continent'].unique())
metric_list = list(df['metric'].unique())

# filter the data to only the data we are plotting
continent = st.selectbox(label = "Choose a continent", options = continent_list)
metric = st.selectbox(label = "Choose a metric", options = metric_list)
df_filtered = df.query(f"continent=='{continent}' & metric=='{metric}'")

# creating the plot
title = f"{metric} for countries in {continent}"
fig = px.line(df_filtered, x = "year", y = "value", color = "country", title = title, labels={"value": f"{metric}"})
st.plotly_chart(fig)

# Line of text describing the plot
st.markdown(f"This plot shows the {metric} for countries in {continent}.")


# Challenge - Display the data table used to create the plot
st.dataframe(df_filtered)
