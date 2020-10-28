import os, sys, json

# acbm model functions
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
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
FGF2Con = [0.0001, 0.00005, 0.00005, 0.0]                   # FGF-2 conc. (g/L)
GConInBM = [0.0178, 0.0267, 0.0267, 0.0356]                 # Glucose concentration in basal media (mol/L)

BaseMedia_cost = [3.12, 3.12, 3.12, 0.24]                   # Basal Media Cost ($/L)
FGF2_cost = [2005000.0, 1002500.0, 0.0, 0.0]                # FGF-2 cost (USD/g)
TGFB = [80900000 * 0.000002, 80900000 * 0.000002, 80900000 * 0.000002, 0.0] # Scenario TGF-b Costs
Transferrin = [4.28, 4.28, 4.28, 0.0]                       # Cost of Transferrin
AA2p_cost = [7.84, 7.84, 7.84, 0.0]                         # $/g
NaHCO3_cost = [0.01, 0.01, 0.01, 0.0]                       # $/g
NaSe_cost = [0.1, 0.1, 0.1, 0.0]                            # $/g
Insulin_cost = [340, 340, 340, 0.0]                         # $/g

# scenarios --------------------------------------------------------------------

# featured
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
        'GConInBM': GConInBM[i],

        'BaseMediaCost': BaseMedia_cost[i],
        'FGF2_cost': FGF2_cost[i],
        'TGFBCost': TGFB[i],
        'TransferrinCost': Transferrin[i],
        'AA2pCost': AA2p_cost[i],
        'NaHCO3Cost': NaHCO3_cost[i],
        'NaSeCost': NaSe_cost[i],
        'InsulinCost': Insulin_cost[i]
    }
    scenarios.append(scen)

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
    'name': 'name',
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
