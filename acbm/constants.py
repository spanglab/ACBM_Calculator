####### Fixed Constants #########
BRWV = 20000.0                      # Bioreactor working volume (L)
FGF2MM = 24000.0
FixManuCost_Factor = 0.15
BRUC = 50000.0                      # Bioreactor Unit Cost = $50,000 per reactor in m^3
Adj_BioR_valu = 1.29                # Adjusted Bioreactor value
BV = 20.0                           # Bioreactor volume (m^3)
BioRScF = 0.60                      # Bioreactor Scale Factor
AA2P_conc = 0.064                   # g/L
NaHCO3_conc = 0.543                 # g/L
NaSe_conc = 0.000014                # g/L
Insulin_conc = 0.0194               # g/L
AnnOpTime = 8760.0                  # Annual Operating Time
AveCellDensity = 1060.0             # Average Single Cell Density (kg/m^3)
AveCellVol = 0.000000000000005      # Average Single Cell volume (m^3 per cell)
DesiredMassMeat = 121000000.0       # Desired Mass of Meat Produced in kg
tot_fixed_eq_costs = Adj_BioR_valu * BRUC * (BV**BioRScF)
oxygen_comsump = 0.0000000000000180 # mol/(h*cell)
mm_O2 = 0.032                       # kg/mol
media_Density = 1.0                 # kg/L
perc_O2_initial_charge = 0.02       # %ww
cost_O2 = 40.0                      # USD/ton
natural_gas_cost = 4.17             # $ per 1000 ft^3
natural_gas = 1.42                  # cents per kWh
boiler_ener_eff = 0.85              # Percentage
desired_Temp = 37.0                 # Desired tempersture in C
starting_Water_temp = 20.0          # Starting water temp in C
water_spec_Heat = 0.0016            # Specific Heat of Water kWh/(kg*C)
heat_release_O2 = 0.13              # Heat released per O2 consumed kWh
heater_eff = 1.0
water_cooler_eff = 1.0
ACBM_cooler_eff = 1.0
ACBM_cool_temp = 4.0                # Temp of cooled ACBM meat
ACBM_spec_heat = 0.000622           # Specific heat of ACBM
prod_worker_wage = 13.68            # $ per hour
Labor_Cost_Corr_Fact = 1 * 1.2 * 0.8 * 1.5 * 1.4 * 1.25
Process_Water_Cost = 0.63           # $/m^3
Waste_Water_Cost = 0.51             # $/m^3
Oxidation_Water_Cost = 0.57         # $/m^3
