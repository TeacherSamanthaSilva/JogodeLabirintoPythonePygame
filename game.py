import pygame
import sys

# Inicialização
pygame.init()
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirinto com Quadrado")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Jogador
player_size = 20
player_pos = [40, 40]
player_speed = 4

# Labirinto (lista de retângulos como paredes)
walls = [
    pygame.Rect(0, 0, WIDTH, 20),  # topo
    pygame.Rect(0, 0, 20, HEIGHT),  # esquerda
    pygame.Rect(0, HEIGHT - 20, WIDTH, 20),  # base
    pygame.Rect(WIDTH - 20, 0, 20, HEIGHT),  # direita
    pygame.Rect(100, 0, 20, 500),
    pygame.Rect(200, 100, 300, 20),
    pygame.Rect(300, 200, 20, 300),
    pygame.Rect(400, 0, 20, 400),
]

# Função para desenhar tudo
def draw():
    WIN.fill(WHITE)
    for wall in walls:
        pygame.draw.rect(WIN, BLACK, wall)
    pygame.draw.rect(WIN, BLUE, (*player_pos, player_size, player_size))
    pygame.display.update()

# Função para verificar colisão
def check_collision(rect):
    for wall in walls:
        if rect.colliderect(wall):
            return True
    return False

# Loop principal
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    new_pos = player_pos[:]
    if keys[pygame.K_LEFT]:
        new_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        new_pos[0] += player_speed
    if keys[pygame.K_UP]:
        new_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        new_pos[1] += player_speed

    new_rect = pygame.Rect(*new_pos, player_size, player_size)
    if not check_collision(new_rect):
        player_pos = new_pos

    draw()
