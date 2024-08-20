import sys

import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_BLUE = (44, 44, 127)

class Game:
    def __init__(self):
        pg.init()

        #Screen Settings
        self.screen = pg.display.set_mode((1200, 800))
        pg.display.set_caption("Game Name")

        #Clock Settings
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            
            
    def _check_events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit() #uninitializes all te pygame modules
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pg.KEYUP:
                    self._check_keyup_events(event)

    def _update_screen(self):
        pg.display.update() #Better than flip()

    def _check_keydown_events(self, event):
        pass

    def _check_keyup_events(self, event):
        pass
        
if __name__ == '__main__':        
    my_game = Game()
    my_game.run()