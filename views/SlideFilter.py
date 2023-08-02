from dash import dcc, html


class SliderFilter:

    @staticmethod
    def render(title, id):
        return (
            html.P(title),
            dcc.RangeSlider(
                id=id,
                min=0, max=100, step=1,
                marks={0: '0', 20: '20', 40: '40', 60: '60', 80: '80', 100: '100'},
                value=[0, 100]
            )
        )
