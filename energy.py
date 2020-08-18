import math
from constants import *
from bioreactor_and_media import *
from oxygen import *

public_elect_cost = float((0.09 * natural_gas_cost + 6.78) / 100)
self_gen_elect_cost = float((natural_gas / boiler_ener_eff) / 100)

cost_of_elect = (public_elect_cost * 0.50) + (self_gen_elect_cost * 0.50)

## Electricity Needed to Cool ACBM

Elect_Cool_ACBM = float((DesiredMassMeat * (desired_Temp - ACBM_cool_temp) * ACBM_spec_heat)/ACBM_cooler_eff)

## Electricity Needed to Cool Bioreactors

Elect_Cool_BioReact1 = float((O2_consum_batch1 * AnnBatches1 * heat_release_O2) / water_cooler_eff)
Elect_Cool_BioReact2 = float((O2_consum_batch2 * AnnBatches2 * heat_release_O2) / water_cooler_eff)
Elect_Cool_BioReact3 = float((O2_consum_batch3 * AnnBatches3 * heat_release_O2) / water_cooler_eff)
Elect_Cool_BioReact4 = float((O2_consum_batch4 * AnnBatches4 * heat_release_O2) / water_cooler_eff)
cust_Elect_Cool_BioReact = float((cust_O2_consum_batch * cust_AnnBatches * heat_release_O2) / water_cooler_eff)

## Electricity Needed to Heat Media

Elect_Heat_Media1 = float(((AnnVolMedia1 * media_Density)*(desired_Temp - starting_Water_temp) * water_spec_Heat) / heater_eff)
Elect_Heat_Media2 = float(((AnnVolMedia2 * media_Density)*(desired_Temp - starting_Water_temp) * water_spec_Heat) / heater_eff)
Elect_Heat_Media3 = float(((AnnVolMedia3 * media_Density)*(desired_Temp - starting_Water_temp) * water_spec_Heat) / heater_eff)
Elect_Heat_Media4 = float(((AnnVolMedia4 * media_Density)*(desired_Temp - starting_Water_temp) * water_spec_Heat) / heater_eff)
cust_Elect_Heat_Media = float(((cust_AnnVolMedia * media_Density)*(desired_Temp - starting_Water_temp) 
                               * water_spec_Heat) / heater_eff)

## Total Electricity Needed

total_Elect1 = Elect_Heat_Media1 + Elect_Cool_BioReact1 + Elect_Cool_ACBM
total_Elect2 = Elect_Heat_Media2 + Elect_Cool_BioReact2 + Elect_Cool_ACBM
total_Elect3 = Elect_Heat_Media3 + Elect_Cool_BioReact3 + Elect_Cool_ACBM
total_Elect4 = Elect_Heat_Media4 + Elect_Cool_BioReact4 + Elect_Cool_ACBM
cust_total_Elect = cust_Elect_Heat_Media + cust_Elect_Cool_BioReact + Elect_Cool_ACBM

## Total Electricity Costs

Elect_Cost1 = total_Elect1 * cost_of_elect
Elect_Cost2 = total_Elect2 * cost_of_elect
Elect_Cost3 = total_Elect3 * cost_of_elect
Elect_Cost4 = total_Elect4 * cost_of_elect
cust_Elect_Cost = cust_total_Elect * cost_of_elect
