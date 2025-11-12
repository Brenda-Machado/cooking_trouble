"""
Cooking Trouble.

Constantes globais da aplicação.

constants.py
"""

# Dimensões da Tela
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Dimensões de Entidades
PLAYER_SIZE = (55, 55)
ENEMY_PERSON_SIZE = (55, 55)
DELIVERY_POINT_SIZE = (120, 120)

# Velocidades
PLAYER_SPEED = 7
ENEMY_PERSON_SPEED = 3
KNOCKBACK_MULTIPLIER = 2

# Raios de Interação
ENEMY_DETECTION_RADIUS = 300
ENEMY_PATROL_RADIUS = 20
ITEM_INTERACTION_RADIUS = 120
DELIVERY_POINT_RADIUS = 120

# Cores
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN_DARK = (34, 139, 34)
COLOR_ORANGE = (255, 140, 0)
COLOR_RED_DARK = (128, 0, 0)

# Estados do Jogo
class GameState:
    MAIN_MENU = "main_menu"
    DIFFICULTY_MENU = "difficulty_menu"
    TUTORIAL = "tutorial"
    GAMEPLAY = "gameplay"
    PAUSED = "paused"
    VICTORY = "victory"
    DEFEAT = "defeat"
    CREDITS = "credits"

# Níveis de Dificuldade
class DifficultyLevel:
    EASY = 0
    MEDIUM = 1
    HARD = 2

# Mapeamento para requisições
DIFFICULTY_NAMES = {
    DifficultyLevel.EASY: "Fácil",
    DifficultyLevel.MEDIUM: "Médio",
    DifficultyLevel.HARD: "Difícil"
}
