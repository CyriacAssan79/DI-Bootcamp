import time
import copy


class GameOfLife:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_alive(self, row, col):
        """Rend une cellule vivante"""
        self.grid[row][col] = 1

    def display(self):
        """Affiche la grille"""
        for row in self.grid:
            print(" ".join("■" if cell else "." for cell in row))
        print()

    def count_neighbors(self, row, col):
        """Compte les voisins vivants"""

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        count = 0

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                count += self.grid[nr][nc]

        return count

    def next_generation(self):

        new_grid = copy.deepcopy(self.grid)

        for r in range(self.rows):
            for c in range(self.cols):

                neighbors = self.count_neighbors(r, c)

                # Règle 1 et 3
                if self.grid[r][c] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[r][c] = 0

                # Règle 2
                elif self.grid[r][c] == 0:
                    if neighbors == 3:
                        new_grid[r][c] = 1

        self.grid = new_grid

    def run(self, generations, delay=0.5):

        for generation in range(generations):

            print(f"Generation {generation}")
            self.display()

            self.next_generation()

            time.sleep(delay)

game = GameOfLife(10, 10)

game.set_alive(1, 2)
game.set_alive(2, 3)
game.set_alive(3, 1)
game.set_alive(3, 2)
game.set_alive(3, 3)

game.run(20)