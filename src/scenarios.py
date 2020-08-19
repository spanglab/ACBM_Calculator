import os, sys
from math import ceil

# acbm model functions
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import acbm.constants as c
import acbm.bioreactor_and_media as bm
import acbm.oxygen as o
import acbm.energy as e
import acbm.labor as l
import acbm.non_electric as ne
import acbm.financing as f

##### Media Related variables per scenario ########
ACC = [10000000.0, 95000000.0, 95000000.0, 200000000.0]     # Achievable cell concentration cells/mL
Ug = [0.000000000000413, 0.000000000000207, 0.000000000000207, 0.0000000000000413]  # Ug = Glu. cons. rate per cell (mol/ h cell)
MatTime = [240, 156, 156, 24]                               # Maturation Time (h)
d = [24.0, 16.0, 16.0, 8.0]                                 # Hours per doubling (h)
FGF2Con = [0.0001, 0.0005, 0.0005, 0.0]                     # FGF-2 conc. (g/L)
FGF2Cost = [2005000.0, 1002500.0, 0.0, 0.0]                 # FGF-2 cost (USD/g)
GConInBM = [0.0178, 0.0267, 0.0267, 0.0356]                 # Glucose concentration in basal media (mol/L)
TGFB = [80900000 * 0.000002, 80900000 * 0.000002, 80900000 * 0.000002, 0.0] # Scenario TGF-b Costs
Transferrin = [4.28, 4.28, 4.28, 0.0]                       # Cost of Transferrin

###### Custom Starting Variables  #########
cust_ACC = 10000000.0
cust_Ug = 0.000000000000413
cust_MatTime = 240.0
cust_hr_doub = 24.0
cust_FGF2Con = 0.0001
cust_FGF2Cost = 2005000.0
cust_GConInBM = 0.0178
cust_TGFB = 80900000 * 0.000002
cust_Transferrin = 4.28

cust_BRWV = c.BRWV

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
    'BRWV': cust_BRWV,
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

# fixed scenarios
for scen in scenarios:
    # bioreactor and media -----------------------------------------------------
    scen = bm.update_bio_and_media_results(scen)
    scen = o.update_oxygen_results(scen)
    scen = e.update_energy_results(scen)
    scen = l.update_labor_results(scen)
    scen = ne.update_non_electric_results(scen)
    scen = f.update_financing_results(scen)

# custom scenario
scenario_custom = bm.update_bio_and_media_results(scenario_custom)
scenario_custom = o.update_oxygen_results(scenario_custom)
scenario_custom = e.update_energy_results(scenario_custom)
scenario_custom = l.update_labor_results(scenario_custom)
scenario_custom = ne.update_non_electric_results(scenario_custom)

# #### Data Lists #####
# Costs_Bioequip = [bm.BioEquip1, bm.BioEquip2, bm.BioEquip3, bm.BioEquip4, bm.BioEquip_Cust]
# Min_Cap_Exp = [bm.BioEquip1_total, bm.BioEquip2_total, bm.BioEquip3_total, bm.BioEquip4_total, bm.BioEquip_Cust_total]
# Costs_Fixed_Manu = [bm.Fix_Manu_Cost1, bm.Fix_Manu_Cost2, bm.Fix_Manu_Cost3, bm.Fix_Manu_Cost4, bm.Fix_Manu_Cust_Cost]
# Media_Costs = [bm.AnnMediaCost1, bm.AnnMediaCost2, bm.AnnMediaCost3, bm.AnnMediaCost4, bm.cust_AnnMediaCost]
# O2_costs = [o.Ann_O2_Cost1, o.Ann_O2_Cost2, o.Ann_O2_Cost3, o.Ann_O2_Cost4, o.cust_Ann_O2_Cost]
# Elect_costs = [e.Elect_Cost1, e.Elect_Cost2, e.Elect_Cost3, e.Elect_Cost4, e.cust_Elect_Cost]
# Labor_costs = [l.Ann_Labor_Cost1, l.Ann_Labor_Cost2, l.Ann_Labor_Cost3, l.Ann_Labor_Cost4, l.cust_Ann_Labor_Cost]
# Non_Electric_costs =[ne.Ann_Water_Cost1, ne.Ann_Water_Cost2, ne.Ann_Water_Cost3, ne.Ann_Water_Cost4, ne.cust_Ann_Water_Cost]
# Min_Ann_Op_Cost = [f.Min_Ann_Op_Cost1, f.Min_Ann_Op_Cost2, f.Min_Ann_Op_Cost3, f.Min_Ann_Op_Cost4, f.cust_Min_Ann_Op_Cost]
# cap_expend_with_debt_equity = [f.cap_expend_with_debt_equity1, f.cap_expend_with_debt_equity2, f.cap_expend_with_debt_equity3, f.cap_expend_with_debt_equity4, f.cust_cap_expend_with_debt_equity]
# Min_ACBM_tomeet_Exp = [f.Min_ACBM_tomeet_Exp1, f.Min_ACBM_tomeet_Exp2, f.Min_ACBM_tomeet_Exp3, f.Min_ACBM_tomeet_Exp4, f.cust_Min_ACBM_tomeet_Exp]
# Min_Ann_Cap_Op_Expend = [f.Min_Ann_Cap_Op_Expend1, f.Min_Ann_Cap_Op_Expend2, f.Min_Ann_Cap_Op_Expend3, f.Min_Ann_Cap_Op_Expend4, f.cust_Min_Ann_Cap_Op_Expend]
# Min_ACBM_Price = [f.Min_ACBM_Price1, f.Min_ACBM_Price2, f.Min_ACBM_Price3, f.Min_ACBM_Price4, f.cust_Min_ACBM_Price]

