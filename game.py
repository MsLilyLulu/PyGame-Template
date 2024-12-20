import pygame
import sys

class GameWindow:
    def __init__(self, size: tuple[int, int], title: str) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def Render(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    win = GameWindow((800,500), "PyGame Window")
    win.Render()