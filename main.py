import streamlit as st
import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot,plot
import pandas as pd

# init_notebook_mode(connected=True) 

st.title('2014 World Power Consumption')
df = pd.read_csv('2014_World_Power_Consumption')
# df.head()

data = dict(
        type = 'choropleth',
        colorscale='aggrnyl',
        locations = df['Country'],
        locationmode = "country names",
        z = df['Power Consumption KWH'],
        text = df['Text'],
        colorbar = {'title' : 'Power Consumption KWH'},
      ) 
layout = dict(title='Power Consumption', geo=dict(showframe=False,
        projection = {'type':'bottomley'}))

choromap = go.Figure(data = [data],layout = layout)
st.write(iplot(choromap,validate=False))

# st.plotly_chart(iplot(choromap,validate=False))