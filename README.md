# Jet Engine Performance Simulator

A simple Python simulation of a turbojet engine with and without afterburner capabilities.

## Features

- Simulates jet engine thermodynamics and thrust generation.
- Calculates thrust, fuel efficiency, thermal & propulsive efficiency, TSFC, and more.
- Supports GUI input for parameter tuning.
- Visualizes performance comparisons via bar graphs.

## Project Structure

- `engine.py`: Core simulation logic.
- `main.py`: CLI entry point.
- `gui.py`: GUI for user interaction (Tkinter).
- `visualize.py`: Visualization of engine metrics (Matplotlib).
- `README.md`: Project documentation.

## How to Run

1. **Install dependencies (if needed):**
    ```bash
    pip install matplotlib
    ```

2. **Command Line Simulation:**
    ```bash
    python main.py
    ```

3. **GUI Simulation:**
    ```bash
    python gui.py
    ```

4. **Visualization:**
    ```bash
    python visualize.py
    ```

## Example Output

=== Jet Engine (No Afterburner) ===
Compressor Temp: 399.55 K
Combustor Temp: 1978.33 K

Kacper Kowalski - 2025