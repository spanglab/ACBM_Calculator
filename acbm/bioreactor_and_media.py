from acbm import constants as c
from math import ceil, log

###### Functions for Calculating other variables ########

def growth_time(doubling_time):
    growth = float((log(100) / log(2)) * doubling_time)
    return growth

def cell_mass_per_batch(Vol, CellCount):
    mass_per = float(Vol * c.AveCellDensity * c.AveCellVol * 1000 * CellCount)
    return mass_per

def total_glu_consume_growth(ACC, Ug, doubling):
    growth_time = float((log(100) / log(2)) * doubling)
    cell_pop = []
    rate = []
    glu_consumed = []
    end_time = doubling * int(growth_time // doubling)
    for i in range(1, int(ceil(growth_time / doubling) + 1 )):
        cell_count = (2**(i-1) * ACC * 200 * 1000)
        cell_pop.append(cell_count)
    for j in cell_pop:
        g_rate = j * Ug
        rate.append(g_rate)
    for k in rate[:-1]:
        g_con = k * doubling
        glu_consumed.append(g_con)
    g_con_last = rate[-1] * (growth_time - end_time)
    glu_consumed.append(g_con_last)
    return float(round(sum(glu_consumed),2))

def glucose_cons_in_mat(Vol, CellCount, ConsRate, MatureTime):
    consumed_in_mat = float(Vol * CellCount * 1000 * ConsRate * MatureTime)
    return consumed_in_mat

def update_bio_and_media_results(scen):
    
    # Total Glucose consumed in Maturation and Growth Phases
    scen['GluConInMatPhase'] = glucose_cons_in_mat(scen['BRWV'], scen['ACC'], scen['Ug'], scen['MatTime'])
    scen['GluConInGrowthPhase'] = total_glu_consume_growth(scen['ACC'], scen['Ug'], scen['d'])

    # Total Glucose in Charge (mol)
    scen['GluInCharge'] = scen['BRWV'] * scen['GConInBM']

    # Total Glucose Consumed per Batch (mol)
    scen['TotGluConBatch'] = scen['GluConInGrowthPhase'] + scen['GluConInMatPhase']

    # Media Charges per batch (mol/mol)
    scen['MediaChargeBatch'] = scen['TotGluConBatch'] / scen['GluInCharge']

    # Volume of Media per Batch (L)
    scen['Media_Vol'] = scen['BRWV'] * scen['MediaChargeBatch']

    # Batches per Year per BioReactor
    scen['BatchPerYear'] = ceil(c.AnnOpTime / (scen['MatTime'] + growth_time(scen['d'])))

    scen['CellMassBatch'] = cell_mass_per_batch(scen['BRWV'], scen['ACC'])
    scen['ACBM'] = scen['CellMassBatch'] * scen['BatchPerYear']

    # Calculated BioReactor numbers 
    scen['BioReact'] = int(ceil(c.DesiredMassMeat / scen['ACBM']))

    scen['AnnBatches'] = int(ceil(scen['BioReact'] * scen['BatchPerYear']))

    # Costs for BioReactors
    scen['BioEquip'] = scen['BioReact'] * c.tot_fixed_eq_costs

    # Total Bioequpiment costs
    scen['BioEquip_total'] = scen['BioEquip'] * 2

    # Fixed Manufacturing Costs = Minimal Capital Expenditures 
    scen['Fix_Manu_Cost'] = scen['BioEquip_total'] * c.FixManuCost_Factor

    # Cost of Media per L
    scen['Media_Cost'] = float(scen['BaseMediaCost'] + 
                               scen['TGFBCost'] + 
                               scen['TransferrinCost'] + 
                               (scen['InsulinCost'] * c.Insulin_conc) + 
                               (scen['NaSeCost'] * c.NaSe_conc) + 
                               (scen['NaHCO3Cost'] * c.NaHCO3_conc) + 
                               (scen['AA2pCost'] * c.AA2P_conc) + 
                               (scen['FGF2_cost'] * scen['FGF2Con']))
    
    # Annual Volume of Media
    scen['AnnVolMedia'] = scen['Media_Vol'] * scen['AnnBatches']

    # Total Annual Cost of Media
    scen['AnnMediaCost'] = scen['AnnVolMedia'] * scen['Media_Cost']

    return scen
