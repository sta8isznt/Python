import sys

import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Game:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((1200, 800))

    def run(self):
        while True:
            self._check_events()
            self._update_screen()
            
            
    def _check_events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pg.KEYUP:
                    self._check_keyup_events(event)
                     

    def _check_keydown_events(self, event):
        pass

    def _check_keyup_events(self, event):
        pass

    def _update_screen(self):
        pg.display.flip()
        
         
my_game = Game()
my_game.run()