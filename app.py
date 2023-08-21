import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px


dash_app = Dash(__name__)

dash_app.title = "Soul Foods Data Viz"

df = pd.read_csv('data/df3')

fig = px.line(df, x="date", y="sales")

dash_app.layout = html.Div(style={'padding': 10}, children=[
    html.H2(
        children='Pink Morsel Sales Visualization',
        style={
            'textAlign': 'center',
            'font-family':'sans-serif'
        },
        id="header"
    ),
    
    html.Div([
      html.Label('Change the region here : '),
      html.Br(),
      dcc.RadioItems([{'label': 'Noth', 'value': 'north'}, {'label': 'South', 'value': 'south'},
      {'label': 'East', 'value': 'east'}, {'label': 'West', 'value': 'west'}], 'north', id='region', inline=True),
    ], style={'display': 'flex', 'textAlign': 'center', 'font-family':'sans-serif', 'alignItems': 'center', 'justifyContent': 'center', 'margin': '10px'}),

    dcc.Graph( 
        id='salesGraph',
        figure=fig,
    )
])

@dash_app.callback(
    Output('salesGraph', 'figure'),
    Input('region', 'value'))

def update_graph(region):
    dff = df[df['region'] == region]

    fig = px.line(dff, x="date", y="sales", template = "ggplot2")

    return fig

if __name__ == '__main__':
    dash_app.run_server(debug=True)