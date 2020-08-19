from acbm import constants as c

def update_non_electric_results(scen):

    ## Process Water Required
    scen['Process_Water'] = scen['AnnVolMedia'] / 1000

    ## Annual Water Costs
    scen['Ann_Water_Cost'] = scen['Process_Water'] * (c.Process_Water_Cost + c.Waste_Water_Cost + c.Oxidation_Water_Cost)

    return scen
