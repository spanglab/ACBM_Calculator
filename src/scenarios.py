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

# rename and save subset to output values used by web app
return_key_map = {
    # plot values
    'BioEquip': 'Costs_Bioequip',
    'BioEquip_total': 'Min_Cap_Exp',
    'Fix_Manu_Cost': 'Costs_Fixed_Manu',
    'AnnMediaCost': 'Media_Costs',
    'Ann_O2_Cost': 'O2_costs',
    'Elect_Cost': 'Elect_costs',
    'Ann_Labor_Cost': 'Labor_costs',
    'Ann_Water_Cost': 'Non_Electric_costs',
    'Min_Ann_Op_Cost': 'Min_Ann_Op_Cost',
    'cap_expend_with_debt_equity': 'cap_expend_with_debt_equity',
    'Min_ACBM_tomeet_Exp': 'Min_ACBM_tomeet_Exp',
    'Min_Ann_Cap_Op_Expend': 'Min_Ann_Cap_Op_Expend',
    'Min_ACBM_Price': 'Min_ACBM_Price',
    # other values
    'BioReact': 'BioReact',
    'AnnBatches': 'AnnBatches',
    'Media_Vol': 'Media_Vol',
    'MediaChargeBatch': 'MediaChargeBatch',
    'TotGluConBatch': 'TotGluConBatch',
    'GluInCharge': 'GluInCharge',
    'GluConInMatPhase': 'GluConInMatPhase',
    'GluConInGrowthPhase': 'GluConInGrowthPhase',
    'AnnVolMedia': 'AnnVolMedia',
    'Media_Cost': 'Media_Cost',
    'Ann_O2_Consum': 'Ann_O2_Consum',
    'O2_consum_batch': 'O2_consum_batch',
    'total_O2_cons_growth': 'total_O2_cons_growth',
    'total_Elect': 'total_Elect',
    'Elect_Cool_BioReact': 'Elect_Cool_BioReact',
    'Elect_Heat_Media': 'Elect_Heat_Media',
    'tot_ann_payment': 'tot_ann_payment'
}
scenario_data = []
for scen in scenarios:
    scenario_data.append({ return_key_map[k]: scen[k] for k in return_key_map })

with open('scenario_data.json', 'w') as outfile:
    json.dump(scenario_data, outfile)
