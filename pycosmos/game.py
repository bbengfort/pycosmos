import os
import pygame

from .title import Title


ASSETS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")


class Game(object):
    """
    The primary controller of the pygame screen, the game has the primary game loop and
    run control system. A game is composed of multiple states, the active state is
    rendered on each loop of the game.
    """

    WIDTH = 1920
    HEIGHT = 1200

    def __init__(self):
        # Start up pygame
        pygame.init()

        # The canvas is the surface that states draw on
        self.canvas = pygame.Surface((self.WIDTH, self.HEIGHT))

        # Manage the screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Cosmos")

        # Set up the game
        self.running = False
        self.state_stack = []

        # Load assets and state
        self.load_assets()
        self.load_states()

    @property
    def state(self):
        """
        Returns the current state, e.g. the last state pushed on the stack.
        """
        return self.state_stack[-1]

    def run(self):
        self.running = True
        clock = pygame.time.Clock()

        # Primary game loop
        while self.running:
            # Get events
            self.events()

            # Do logical updates
            self.update()

            # Render the graphics here
            self.render()

            # wait until next frame (at 60 FPS)
            clock.tick(60)

        # When the game loop ends, quit pygame
        pygame.quit()

    def events(self):
        # Process player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.state.update()

    def render(self):
        # Render the state to the game canvas
        self.state.render(self.canvas)

        # Render the current state to the screen
        self.screen.blit(
            pygame.transform.scale(
                self.canvas, (self.WIDTH, self.HEIGHT)
            ),
            (0, 0),
        )
        pygame.display.flip()

    def load_assets(self):
        pass

    def load_states(self):
        self.title_screen = Title(self)
        self.title_screen.enter_state()
