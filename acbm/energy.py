from acbm import constants as c

## Cost of electricity
public_elect_cost = float((0.09 * c.natural_gas_cost + 6.78) / 100)
self_gen_elect_cost = float((c.natural_gas / c.boiler_ener_eff) / 100)

cost_of_elect = (public_elect_cost * 0.50) + (self_gen_elect_cost * 0.50)

## Electricity Needed to Cool ACBM
Elect_Cool_ACBM = float((c.DesiredMassMeat * (c.desired_Temp - c.ACBM_cool_temp) * c.ACBM_spec_heat) / c.ACBM_cooler_eff)

def update_energy_results(scen):

    ## Electricity Needed to Cool Bioreactors
    scen['Elect_Cool_BioReact'] = float((scen['O2_consum_batch'] * scen['AnnBatches'] * c.heat_release_O2) / c.water_cooler_eff)

    ## Electricity Needed to Heat Media
    scen['Elect_Heat_Media'] = float(((scen['AnnVolMedia'] * c.media_Density) * (c.desired_Temp - c.starting_Water_temp) * c.water_spec_Heat) / c.heater_eff)

    ## Total Electricity Needed
    scen['total_Elect'] = scen['Elect_Heat_Media'] + scen['Elect_Cool_BioReact'] + Elect_Cool_ACBM

    ## Total Electricity Costs
    scen['Elect_Cost'] = scen['total_Elect'] * cost_of_elect

    return scen
