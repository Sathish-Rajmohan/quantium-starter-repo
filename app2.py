# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("task2.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

fig = px.line(df, x="Date", y="Sales", title="Pink Morsel sales over time", labels={"Date": "Date", "Sales": "Sales in $"}, color="Region")

app.layout = html.Div(style={"fontFamily": "Times New Roman", "maxWidth": "900px", "margin": "0 auto", "padding": "20px", "backgroundColor": "#03fb7f"}, children=[
    html.H1("Pink Morsel sales visualiser", style={"textAlign": "center", "color": "#dc240f"}),

    html.Div(style={"textAlign": "center", "marginBottom": "20px"}, children=[
        dcc.RadioItems(
            id="region_filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            labelStyle={"marginRight": "20px", "fontSize": "16px"}
        )
    ]),
    dcc.Graph(id="sales_graph")
])

@callback(Output("sales_graph", "figure"), Input("region_filter", "value"))
def update_graph(region):
    filtered = df if region == "all" else df[df["Region"] == region]
    return px.line(filtered, x="Date", y="Sales", title="Pink Morsel Sales Over Time", labels={"Date": "Date", "Sales": "Sales in $"})

if __name__ == '__main__':
    app.run(debug=True)