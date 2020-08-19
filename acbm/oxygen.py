from math import ceil, log
from acbm import constants as c
#from bioreactor_and_media import *

def total_O2_consume_growth(ACC, doubling):
    growth_time = float((log(100) / log(2)) * doubling)
    cell_pop = []
    rate = []
    O2_consumed = []
    end_time = doubling * int(growth_time // doubling)
    for i in range(1, int(ceil(growth_time / doubling) + 1 )):
        cell_count = (2**(i-1) * ACC * 200 * 1000)
        cell_pop.append(cell_count)
    for j in cell_pop:
        O2_rate = j * c.oxygen_comsump
        rate.append(O2_rate)    
    for k in rate[:-1]:
        O2_con = k * doubling
        O2_consumed.append(O2_con)
    O2_con_last = rate[-1] * (growth_time - end_time)
    O2_consumed.append(O2_con_last)
    return float(sum(O2_consumed))

def update_oxygen_results(scen):
    ## O2 Consumed In Maturation
    scen['O2_cons_in_mat'] = float((scen['BRWV'] * scen['ACC'] * 1000) * scen['MatTime'] * c.oxygen_comsump)

    ## Initial O2 per batch
    scen['initial_O2_batch'] = float(((scen['MediaChargeBatch'] * scen['BRWV']) * c.media_Density * c.perc_O2_initial_charge) / c.mm_O2)

    ## Total O2 Consumed in Growth
    scen['total_O2_cons_growth'] = total_O2_consume_growth(scen['ACC'], scen['d'])

    ## O2 Consumed per batch
    scen['O2_consum_batch'] = float(scen['total_O2_cons_growth'] + scen['initial_O2_batch'] + scen['O2_cons_in_mat'])

    ## Annual O2 Consumption
    scen['Ann_O2_Consum'] = float((scen['O2_consum_batch'] * c.mm_O2 * scen['AnnBatches']) / 1000)

    ## Annual O2 Cost
    scen['Ann_O2_Cost'] = float(scen['Ann_O2_Consum'] * c.cost_O2)

    return scen