from dash import dcc


class Graph:
    @staticmethod
    def render():
        return dcc.Graph(id="scatter-plot")
