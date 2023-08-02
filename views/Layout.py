from dash import html


class Layout:
    @staticmethod
    def render(app, title, content):
        app.layout = html.Div([
            html.H2(title),
            *content,
        ])
