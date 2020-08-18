import math
from constants import *
from bioreactor_and_media import *
from oxygen import *
from energy import *
from labor import *
from non_electric import *

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

tot_equity_cost1 = Total_Equity_Cost(BioEquip1_total)
tot_equity_cost2 = Total_Equity_Cost(BioEquip2_total)
tot_equity_cost3 = Total_Equity_Cost(BioEquip3_total)
tot_equity_cost4 = Total_Equity_Cost(BioEquip4_total)
cust_tot_equity_cost = Total_Equity_Cost(BioEquip_Cust_total)

ann_equity_recov1 = Ann_Equity_Recov(tot_equity_cost1)
ann_equity_recov2 = Ann_Equity_Recov(tot_equity_cost2)
ann_equity_recov3 = Ann_Equity_Recov(tot_equity_cost3)
ann_equity_recov4 = Ann_Equity_Recov(tot_equity_cost4)
cust_ann_equity_recov = Ann_Equity_Recov(cust_tot_equity_cost)

tot_debt_cost1 = Total_Debt_Cost(BioEquip1_total)
tot_debt_cost2 = Total_Debt_Cost(BioEquip2_total)
tot_debt_cost3 = Total_Debt_Cost(BioEquip3_total)
tot_debt_cost4 = Total_Debt_Cost(BioEquip4_total)
cust_tot_debt_cost = Total_Debt_Cost(BioEquip_Cust_total)

ann_debt_payment1 = Ann_Debt_Payment(tot_debt_cost1)
ann_debt_payment2 = Ann_Debt_Payment(tot_debt_cost2)
ann_debt_payment3 = Ann_Debt_Payment(tot_debt_cost3)
ann_debt_payment4 = Ann_Debt_Payment(tot_debt_cost4)
cust_ann_debt_payment = Ann_Debt_Payment(cust_tot_debt_cost)

tot_ann_payment1 = ann_debt_payment1 + ann_equity_recov1
tot_ann_payment2 = ann_debt_payment2 + ann_equity_recov2
tot_ann_payment3 = ann_debt_payment3 + ann_equity_recov3
tot_ann_payment4 = ann_debt_payment4 + ann_equity_recov4
cust_tot_ann_payment = cust_ann_debt_payment + cust_ann_equity_recov

cap_expend_with_debt_equity1 = tot_ann_payment1 * Economic_Life
cap_expend_with_debt_equity2 = tot_ann_payment2 * Economic_Life
cap_expend_with_debt_equity3 = tot_ann_payment3 * Economic_Life
cap_expend_with_debt_equity4 = tot_ann_payment4 * Economic_Life
cust_cap_expend_with_debt_equity = cust_tot_ann_payment * Economic_Life

###### Final Finance Values

Min_Ann_Op_Cost1 = float(Fix_Manu_Cost1 + AnnMediaCost1 + Ann_O2_Cost1 + Elect_Cost1 + Ann_Labor_Cost1 + Ann_Water_Cost1)
Min_Ann_Op_Cost2 = float(Fix_Manu_Cost2 + AnnMediaCost2 + Ann_O2_Cost2 + Elect_Cost2 + Ann_Labor_Cost2 + Ann_Water_Cost2)
Min_Ann_Op_Cost3 = float(Fix_Manu_Cost3 + AnnMediaCost3 + Ann_O2_Cost3 + Elect_Cost3 + Ann_Labor_Cost3 + Ann_Water_Cost3)
Min_Ann_Op_Cost4 = float(Fix_Manu_Cost4 + AnnMediaCost4 + Ann_O2_Cost4 + Elect_Cost4 + Ann_Labor_Cost4 + Ann_Water_Cost4)
cust_Min_Ann_Op_Cost = float(Fix_Manu_Cust_Cost + cust_AnnMediaCost + cust_Ann_O2_Cost + cust_Elect_Cost + cust_Ann_Labor_Cost + cust_Ann_Water_Cost)

Min_ACBM_tomeet_Exp1 = float(Min_Ann_Op_Cost1 / DesiredMassMeat)
Min_ACBM_tomeet_Exp2 = float(Min_Ann_Op_Cost2 / DesiredMassMeat)
Min_ACBM_tomeet_Exp3 = float(Min_Ann_Op_Cost3 / DesiredMassMeat)
Min_ACBM_tomeet_Exp4 = float(Min_Ann_Op_Cost4 / DesiredMassMeat)
cust_Min_ACBM_tomeet_Exp = float(cust_Min_Ann_Op_Cost / DesiredMassMeat)

Min_Ann_Cap_Op_Expend1 = (BioEquip1_total / Economic_Life) + Min_Ann_Op_Cost1
Min_Ann_Cap_Op_Expend2 = (BioEquip2_total / Economic_Life) + Min_Ann_Op_Cost2
Min_Ann_Cap_Op_Expend3 = (BioEquip3_total / Economic_Life) + Min_Ann_Op_Cost3
Min_Ann_Cap_Op_Expend4 = (BioEquip4_total / Economic_Life) + Min_Ann_Op_Cost4
cust_Min_Ann_Cap_Op_Expend = (BioEquip_Cust_total / Economic_Life) + cust_Min_Ann_Op_Cost

Min_ACBM_Price1 = float(Min_Ann_Cap_Op_Expend1 / DesiredMassMeat)
Min_ACBM_Price2 = float(Min_Ann_Cap_Op_Expend2 / DesiredMassMeat)
Min_ACBM_Price3 = float(Min_Ann_Cap_Op_Expend3 / DesiredMassMeat)
Min_ACBM_Price4 = float(Min_Ann_Cap_Op_Expend4 / DesiredMassMeat)
cust_Min_ACBM_Price = float(cust_Min_Ann_Cap_Op_Expend / DesiredMassMeat)
