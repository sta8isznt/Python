import pygame
import pygame.freetype

pygame.init()

screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Module Basic Functions")

white = (255, 255, 255)
black = (0, 0, 0)
green = (144, 238, 144)
orange = (255, 165, 0)
blue = (173, 216, 230)
yellow = (255, 255, 102)
red = (255, 99, 71)
purple = (218, 112, 214)
light_gray = (211, 211, 211)

pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 24)
title_font = pygame.font.Font(pygame.font.get_default_font(), 36)

def draw_text_box(surface, x, y, width, height, text_list, color, title):
    shadow_offset = 5
    shadow_color = light_gray
    pygame.draw.rect(surface, shadow_color, (x + shadow_offset, y + shadow_offset, width, height), border_radius=10)
    pygame.draw.rect(surface, color, (x, y, width, height), border_radius=10)
    pygame.draw.rect(surface, black, (x, y, width, height), 2, border_radius=10)
    title_surf = font.render(title, True, black)
    surface.blit(title_surf, (x + 10, y - 30))
    for i, line in enumerate(text_list):
        text_surf = font.render(line, True, black)
        surface.blit(text_surf, (x + 10, y + 35 + i * 30))

functions = [
    {
        "title": "Surface",
        "color": green,
        "text": ["blit(source, dest)", "fill(color, rect=None)", "convert()", "get_at((x, y))"],
        "pos": (50, 150, 350, 200),
    },
    {
        "title": "Rect",
        "color": orange,
        "text": ["colliderect(rect)", "move(x, y)", "inflate(x, y)", "clip(rect)"],
        "pos": (450, 150, 350, 200),
    },
    {
        "title": "Color",
        "color": blue,
        "text": ["normalize()", "correct_gamma(gamma)", "hsva"],
        "pos": (850, 150, 350, 150),
    },
    {
        "title": "Font",
        "color": yellow,
        "text": ["render(text, antialias, color)", "size(text)", "set_underline(value)"],
        "pos": (50, 400, 350, 150),
    },
    {
        "title": "event",
        "color": red,
        "text": ["get()", "poll()", "post(Event)", "set_grab(bool)"],
        "pos": (450, 400, 350, 200),
    },
    {
        "title": "time",
        "color": purple,
        "text": ["Clock().tick(framerate)", "delay(milliseconds)", "get_ticks()"],
        "pos": (850, 400, 350, 150),
    },
    {
        "title": "display",
        "color": green,
        "text": ["set_mode((width, height))", "flip()", "update()", "set_caption(title)"],
        "pos": (50, 600, 350, 150),
    },
]

def draw_gradient_background(surface, color1, color2):
    for y in range(screen_height):
        color = [
            color1[i] + (color2[i] - color1[i]) * y // screen_height
            for i in range(3)
        ]
        pygame.draw.line(surface, color, (0, y), (screen_width, y))

running = True
while running:
    draw_gradient_background(screen, white, light_gray)

    title_surf = title_font.render("PYGAME MODULE BASIC FUNCTIONS", True, black)
    screen.blit(title_surf, (screen_width // 2 - title_surf.get_width() // 2, 50))

    for func in functions:
        draw_text_box(screen, *func["pos"], func["text"], func["color"], func["title"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
