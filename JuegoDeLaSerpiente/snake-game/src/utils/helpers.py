def generate_random_position(width, height):
    import random
    return (random.randint(0, width - 1), random.randint(0, height - 1))

def check_collision(pos1, pos2):
    return pos1 == pos2

def is_out_of_bounds(position, width, height):
    x, y = position
    return x < 0 or x >= width or y < 0 or y >= height

def draw_text(surface, text, position, font, color):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)