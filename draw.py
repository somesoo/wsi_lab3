import matplotlib.pyplot as plt
import pandas as pd
import re

# Wklejone dane jako tekst
raw_data = """
X(depth=1) vs O(depth=1) → {'X': 8, 'O': 1, 'Draw': 1}
X(depth=1) vs O(depth=2) → {'X': 3, 'O': 7, 'Draw': 0}
X(depth=1) vs O(depth=3) → {'X': 0, 'O': 7, 'Draw': 3}
X(depth=1) vs O(depth=4) → {'X': 1, 'O': 7, 'Draw': 2}
X(depth=1) vs O(depth=5) → {'X': 1, 'O': 5, 'Draw': 4}
X(depth=1) vs O(depth=6) → {'X': 0, 'O': 8, 'Draw': 2}
X(depth=1) vs O(depth=7) → {'X': 0, 'O': 6, 'Draw': 4}
X(depth=1) vs O(depth=8) → {'X': 0, 'O': 8, 'Draw': 2}
X(depth=1) vs O(depth=9) → {'X': 0, 'O': 7, 'Draw': 3}
X(depth=2) vs O(depth=1) → {'X': 10, 'O': 0, 'Draw': 0}
X(depth=2) vs O(depth=2) → {'X': 3, 'O': 0, 'Draw': 7}
X(depth=2) vs O(depth=3) → {'X': 4, 'O': 2, 'Draw': 4}
X(depth=2) vs O(depth=4) → {'X': 3, 'O': 2, 'Draw': 5}
X(depth=2) vs O(depth=5) → {'X': 1, 'O': 4, 'Draw': 5}
X(depth=2) vs O(depth=6) → {'X': 0, 'O': 1, 'Draw': 9}
X(depth=2) vs O(depth=7) → {'X': 0, 'O': 1, 'Draw': 9}
X(depth=2) vs O(depth=8) → {'X': 0, 'O': 1, 'Draw': 9}
X(depth=2) vs O(depth=9) → {'X': 0, 'O': 1, 'Draw': 9}
X(depth=3) vs O(depth=1) → {'X': 10, 'O': 0, 'Draw': 0}
X(depth=3) vs O(depth=2) → {'X': 4, 'O': 2, 'Draw': 4}
X(depth=3) vs O(depth=3) → {'X': 6, 'O': 1, 'Draw': 3}
X(depth=3) vs O(depth=4) → {'X': 3, 'O': 3, 'Draw': 4}
X(depth=3) vs O(depth=5) → {'X': 1, 'O': 2, 'Draw': 7}
X(depth=3) vs O(depth=6) → {'X': 0, 'O': 4, 'Draw': 6}
X(depth=3) vs O(depth=7) → {'X': 0, 'O': 2, 'Draw': 8}
X(depth=3) vs O(depth=8) → {'X': 0, 'O': 3, 'Draw': 7}
X(depth=3) vs O(depth=9) → {'X': 0, 'O': 1, 'Draw': 9}
X(depth=4) vs O(depth=1) → {'X': 9, 'O': 1, 'Draw': 0}
X(depth=4) vs O(depth=2) → {'X': 8, 'O': 1, 'Draw': 1}
X(depth=4) vs O(depth=3) → {'X': 5, 'O': 2, 'Draw': 3}
X(depth=4) vs O(depth=4) → {'X': 4, 'O': 0, 'Draw': 6}
X(depth=4) vs O(depth=5) → {'X': 2, 'O': 1, 'Draw': 7}
X(depth=4) vs O(depth=6) → {'X': 0, 'O': 1, 'Draw': 9}
X(depth=4) vs O(depth=7) → {'X': 0, 'O': 1, 'Draw': 9}
X(depth=4) vs O(depth=8) → {'X': 0, 'O': 1, 'Draw': 9}
X(depth=4) vs O(depth=9) → {'X': 0, 'O': 1, 'Draw': 9}
X(depth=5) vs O(depth=1) → {'X': 10, 'O': 0, 'Draw': 0}
X(depth=5) vs O(depth=2) → {'X': 7, 'O': 1, 'Draw': 2}
X(depth=5) vs O(depth=3) → {'X': 9, 'O': 0, 'Draw': 1}
X(depth=5) vs O(depth=4) → {'X': 7, 'O': 1, 'Draw': 2}
X(depth=5) vs O(depth=5) → {'X': 7, 'O': 1, 'Draw': 2}
X(depth=5) vs O(depth=6) → {'X': 0, 'O': 1, 'Draw': 9}
X(depth=5) vs O(depth=7) → {'X': 0, 'O': 2, 'Draw': 8}
X(depth=5) vs O(depth=8) → {'X': 0, 'O': 3, 'Draw': 7}
X(depth=5) vs O(depth=9) → {'X': 0, 'O': 1, 'Draw': 9}
X(depth=6) vs O(depth=1) → {'X': 10, 'O': 0, 'Draw': 0}
X(depth=6) vs O(depth=2) → {'X': 9, 'O': 0, 'Draw': 1}
X(depth=6) vs O(depth=3) → {'X': 9, 'O': 0, 'Draw': 1}
X(depth=6) vs O(depth=4) → {'X': 7, 'O': 0, 'Draw': 3}
X(depth=6) vs O(depth=5) → {'X': 4, 'O': 0, 'Draw': 6}
X(depth=6) vs O(depth=6) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=6) vs O(depth=7) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=6) vs O(depth=8) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=6) vs O(depth=9) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=7) vs O(depth=1) → {'X': 10, 'O': 0, 'Draw': 0}
X(depth=7) vs O(depth=2) → {'X': 5, 'O': 0, 'Draw': 5}
X(depth=7) vs O(depth=3) → {'X': 9, 'O': 0, 'Draw': 1}
X(depth=7) vs O(depth=4) → {'X': 6, 'O': 0, 'Draw': 4}
X(depth=7) vs O(depth=5) → {'X': 6, 'O': 0, 'Draw': 4}
X(depth=7) vs O(depth=6) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=7) vs O(depth=7) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=7) vs O(depth=8) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=7) vs O(depth=9) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=8) vs O(depth=1) → {'X': 10, 'O': 0, 'Draw': 0}
X(depth=8) vs O(depth=2) → {'X': 8, 'O': 0, 'Draw': 2}
X(depth=8) vs O(depth=3) → {'X': 7, 'O': 0, 'Draw': 3}
X(depth=8) vs O(depth=4) → {'X': 9, 'O': 0, 'Draw': 1}
X(depth=8) vs O(depth=5) → {'X': 8, 'O': 0, 'Draw': 2}
X(depth=8) vs O(depth=6) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=8) vs O(depth=7) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=8) vs O(depth=8) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=8) vs O(depth=9) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=9) vs O(depth=1) → {'X': 10, 'O': 0, 'Draw': 0}
X(depth=9) vs O(depth=2) → {'X': 9, 'O': 0, 'Draw': 1}
X(depth=9) vs O(depth=3) → {'X': 6, 'O': 0, 'Draw': 4}
X(depth=9) vs O(depth=4) → {'X': 8, 'O': 0, 'Draw': 2}
X(depth=9) vs O(depth=5) → {'X': 9, 'O': 0, 'Draw': 1}
X(depth=9) vs O(depth=6) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=9) vs O(depth=7) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=9) vs O(depth=8) → {'X': 0, 'O': 0, 'Draw': 10}
X(depth=9) vs O(depth=9) → {'X': 0, 'O': 0, 'Draw': 10}
"""

