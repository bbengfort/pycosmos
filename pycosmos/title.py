from .state import State


class Title(State):

    def __init__(self, game):
        super(Title, self).__init__(game)

    def update(self):
        pass

    def render(self, canvas):
        canvas.fill((99, 99, 99))
