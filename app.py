# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("task2.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

fig = px.line(df, x="Date", y="Sales", title="Pink Morsel Sales Over Time", labels={"Date": "Date", "Sales": "Sales in $"},color="Region")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Visualiser'),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)