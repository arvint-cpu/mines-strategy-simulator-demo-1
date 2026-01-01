# Mines Demo 1 – Console Prototype

This is **Demo 1**, the earliest prototype in the progression toward  
**Mines Strategy Simulator**.

It is a **console-based Mines-style game** written in pure Python, created to
experiment with:
- grid logic
- random mine placement
- balance tracking
- multipliers
- basic risk–reward mechanics

---

## Disclaimer

**Educational / simulation only.**
- No real money
- No gambling
- For learning and experimentation purposes only

---

## Purpose of This Demo

The goal of this demo was **not polish**, but understanding fundamentals:

- How to represent a grid in Python
- How to track revealed vs hidden cells
- How to randomly place mines without duplicates
- How a multiplier can increase with successful moves
- How risk affects balance over time

This prototype directly inspired later GUI-based versions.

---

## How the Game Works

- Grid size: **5 × 5**
- Mines are placed randomly at the start
- Each move:
  - Costs a fixed bet amount
  - Reveals one cell
- If the cell is safe:
  - Multiplier increases
- If the cell contains a mine:
  - Game ends immediately

At the end:
- The full grid is revealed
- Final balance and reward are calculated

---

## How to Run

Make sure you have **Python 3** installed.

```bash
python main.py