# def update_figure(new_cust_BRWV, new_cust_FGF2Con, new_cust_FGF2Cost, new_cust_ACC,
#                   new_cust_MatTime, new_cust_hr_doub, new_cust_Ug, new_cust_GConInBM):
    
#     new_cust_Ug = new_cust_Ug / 10**16

#     # New Custom Media Cost Variables
#     new_cust_GluCon_Mat = bm.glucose_cons_in_mat(new_cust_BRWV, new_cust_ACC, new_cust_Ug, new_cust_MatTime)
#     new_cust_GluCon_Growth = bm.total_glu_consume_growth(new_cust_ACC, new_cust_Ug, new_cust_hr_doub)
#     new_cust_GluInCharge = float(new_cust_BRWV * new_cust_GConInBM)
#     new_cust_TotCluConBatch = new_cust_GluCon_Growth + new_cust_GluCon_Mat
#     new_cust_MediaChargeBatch = new_cust_TotCluConBatch / new_cust_GluInCharge
#     new_cust_Media_Vol = new_cust_BRWV * new_cust_MediaChargeBatch
#     new_cust_BatchPerYear = AnnOpTime / (new_cust_MatTime + bm.growth_time(new_cust_hr_doub))
#     new_cust_CellMassBatch = bm.cell_mass_per_batch(new_cust_BRWV, new_cust_ACC)
#     new_cust_ACBM = new_cust_CellMassBatch * new_cust_BatchPerYear
#     new_cust_BioReact = DesiredMassMeat / new_cust_ACBM
#     new_cust_AnnBatches = new_cust_BioReact * new_cust_BatchPerYear
#     new_BioEquip_Cust = new_cust_BioReact * tot_fixed_eq_costs
#     new_BioEquip_Cust_total = new_BioEquip_Cust * 2
#     new_Fix_Manu_Cust_Cost = new_BioEquip_Cust_total * FixManuCost_Factor
#     new_cust_Media_Cost = float(BaseMedia_cost + 
#                         TGFB[0] + 
#                         Transferrin[0] + 
#                         (Insulin_cost * Insulin_conc) + 
#                         (NaSe_cost * NaSe_conc) + 
#                         (NaHCO3_cost * NaHCO3_conc) + 
#                         (AA2p_cost * AA2P_conc) + 
#                         (new_cust_FGF2Con * new_cust_FGF2Cost))
#     new_cust_AnnVolMedia = new_cust_Media_Vol * new_cust_AnnBatches
#     new_cust_AnnMediaCost = new_cust_AnnVolMedia * new_cust_Media_Cost

#     # New O2 Custom Costs
#     new_cust_O2_cons_in_mat = float((new_cust_BRWV * new_cust_ACC * 1000) * new_cust_MatTime * oxygen_comsump)
#     new_cust_initial_O2_batch = float(((new_cust_MediaChargeBatch * new_cust_BRWV) 
#                                        * media_Density * perc_O2_initial_charge) / mm_O2)
#     new_cust_total_O2_cons_growth = o.total_O2_consume_growth(new_cust_ACC,new_cust_hr_doub)
#     new_cust_O2_consum_batch = new_cust_total_O2_cons_growth + new_cust_initial_O2_batch + new_cust_O2_cons_in_mat
#     new_cust_Ann_O2_Consum = (new_cust_O2_consum_batch * mm_O2 * new_cust_AnnBatches)/1000
#     new_cust_Ann_O2_Cost = new_cust_Ann_O2_Consum * cost_O2

#     # New Energy Costs
#     new_cust_Elect_Cool_BioReact = float((new_cust_O2_consum_batch * new_cust_AnnBatches * heat_release_O2) / water_cooler_eff)
#     new_cust_Elect_Heat_Media = float(((new_cust_AnnVolMedia * media_Density) * (desired_Temp - starting_Water_temp) 
#                                * water_spec_Heat) / heater_eff)
#     new_cust_total_Elect = new_cust_Elect_Heat_Media + new_cust_Elect_Cool_BioReact + e.Elect_Cool_ACBM
#     new_cust_Elect_Cost = new_cust_total_Elect * e.cost_of_elect

#     # New Labor Costs
#     new_cust_Manpower_Cost = (new_cust_BioReact)
#     new_cust_Ann_Labor_Cost = new_cust_Manpower_Cost * Labor_Cost_Corr_Fact * prod_worker_wage * AnnOpTime

