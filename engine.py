import math

# Constants
GAMMA = 1.4  # Heat capacity ratio for air
R = 287.05   # Gas constant [J/kg·K]
CP = 1005    # Specific heat at constant pressure [J/kg·K]
GRAVITY = 9.80665  # Gravity [m/s²]

class JetEngine:

    """
    Simulates the performance of a turbojet engine using basic thermodynamic priciples.
    Icludes afterburner functionality and calculates key performance metrics.
    """
    
    def __init__(
        self,
        altitude=10000, # metres
        compression_ratio=10,
        fuel_energy=43e6,              # Jet-A fuel energy [J/kg]
        eta_comp=0.85,
        eta_turb=0.85,
        mechanical_eff=0.9,
        nozzle_eff=0.9,
        flight_speed=1000,             
        fuel_air_ratio=0.045,
        use_afterburner=False,
        afterburner_fuel_fraction=0.03,
        drag_coefficient=0.01,
        frontal_area=0.9
    ):
        self.altitude = altitude
        self.T0, self.P0, self.air_density = self.isa_atmosphere(altitude)

        self.r = compression_ratio
        self.fuel_energy = fuel_energy
        self.eta_comp = eta_comp
        self.eta_turb = eta_turb
        self.mechanical_eff = mechanical_eff
        self.nozzle_eff = nozzle_eff
        self.V0 = flight_speed
        self.fuel_air_ratio = fuel_air_ratio
        self.use_afterburner = use_afterburner
        self.afterburner_fuel_fraction = afterburner_fuel_fraction
        self.drag_coefficient = drag_coefficient
        self.frontal_area = frontal_area

    def isa_atmosphere(self, altitude):

        """
        Calculates temperature, pressure, and density at a given altitude
        
        Parameters:
        altitude (float): Altitude in meters
        
        Returns:
        tuple: (Temperature in K, Pressure in Pa, Density in kg/m³)
        """
        if altitude < 11000:  # Troposphere
            T = 288.15 - 0.0065 * altitude 
            P = 101325 * (T / 288.15) ** (-(GRAVITY / (0.0065 * R)))
        else:
            T = 216.65
            P = 22632 * math.exp(-GRAVITY * (altitude - 11000) / (R * T))
        rho = P / (R * T)
        return T, P, rho

    def compressor(self):
        # Temperature after compression (isentropic efficiency included)
        T2 = self.T0 * (1 + ((self.r ** ((GAMMA - 1) / GAMMA) - 1) / self.eta_comp))
        # Pressure after compression (ideal)
        P2 = self.P0 * self.r
        return T2, P2

    def combustor(self, T2):
        fuel_input = self.fuel_air_ratio * self.fuel_energy
        T3 = T2 + fuel_input / (CP * (1 + self.fuel_air_ratio))
        return T3

    def turbine(self, T3, T2):
        T1 = self.T0
        comp_work = CP * (T2 - T1)  # Compressor work in temperature units
        turbine_work_needed = comp_work / self.mechanical_eff
        T4 = T3 - turbine_work_needed / (CP * (1 + self.fuel_air_ratio))
        return T4

    def afterburner(self, T4):
        extra_energy = self.afterburner_fuel_fraction * self.fuel_energy
        mass_total = 1 + self.fuel_air_ratio + self.afterburner_fuel_fraction
        T5 = T4 + extra_energy / (CP * mass_total)
        V_exit = math.sqrt(2 * self.nozzle_eff * CP * (T5 - self.T0))
        return T5, V_exit

    def nozzle_velocity(self, T_exit):
        return math.sqrt(2 * CP * (T_exit - self.T0)) * self.nozzle_eff

    def drag(self):
        return 0.5 * self.air_density * self.V0**2 * self.drag_coefficient * self.frontal_area

    def simulate(self):
        A_inlet = self.frontal_area
        T_inlet = self.T0
        P_inlet = self.P0
        rho = self.air_density
        M = self.V0 / math.sqrt(GAMMA * R * T_inlet)
        mass_flow = self.air_density * self.V0 * A_inlet
        self.mass_flow = mass_flow  
        
        T2, _ = self.compressor()
        T3 = self.combustor(T2)
        T4 = self.turbine(T3, T2)

        if self.use_afterburner:
            T_exit, V_exit = self.afterburner(T4)
            fuel_flow = (self.fuel_air_ratio + self.afterburner_fuel_fraction) * self.mass_flow
        else:
            T_exit = T4
            V_exit = self.nozzle_velocity(T_exit)
            fuel_flow = self.fuel_air_ratio * self.mass_flow

        gross_thrust = self.mass_flow * (V_exit - self.V0)
        net_thrust = gross_thrust - self.drag()

        # Handle zero or negative thrust cases safely
        if net_thrust <= 0:
            net_thrust = 0
            tsfc = float('inf')
            isp = 0
        else:
            tsfc = fuel_flow / net_thrust  # kg/N·s
            isp = net_thrust / (fuel_flow * GRAVITY)

        # Power calculations
        kinetic_power = 0.5 * self.mass_flow * (V_exit**2 - self.V0**2)
        fuel_power = fuel_flow * self.fuel_energy
        thermal_eff = kinetic_power / fuel_power if fuel_power else 0

        # Corrected propulsive efficiency for high-speed flows
        prop_eff = (2 * self.V0 * (V_exit - self.V0)) / (V_exit**2 + self.V0**2) if (V_exit > self.V0) else 0
        overall_eff = thermal_eff * prop_eff

        return {
            'Compressor Temp (T2)': T2,
            'Combustor Temp (T3)': T3,
            'Turbine/Exit Temp': T_exit,
            'Exhaust Velocity': V_exit,
            'Net Thrust': net_thrust,
            'Fuel Flow Rate': fuel_flow,
            'TSFC': tsfc,
            'Thermal Efficiency': thermal_eff,
            'Propulsive Efficiency': prop_eff,
            'Overall Efficiency': overall_eff,
            'Specific Impulse (Isp)': isp
        }

def print_results(title, result):
    print(f"=== {title} ===")
    print(f"Compressor Temp: {result['Compressor Temp (T2)']:.2f} K")
    print(f"Combustor Temp: {result['Combustor Temp (T3)']:.2f} K")
    print(f"Turbine/Nozzle Exit Temp: {result['Turbine/Exit Temp']:.2f} K")
    print(f"Exhaust Velocity: {result['Exhaust Velocity']:.2f} m/s")
    print(f"Thrust: {result['Net Thrust']:.2f} N")
    print(f"Fuel Flow Rate: {result['Fuel Flow Rate']:.4f} kg/s")
    print(f"TSFC: {result['TSFC'] * 1e6 if result['TSFC'] != float('inf') else float('inf'):.2f} mg/N·s")
    print(f"Thermal Efficiency: {result['Thermal Efficiency'] * 100:.2f} %")
    print(f"Propulsive Efficiency: {result['Propulsive Efficiency'] * 100:.2f} %")
    print(f"Overall Efficiency: {result['Overall Efficiency'] * 100:.2f} %")
    print(f"Specific Impulse (Isp): {result['Specific Impulse (Isp)']:.2f} s\n")

# Run simulation
base_engine = JetEngine(altitude=20000, use_afterburner=False)
ab_engine = JetEngine(altitude=20000, use_afterburner=True, afterburner_fuel_fraction=0.03)

base_results = base_engine.simulate()
ab_results = ab_engine.simulate()

# Print results
print_results("Base Engine (No Afterburner)", base_results)
print_results("Afterburning Engine", ab_results)
