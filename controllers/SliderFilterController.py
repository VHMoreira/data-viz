from models.TableData import TableData
import plotly.express as px


class SliderFilterController:

    @staticmethod
    def update(x_slider, y_slider):
        data = TableData()
        data.read()

        low_x, high_x = x_slider
        low_y, high_y = y_slider

        fig = px.scatter(
            data.data_frame,
            data.position_x,
            data.position_y,
            color=data.colours,
            size=data.sizes,
            symbol=data.shapes,
            labels={
                'cor': 'Cor',
                'symbol': 'Forma',
                'x': 'Posição X',
                'y': 'Posição Y'
            },
            range_x=[low_x, high_x],
            range_y=[low_y, high_y],
        )

        fig.update_layout(showlegend=False)

        return fig