#     # New Non-Electric Costs
#     new_cust_Process_Water = new_cust_AnnVolMedia / 1000
#     new_cust_Ann_Water_Cost = new_cust_Process_Water * (Process_Water_Cost + Waste_Water_Cost + Oxidation_Water_Cost)

#     # New Financing Values
#     new_cust_tot_equity_cost = f.Total_Equity_Cost(new_BioEquip_Cust_total)
#     new_cust_ann_equity_recov = f.Ann_Equity_Recov(new_cust_tot_equity_cost)
#     new_cust_tot_debt_cost = f.Total_Debt_Cost(new_BioEquip_Cust_total)
#     new_cust_ann_debt_payment = f.Ann_Debt_Payment(new_cust_tot_debt_cost)
#     new_cust_tot_ann_payment = new_cust_ann_debt_payment + new_cust_ann_equity_recov
#     new_cust_cap_expend_with_debt_equity = float(new_cust_tot_ann_payment * f.Economic_Life)
#     new_cust_Min_Ann_Op_Cost = float(new_Fix_Manu_Cust_Cost + 
#                                      new_cust_AnnMediaCost + 
#                                      new_cust_Ann_O2_Cost + 
#                                      new_cust_Elect_Cost + 
#                                      new_cust_Ann_Labor_Cost + 
#                                      new_cust_Ann_Water_Cost)
#     new_cust_Min_ACBM_tomeet_Exp = float(new_cust_Min_Ann_Op_Cost / DesiredMassMeat)
#     new_cust_Min_Ann_Cap_Op_Expend = (new_BioEquip_Cust_total / f.Economic_Life) + new_cust_Min_Ann_Op_Cost
#     new_cust_Min_ACBM_Price = float(new_cust_Min_Ann_Cap_Op_Expend / DesiredMassMeat)

#     # New Data lists 
#     new_Costs_Bioequip = [bm.BioEquip1, bm.BioEquip2, bm.BioEquip3, bm.BioEquip4, new_BioEquip_Cust]
#     new_Min_Cap_exp = [bm.BioEquip1_total, bm.BioEquip2_total, bm.BioEquip3_total, bm.BioEquip4_total, new_BioEquip_Cust_total]
#     new_Costs_Fixed_Manu = [bm.Fix_Manu_Cost1, bm.Fix_Manu_Cost2, bm.Fix_Manu_Cost3, bm.Fix_Manu_Cost4, new_Fix_Manu_Cust_Cost]
#     new_AnnMediaCosts = [bm.AnnMediaCost1, bm.AnnMediaCost2, bm.AnnMediaCost3, bm.AnnMediaCost4, new_cust_AnnMediaCost]
    
#     new_O2_costs = [o.Ann_O2_Cost1, o.Ann_O2_Cost2, o.Ann_O2_Cost3, o.Ann_O2_Cost4, new_cust_Ann_O2_Cost]

#     new_Elect_costs = [e.Elect_Cost1, e.Elect_Cost2, e.Elect_Cost3, e.Elect_Cost4, new_cust_Elect_Cost]

#     new_Labor_costs = [l.Ann_Labor_Cost1, l.Ann_Labor_Cost2, l.Ann_Labor_Cost3, l.Ann_Labor_Cost4, new_cust_Ann_Labor_Cost]
    
#     new_Non_Electric_costs =[ne.Ann_Water_Cost1, ne.Ann_Water_Cost2, ne.Ann_Water_Cost3, ne.Ann_Water_Cost4, new_cust_Ann_Water_Cost]
    
#     new_cap_expend_with_debt_equity = [f.cap_expend_with_debt_equity1, f.cap_expend_with_debt_equity2, f.cap_expend_with_debt_equity3, f.cap_expend_with_debt_equity4, new_cust_cap_expend_with_debt_equity]
#     new_Min_Ann_Op_Cost = [f.Min_Ann_Op_Cost1, f.Min_Ann_Op_Cost2, f.Min_Ann_Op_Cost3, f.Min_Ann_Op_Cost4, new_cust_Min_Ann_Op_Cost]
#     new_Min_ACBM_tomeet_Exp = [f.Min_ACBM_tomeet_Exp1, f.Min_ACBM_tomeet_Exp2, f.Min_ACBM_tomeet_Exp3, f.Min_ACBM_tomeet_Exp4, new_cust_Min_ACBM_tomeet_Exp]
#     new_Min_Ann_Cap_Op_Expend = [f.Min_Ann_Cap_Op_Expend1, f.Min_Ann_Cap_Op_Expend2, f.Min_Ann_Cap_Op_Expend3, f.Min_Ann_Cap_Op_Expend4, new_cust_Min_Ann_Cap_Op_Expend]
#     new_Min_ACBM_Price = [f.Min_ACBM_Price1, f.Min_ACBM_Price2, f.Min_ACBM_Price3, f.Min_ACBM_Price4, new_cust_Min_ACBM_Price]
 