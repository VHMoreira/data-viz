import pandas as pd

shape = {
    'quad': 'square',
    'circulo': 'circle',
    'triangulo': 'triangle-up',
    'estrela': 'star',
    'asteristico': 'asterisk',
    'x': 'x'
}


class TableData:
    def __init__(self):
        self.data_frame = None
        self.position_x = []
        self.position_y = []
        self.shapes = []
        self.colours = []
        self.sizes = []

    def read(self):
        self.data_frame = pd.read_csv("static/data.csv", delimiter=',')

        for row in self.data_frame['posicao']:
            x, y = row.replace('(', '').replace(')', '').split('/')
            self.position_x.append(int(x))
            self.position_y.append(int(y))

        for row in self.data_frame['forma']:
            self.shapes.append(shape[row])

        self.colours = self.data_frame['cor']
        self.sizes = self.data_frame['tamanho']
