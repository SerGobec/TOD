import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
# Завантаження даних
data = pd.read_csv('stocks3.csv')  # Припустимо, що у вас є файл stock_data.csv з даними акцій

# Створення Dash-додатку
app = dash.Dash(name)

app.layout = html.Div(children=[
    html.H1(children='Stock price chart'),
    dcc.Graph(
        id='stock-chart',
        figure={
            'data': [
                go.Scatter(
                    x=data['Date'],
                    y=data['Price'],
                    mode='lines',
                    name='share price'
                )
            ],
            'layout': go.Layout(
                xaxis={'title': 'Date'},
                yaxis={'title': 'share price'},
                hovermode='closest'
            )
        }
    )
])

if name == 'main':
    app.run_server(debug=True)