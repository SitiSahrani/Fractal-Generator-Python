import pygame
import numpy as np
import math

# Mandelbrot set parameters
xm, xM = -2, 1
ym, yM = -1.2, 1.2
sx, sy = 1.0, 1.0
u = 250  # Scaling factor

# Compute step size based on resolution
dx = xM - xm
dy = yM - ym
H = int(dx * u / sx)  # Convert to integer
V = int(dy * u / sy)  # Convert to integer
z = 1.0 / u  # Scale for pixels
max_iter = 512
jari = 100  # Escape radius squared


def mandelbrot_set(screen):
    for px in range(H):
        for py in range(V):
            x = xm + px * dx / H
            y = ym + py * dy / V
            r, s = 0, 0
            i = 0

            while i < max_iter and (r * r + s * s) < jari:
                t = r
                r = r * r - s * s + x
                s = 2 * t * s + y
                i += 1

            # Color Mapping
            if i < max_iter:
                t = (360 * i / max_iter) ** 1.5
                color = (
                    int(256 * math.sin(i)) % 256,
                    i % 256,
                    int(256 * (math.cos(i) + math.sin(i))) % 256,
                )
                screen.set_at((px, py), color)  # px, py sudah integer dari range()

def main():
    pygame.init()
    screen = pygame.display.set_mode((H, V))
    pygame.display.set_caption("Mandelbrot Set Fractal")
    screen.fill((0, 0, 0))  # Black background

    mandelbrot_set(screen)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()