import pandas as pd
import plotly.express as px  # (version 4.7.0)

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv("American_Bear.csv")

df2 = df['Location'].str.replace('near', '')

df2 =df2.str.split(',', expand=True)
df2.rename(columns={0:'City',
                  1:'State'},
          inplace=True, errors='raise')
df_col = pd.concat([df, df2], axis=1)


df_bear = pd.read_csv('Bear_Geo.csv')

# ------------------------------------------------------------------------------
# App layout
app.layout = dbc.Container([
    html.H1("Bear Attack Dashboard", style={'text-align': 'center'}),

    dcc.Dropdown(id="Slct_bear",
                 options=[
                     {"label": "Polar Bear", "value": 'Polar Bear'},
                     {"label": "Black Bear", "value": 'Black bear'},
                     {"label": "Brown Bear", "value": 'Brown bear'}],
                 multi=False,
                 value='Polar Bear',
                 style={'width': "40%"},
                 clearable = False,
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='bear_graph', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='bear_graph', component_property='figure')],
    [Input(component_id='Slct_bear', component_property='value')]

)
def update_graph(Selct_bear):
    print(Selct_bear)
    print(type(Selct_bear))

    container = "The bear chosen by user was: {}".format(Selct_bear)

    dff = df_bear
    dff = dff[dff["Type of bear"] == Selct_bear]

    # Plotly Express
    fig = px.scatter_mapbox(dff, lat="lat", lon="lng", hover_name="City", hover_data=["Name", "State", "Type of bear"],
                            #color_discrete_sequence=["fuchsia"], zoom=3, height=500)
                            color='Type of bear', zoom=3, height=500)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 10, "t": 10, "l": 10, "b": 10})
    fig.show()

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
