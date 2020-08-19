import os, sys, json

# acbm model functions
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import acbm.constants as c
import acbm.bioreactor_and_media as bm
import acbm.oxygen as o
import acbm.energy as e
import acbm.labor as l
import acbm.non_electric as ne
import acbm.financing as f

##### Media related variables per scenario ########
ACC = [10000000.0, 95000000.0, 95000000.0, 200000000.0]     # Achievable cell concentration cells/mL
Ug = [0.000000000000413, 0.000000000000207, 0.000000000000207, 0.0000000000000413]  # Ug = Glu. cons. rate per cell (mol/ h cell)
MatTime = [240, 156, 156, 24]                               # Maturation Time (h)
d = [24.0, 16.0, 16.0, 8.0]                                 # Hours per doubling (h)
FGF2Con = [0.0001, 0.0005, 0.0005, 0.0]                     # FGF-2 conc. (g/L)
FGF2Cost = [2005000.0, 1002500.0, 0.0, 0.0]                 # FGF-2 cost (USD/g)
GConInBM = [0.0178, 0.0267, 0.0267, 0.0356]                 # Glucose concentration in basal media (mol/L)
TGFB = [80900000 * 0.000002, 80900000 * 0.000002, 80900000 * 0.000002, 0.0] # Scenario TGF-b Costs
Transferrin = [4.28, 4.28, 4.28, 0.0]                       # Cost of Transferrin

###### Custom scenario starting values  #########
cust_ACC = 10000000.0
cust_Ug = 0.000000000000413
cust_MatTime = 240.0
cust_hr_doub = 24.0
cust_FGF2Con = 0.0001
cust_FGF2Cost = 2005000.0
cust_GConInBM = 0.0178
cust_TGFB = 80900000 * 0.000002
cust_Transferrin = 4.28

# scenarios --------------------------------------------------------------------

# base
scenarios = []
for i in range(4):
    scen = {
        'BRWV': c.BRWV,
        'name': f'scenario {i + 1}',
        'ACC': ACC[i],
        'Ug': Ug[i],
        'MatTime': MatTime[i],
        'd': d[i],
        'FGF2Con': FGF2Con[i],
        'FGF2Cost': FGF2Cost[i],
        'GConInBM': GConInBM[i],
        'TGFB': TGFB[i],
        'Transferrin': Transferrin[i]
    }
    scenarios.append(scen)

# custom
scenario_custom = {
    'BRWV': c.BRWV,
    'name': f'scenario custom',
    'ACC': cust_ACC,
    'Ug': cust_Ug,
    'MatTime': cust_MatTime,
    'd': cust_hr_doub,
    'FGF2Con': cust_FGF2Con,
    'FGF2Cost': cust_FGF2Cost,
    'GConInBM': cust_GConInBM,
    'TGFB': cust_TGFB,
    'Transferrin': cust_Transferrin
}

scenarios.append(scenario_custom)

def run_model(scen):
    '''Run each of the update functions for the provided scenario.'''
    scen = bm.update_bio_and_media_results(scen)
    scen = o.update_oxygen_results(scen)
    scen = e.update_energy_results(scen)
    scen = l.update_labor_results(scen)
    scen = ne.update_non_electric_results(scen)
    scen = f.update_financing_results(scen)

# run model for each scenario
for scen in scenarios:
    run_model(scen)
 
# save results to JSON file
with open('model_results.json', 'w') as outfile:
    json.dump(scenarios, outfile)
