class GameStats:
    def __init__(self,game):
        self.settings = game.settings
        self.reset_stats()

        self.game_active = False
        self.set_high_score()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def set_high_score(self):
        with open(self.settings.filename) as file:
            contents = file.read()
        self.high_score = int(contents)