from acbm import constants as c

def update_labor_results(scen):

    ## Manpower Calculation
    scen['Manpower_Cost'] = scen['BioReact']

    ## Annual Labor Costs
    scen['Ann_Labor_Cost'] = scen['Manpower_Cost'] * c.Labor_Cost_Corr_Fact * c.prod_worker_wage * c.AnnOpTime

    return scen
