import random

# Constants
GRID_SIZE = 5
NUM_MINES = 3
INITIAL_BALANCE = 100
BET_AMOUNT = 5
MULTIPLIER_INCREMENT = 0.5

# Initialize the grid
grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
mines = []

# Place mines randomly
for _ in range(NUM_MINES):
    while True:
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if (x, y) not in mines:
            mines.append((x, y))
            grid[x][y] = 'M'  # 'M' represents a mine
            break

# Function to display the grid
def display_grid():
    print("\n  " + " ".join(str(i) for i in range(GRID_SIZE)))
    for i in range(GRID_SIZE):
        print(i, end=" ")
        for j in range(GRID_SIZE):
            if revealed[i][j]:
                print(grid[i][j], end=" ")
            else:
                print(".", end=" ")
        print()

# Main game loop
def main():
    balance = INITIAL_BALANCE
    multiplier = 1.0
    print("Welcome to Mines Gambling Game!")
    print(f"Starting balance: ${balance}")
    print(f"Each move costs ${BET_AMOUNT}. Avoid the mines to win!")

    while balance >= BET_AMOUNT:
        print(f"\nCurrent balance: ${balance}")
        print(f"Current multiplier: {multiplier:.1f}x")
        display_grid()

        # Ask for cell to reveal
        while True:
            try:
                x = int(input("Enter row: "))
                y = int(input("Enter column: "))
                if x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
                    print("Invalid input. Try again.")
                    continue
                if revealed[x][y]:
                    print("You already revealed this cell. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Try again.")

        # Deduct bet amount
        balance -= BET_AMOUNT

        # Reveal the cell
        revealed[x][y] = True
        if (x, y) in mines:
            print("Boom! You hit a mine. Game over!")
            break
        else:
            multiplier += MULTIPLIER_INCREMENT
            print(f"Safe! Multiplier increased to {multiplier:.1f}x.")

    # End of game
    if balance < BET_AMOUNT:
        print("\nYou ran out of balance. Game over!")
    else:
        print("\nYou chose to stop. Game over!")

    # Reveal all cells at the end
    print("\nFinal Grid:")
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            revealed[i][j] = True
    display_grid()

    # Calculate final reward
    final_reward = BET_AMOUNT * multiplier
    print(f"\nFinal multiplier: {multiplier:.1f}x")
    print(f"Final reward: ${final_reward:.2f}")
    print(f"Final balance: ${balance + final_reward:.2f}")

if __name__ == "__main__":
    main()
