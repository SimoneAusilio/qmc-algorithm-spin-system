class Square:
    "creating a class square for the chessboard"
    "Square of a chessboard defining its type "
    def __init__(self, sqr_type):
        self.square_type = sqr_type

    def _update(self, sqr_type):
        "update the attribute of the square"
        self.square_type = sqr_type
    
    def _get_square_type(self):
        return self.square_type