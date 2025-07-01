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
=== Base Engine (No Afterburner) ===
Compressor Temp: 453.87 K
Combustor Temp: 2296.33 K
Turbine/Nozzle Exit Temp: 2044.10 K
Exhaust Velocity: 1724.90 m/s
Thrust: 57038.20 N
Fuel Flow Rate: 3.5654 kg/s
TSFC: 62.51 mg/N·s
Thermal Efficiency: 51.04 %
Propulsive Efficiency: 36.47 %
Overall Efficiency: 18.61 %
Specific Impulse (Isp): 1631.32 s

=== Afterburning Engine ===
Compressor Temp: 453.87 K
Combustor Temp: 2296.33 K
Turbine/Nozzle Exit Temp: 3238.13 K
Exhaust Velocity: 2337.92 m/s
Thrust: 105608.17 N
Fuel Flow Rate: 5.9423 kg/s
TSFC: 56.27 mg/N·s
Thermal Efficiency: 69.24 %
Propulsive Efficiency: 41.38 %
Overall Efficiency: 28.65 %
Specific Impulse (Isp): 1812.27 s

Kacper Kowalski - 2025
