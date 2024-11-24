import pygame as pg
import sys

class Game:
    def __init__(self):
        pg.init()

        #Screen Settings
        self.screen = pg.display.set_mode((1280, 700))
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("Pong Game")

        self.clock = pg.time.Clock()
    
    def run(self):
        while True:
            self._update_screen()
            self._check_events()
            self.clock.tick(60)

    def _update_screen(self):
        pg.draw.aaline(self.screen, 'white', self.screen_rect.midtop, self.screen_rect.midbottom)
        pg.display.update()

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        pass
    def _check_keyup_events(self, event):
        pass

if __name__ == "__main__":     
    my_game = Game()
    my_game.run()
