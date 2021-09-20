CIRCLE_RADIUS = 50
SQUARE_SIDE = 30
FIGURE_WIDTH = 50
PINCH_RADIUS = 30
PINCH_WIDTH = 30
CONTOUR_WIDTH = 5
CONTOUR_RADIUS = CIRCLE_RADIUS + CONTOUR_WIDTH


class Piece:
    def __init__(self, id) -> None:
        self.round = bool(id//8)
        self.blue = bool(id%8//4)
        self.tall = bool(id%8%4//2)
        self.pinched = bool(id%8%4%2)
