CIRCLE_RADIUS = 60
SQUARE_SIDE = 30
FIGURE_WIDTH = 10


class Piece:
    def __init__(self, id) -> None:
        self.round = bool(id//8)
        self.blue = bool(id%8//4)
        self.tall = bool(id%8%4//2)
        self.pinched = bool(id%8%4%2)
