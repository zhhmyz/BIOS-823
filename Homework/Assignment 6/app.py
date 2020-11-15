# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("./sed17-sr-tab012.xlsx", header=3)
df1 = df.iloc[[2, 6, 10, 13, 20, 30, 36, 41], [0, 1, 3, 5, 7, 9]]
df2 = df1.melt(var_name = 'Year', id_vars = 'Field of study', value_name = 'Doctorate recipients')

fig = px.line(df2, x = 'Year', y = 'Doctorate recipients', color = 'Field of study', title='Doctorate recipients over time')
fig.update_traces(mode="markers+lines")
fig.update_xaxes(showspikes=True, spikecolor="green", spikesnap="cursor", spikemode="across")
fig.update_yaxes(showspikes=True, spikecolor="orange", spikethickness=2)
fig.update_layout(spikedistance=1000, hoverdistance=100)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.H1(children='Dashboard Visualization of PhDs awarded in the US'),

    dcc.Graph(
        id='Doctorate recipients over time',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)