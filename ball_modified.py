from ball import Ball


class BallWithPause(Ball):

    def __init__(self, xy, vector, game_screen, paused=False):
        super().__init__(xy, vector, game_screen)
        self.paused = paused

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def toogle(self):
        self.paused = not self.paused

    def calcnewpos(self,rect,vector):
        # if it is not allowed to move return the same position
        if not self.paused:
            return super().calcnewpos(rect, vector)
        else:
            return self.rect
        
