import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np


app = dash.Dash()
server = app.server


df_nse = pd.read_csv("./data.csv")

df_nse["Date"] = pd.to_datetime(df_nse.Date, format="%Y-%m-%d")
df_nse.index = df_nse['Date']


data = df_nse.sort_index(ascending=True, axis=0)
new_data = pd.DataFrame(index=range(0, len(df_nse)), columns=[
                        'Date', 'Close', 'High', 'Low'])

for i in range(0, len(data)):
    new_data["Date"][i] = data['Date'][i]
    new_data["Close"][i] = data["Close"][i]
    new_data["High"][i] = data["High"][i]
    new_data["Low"][i] = data["Low"][i]

new_data.index = new_data.Date
new_data.drop("Date", axis=1, inplace=True)


# __________________________

trace1 = []
trace2 = []
trace1.append(
    go.Scatter(x=new_data.index,
               y=new_data["High"],
               mode='lines', opacity=0.7,
               name=f'High'))
trace2.append(
    go.Scatter(x=new_data.index,
               y=new_data["Low"],
               mode='lines', opacity=0.6,
               name=f'Low'))
traces = [trace1, trace2]
data = [val for sublist in traces for val in sublist]

# __________________________

app.layout = html.Div([

    html.H1("Stock Price Analysis Dashboard", style={"textAlign": "center"}),

    dcc.Tabs(id="tabs", children=[

        dcc.Tab(label='Closing Rates', children=[
            html.Div([
                dcc.Graph(
                    id="Actual Data",
                    figure={
                        "data": [
                            go.Scatter(
                                x=new_data.index,
                                y=new_data["Close"],
                                mode='lines'
                            )

                        ],
                        "layout":go.Layout(
                            title='Closer Plot',
                            height=600,
                            xaxis={'title': 'Date',
                                   'rangeselector': {'buttons': list([{'count': 1, 'label': '1M',
                                                                       'step': 'month',
                                                                       'stepmode': 'backward'},
                                                                      {'count': 6, 'label': '6M',
                                                                       'step': 'month',
                                                                       'stepmode': 'backward'},
                                                                      {'step': 'all'}])},
                                   'rangeslider': {
                                       'visible': True}, 'type': 'date'},
                            yaxis={'title': 'Closing Rate'}
                        )
                    }

                )
            ])


        ]),
        dcc.Tab(label='Stocks High vs Lows', children=[
            html.Div([
                dcc.Graph(id='highlow',
                          figure={
                              'data': data,
                              'layout': go.Layout(
                                  colorway=["#5E0DAC", '#FF4F00', '#375CB1',
                                            '#FF7400', '#FFF400', '#FF0056'],
                                  height=600,
                                  title=f"High and Low Prices Over Time",
                                  legend=dict(
                                      orientation="h",
                                      yanchor="bottom",
                                      y=1.02,
                                      xanchor="right",
                                      x=1
                                  ),
                                  xaxis={"title": "Date",
                                         'rangeselector':
                                         {'buttons': list([{'count': 1, 'label': '1M',
                                                            'step': 'month',
                                                            'stepmode': 'backward'},
                                                           {'count': 6, 'label': '6M',
                                                            'step': 'month',
                                                            'stepmode': 'backward'},
                                                           {'step': 'all'}])},
                                         'rangeslider': {'visible': True}, 'type': 'date'
                                         },
                                  yaxis={"title": "Price (INR)"})}),

            ], className="container"),
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
