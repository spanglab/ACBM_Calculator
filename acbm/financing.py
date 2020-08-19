from acbm import constants as c

Economic_Life = 20 # Years
Cost_of_Equity = 0.15 # % per Y
Debt_Interest_Rate = 0.05 # % per Y
Debt_Ratio = 0.90
Equity_Ratio = 1.00 - 0.90

cap_rec_fac_num = (Cost_of_Equity * (1 + Cost_of_Equity)**Economic_Life)
cap_rec_fac_denom = ((1 + Cost_of_Equity)**Economic_Life - 1)
cap_rec_fac = cap_rec_fac_num / cap_rec_fac_denom

debt_rec_fac_num = (Debt_Interest_Rate * (1 + Debt_Interest_Rate)**Economic_Life)
debt_rec_fac_denom = ((1 + Debt_Interest_Rate)**Economic_Life - 1)
debt_rec_fac = debt_rec_fac_num / debt_rec_fac_denom

def Total_Equity_Cost(bioreactor_cost):
    return float(bioreactor_cost * Equity_Ratio)

def Ann_Equity_Recov(tot_equity): 
    Ann_Equity_Recov = float(tot_equity * cap_rec_fac)
    return Ann_Equity_Recov

def Total_Debt_Cost(bioreactor_cost):
    return float(bioreactor_cost * Debt_Ratio)
    
def Ann_Debt_Payment(tot_debt):
    Ann_Debt_Payment = float(tot_debt * debt_rec_fac)
    return float(Ann_Debt_Payment)

def update_financing_results(scen):

    scen['tot_equity_cost'] = Total_Equity_Cost(scen['BioEquip_total'])
    scen['ann_equity_recov'] = Ann_Equity_Recov(scen['tot_equity_cost'])
    scen['tot_debt_cost'] = Total_Debt_Cost(scen['BioEquip_total'])
    scen['ann_debt_payment'] = Ann_Debt_Payment(scen['tot_debt_cost'])
    scen['tot_ann_payment'] = scen['ann_debt_payment'] + scen['ann_equity_recov']
    scen['cap_expend_with_debt_equity'] = scen['tot_ann_payment'] + Economic_Life

    ## Final Finance Values
    scen['Min_Ann_Op_Cost'] = float(scen['Fix_Manu_Cost'] + scen['AnnMediaCost'] + scen['Ann_O2_Cost'] + scen['Elect_Cost'] + scen['Ann_Labor_Cost'] + scen['Ann_Water_Cost'])
    scen['Min_ACBM_tomeet_Exp'] = float(scen['Min_Ann_Op_Cost'] / c.DesiredMassMeat)
    scen['Min_Ann_Cap_Op_Expend'] = (scen['BioEquip_total'] / Economic_Life) + scen['Min_Ann_Op_Cost']
    scen['Min_ACBM_Price'] = float(scen['Min_Ann_Cap_Op_Expend'] / c.DesiredMassMeat)

    return scen
