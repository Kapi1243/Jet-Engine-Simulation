import matplotlib.pyplot as plt
import numpy as np
from engine import JetEngine

def plot_thrust_vs_speed():
    speeds = np.linspace(100, 1500, 50)
    thrust = []

    for v in speeds:
        engine = JetEngine(flight_speed=v)
        result = engine.simulate()
        thrust.append(result['Net Thrust'])

    plt.figure(figsize=(10, 6))
    plt.plot(speeds, thrust, label="Net Thrust", color='blue')
    plt.title("Thrust vs Flight Speed")
    plt.xlabel("Flight Speed (m/s)")
    plt.ylabel("Thrust (N)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_efficiency_vs_compression():
    ratios = np.linspace(5, 30, 50)
    thermal_eff = []
    prop_eff = []
    overall_eff = []

    for r in ratios:
        engine = JetEngine(compression_ratio=r)
        result = engine.simulate()
        thermal_eff.append(result['Thermal Efficiency'] * 100)
        prop_eff.append(result['Propulsive Efficiency'] * 100)
        overall_eff.append(result['Overall Efficiency'] * 100)

    plt.figure(figsize=(10, 6))
    plt.plot(ratios, thermal_eff, label="Thermal Efficiency")
    plt.plot(ratios, prop_eff, label="Propulsive Efficiency")
    plt.plot(ratios, overall_eff, label="Overall Efficiency")
    plt.title("Efficiency vs Compression Ratio")
    plt.xlabel("Compression Ratio")
    plt.ylabel("Efficiency (%)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_isp_vs_altitude():
    altitudes = np.linspace(0, 25000, 50)
    isp = []

    for alt in altitudes:
        engine = JetEngine(altitude=alt)
        result = engine.simulate()
        isp.append(result['Specific Impulse (Isp)'])

    plt.figure(figsize=(10, 6))
    plt.plot(altitudes, isp, label="Specific Impulse (Isp)", color='green')
    plt.title("Specific Impulse vs Altitude")
    plt.xlabel("Altitude (m)")
    plt.ylabel("Specific Impulse (s)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_thrust_vs_speed()
    plot_efficiency_vs_compression()
    plot_isp_vs_altitude()