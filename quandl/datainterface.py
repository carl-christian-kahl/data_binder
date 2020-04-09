import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dataloadinterface
import dataanalytics

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

tabs = dbc.Tabs(
    [
        dbc.Tab(dataanalytics.tab_content, label="Data analytics"),
        dbc.Tab(dataloadinterface.tab_content, label="Data load"),
    ]
)

app.layout = dbc.Container(
    tabs,
    className="p-5",
)

if __name__ == "__main__":
    app.run_server()