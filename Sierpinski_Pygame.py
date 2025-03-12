import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
H, V = 500, 500
screen = pygame.display.set_mode((H, V))
pygame.display.set_caption("Sierpiński Gasket")

# Warna latar belakang hitam
screen.fill((0, 0, 0))

# Titik sudut segitiga
a = [
    (H // 2, 50),     # Titik atas
    (50, V - 50),     # Titik kiri bawah
    (H - 50, V - 50)  # Titik kanan bawah
]

# Pilih titik awal dari salah satu sudut segitiga
x, y = random.choice(a)

running = True
paused = False  # Status awal: tidak berhenti

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Jika klik tombol close (X)
            running = False
        elif event.type == pygame.KEYDOWN:  # Jika tombol keyboard ditekan
            paused = not paused  # Toggle (berhenti/jalan)

    if not paused:  # Jika tidak sedang berhenti, gambar fraktal
        # Pilih salah satu titik sudut secara acak
        x1, y1 = random.choice(a)

        # Pindah ke titik tengah antara titik saat ini dan titik sudut yang dipilih
        x = (x + x1) // 2
        y = (y + y1) // 2

        # Warna acak dalam format (R, G, B)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Gambar titik
        screen.set_at((x, y), color)

        # Update layar
        pygame.display.flip()


pygame.quit()
