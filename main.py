from dash import Dash, Input, Output
from views.Layout import Layout
from views.Graph import Graph
from views.SlideFilter import SliderFilter
from controllers.SliderFilterController import SliderFilterController

app = Dash(__name__)

Layout.render(
    app,
    title='Table data',
    content=(
        Graph.render(),
        *SliderFilter.render(title='Filtrar pelo eixo X', id='x-slider'),
        *SliderFilter.render(title='Filtrar pelo eixo Y', id='y-slider')
    )
)


@app.callback(
    Output("scatter-plot", "figure"),
    Input("x-slider", "value"),
    Input("y-slider", "value"),
)
def update(x_slider, y_slider):
    return SliderFilterController.update(x_slider, y_slider)


app.run_server(debug=True)
