class Stats():
    """checking statistic"""

    def __init__(self):
        """initialization of statistic"""
        self.reset_stats()
        self.run_game = True
        self.menu_displayed = False
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())
        
    def reset_stats(self):
        """game statistic"""
        self.cannons_left = 1
        self.score = 0
        self.level = 1
