from src.snake_game import SnakeGame

WINDOW_WIDTH = 800
WINDOW_HEIGTH = 600

GAME_WIDTH = 800
GAME_HEIGTH = 600

FPS = 120
TITLE = "Snake Flood Fill"

game = SnakeGame(TITLE, WINDOW_WIDTH, WINDOW_HEIGTH, FPS)
game.run()

