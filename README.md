# 🖥️ Fractal Visualizations with Pygame

This project explores the fascinating world of **fractals**, demonstrating how simple mathematical rules can generate intricate and beautiful patterns. Built using **Python** and **Pygame**, this repository features three visually stunning fractal visualizations:

📌 **Overview**
This project showcases the following fractals:
- **Sierpiński Gasket** – A self-replicating triangular fractal generated using the Chaos Game.
- **Julia Set** – A complex-plane fractal created by iterating over complex numbers.
- **Mandelbrot Set** – A famous fractal that reveals infinite complexity through iterative calculations.

🛠 **Technologies Used**
- **Python** (for mathematical computations and graphics rendering)
- **Pygame** (for visualizing the fractals in an interactive environment)
- **NumPy** (for optimized calculations)

📂 **Dataset & Mathematical Background**
Fractals are generated based on mathematical formulas and iterative processes:
- **Sierpiński Gasket** uses midpoint displacement in a triangle.
- **Julia Set** follows the recursive formula:  
  $$z_{n+1} = z_n^2 + c$$  
  where **c** is a complex constant.
- **Mandelbrot Set** iterates the same equation, but with **c** representing each pixel's complex coordinate.

---

## ▶️ Running the Project
Ensure **Python 3.13** and **Pygame** are installed:

```bash
pip install pygame numpy
```

Run each fractal visualization using:
[Sierpinski_Pygame.py](Sierpinski_Pygame.py);
[JuliaSet_Pygame.py](JuliaSet_Pygame.py);
[Mandelbrot_Pygame.py](Mandelbrot_Pygame.py).

## 📊 Fractal Analysis & Output

### 1️⃣ **Sierpiński Gasket**
A triangle-based fractal generated by selecting midpoints iteratively.

**Controls:**
- **Press any key** to pause/resume.
- **Click (X)** to exit.

🎨 **Example Output:**
![Sierpiński Gasket](images/sierpinski_output.png)

---

### 2️⃣ **Julia Set**
A stunning fractal generated from complex number transformations.

🎨 **Example Output:**
![Julia Set](images/julia_output.png)

---

### 3️⃣ **Mandelbrot Set**
A world-famous fractal revealing infinite self-similarity.

🎨 **Example Output:**
![Mandelbrot Set](images/mandelbrot_output.png)

---

## 🎨 Customization & Further Exploration
Want to experiment with fractals? Try modifying:
- **Iteration depth** (for finer details)
- **Color schemes** (for visual appeal)
- **Complex constants** (in Julia Set for different patterns)

---

## 🤝 Contributing
Interested in contributing? Follow these steps:
1. **Fork** the repository.
2. **Create a new branch** for your changes.
3. **Submit a pull request** with your improvements.

---

## 📜 License
This project is licensed under the **MIT License** – feel free to use, modify, and share!

🚀 **Explore the beauty of fractals!**

