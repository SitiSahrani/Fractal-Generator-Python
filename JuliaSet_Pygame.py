import pygame
import numpy as np
import math

# Window dimensions
H, V = 800, 600  # Equivalent to width (H) and height (V)

# Julia set parameters
xm, xM = -0.8, -0.2
ym, yM = -0.3, 0.3
max_iter = 512
jari = 100  # Escape radius squared
c_real, c_imag = -0.7488, 0.107421  # Constant for Julia set

# Compute step size based on resolution
dx = xM - xm
dy = yM - ym
z = dx / H  # Scale for pixels


def julia_set(screen):
    for px in range(H):
        for py in range(V):
            x = xm + px * dx / H
            y = ym + py * dy / V
            r, s = x, y
            i = 0

            while i < max_iter and (r * r + s * s) < jari:
                t = r
                r = r * r - s * s + c_real
                s = 2 * t * s + c_imag
                i += 1

            # Color Mapping
            if i < max_iter:
                t = (360 * i / max_iter) ** 1.5
                color = (
                    int(256 * math.sin(i)) % 256,
                    i % 256,
                    int(256 * (math.cos(i) + math.sin(i))) % 256,
                )
                screen.set_at((px, py), color)


def main():
    pygame.init()
    screen = pygame.display.set_mode((H, V))
    pygame.display.set_caption("Julia Set Fractal")
    screen.fill((0, 0, 0))  # Black background

    julia_set(screen)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