# Parsowanie danych
pattern = r"X\(depth=(\d+)\) vs O\(depth=(\d+)\) → {'X': (\d+), 'O': (\d+), 'Draw': (\d+)}"
data = re.findall(pattern, raw_data)

df = pd.DataFrame(data, columns=["X_depth", "O_depth", "X_wins", "O_wins", "Draws"]).astype(int)

# Przekształcenie do formy macierzy
pivot_x = df.pivot(index="X_depth", columns="O_depth", values="X_wins")
pivot_o = df.pivot(index="X_depth", columns="O_depth", values="O_wins")
pivot_d = df.pivot(index="X_depth", columns="O_depth", values="Draws")

# Rysowanie wykresów
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

im0 = axs[0].imshow(pivot_x, cmap="Blues", origin="lower")
axs[0].set_title("Wygrane gracza X")
axs[0].set_xlabel("Głębokość gracza O")
axs[0].set_ylabel("Głębokość gracza X")
fig.colorbar(im0, ax=axs[0])

im1 = axs[1].imshow(pivot_o, cmap="Reds", origin="lower")
axs[1].set_title("Wygrane gracza O")
axs[1].set_xlabel("Głębokość gracza O")
axs[1].set_ylabel("Głębokość gracza X")
fig.colorbar(im1, ax=axs[1])

im2 = axs[2].imshow(pivot_d, cmap="Greens", origin="lower")
axs[2].set_title("Remisy")
axs[2].set_xlabel("Głębokość gracza O")
axs[2].set_ylabel("Głębokość gracza X")
fig.colorbar(im2, ax=axs[2])

plt.suptitle("Wyniki gier X vs O przy różnych głębokościach Min-Max")
plt.tight_layout()
plt.show()
