from constants import *
import numpy as np
import math

###### Functions for Calculating other variables ########

def growth_time(doubling_time):
    growth = float((np.log(100) / np.log(2)) * doubling_time)
    return growth

def cell_mass_per_batch(Vol,CellCount):
    mass_per = float(Vol * AveCellDensity * AveCellVol * 1000 * CellCount)
    return mass_per

def total_glu_consume_growth(ACC, Ug, doubling):
    growth_time = float((np.log(100) / np.log(2)) * doubling)
    cell_pop = []
    rate = []
    glu_consumed = []
    end_time = doubling * int(growth_time // doubling)
    for i in range(1, int(math.ceil(growth_time / doubling) + 1 )):
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

def glucose_cons_in_mat(Vol,CellCount,ConsRate,MatureTime):
    consumed_in_mat = float(Vol * CellCount * 1000 * ConsRate * MatureTime)
    return consumed_in_mat

# Total Glucose consumed in Maturation and Growth Phases
GluConInMatPhase1 = glucose_cons_in_mat(BRWV,ACC[0],Ug[0],MatTime[0])
GluConInMatPhase2 = glucose_cons_in_mat(BRWV,ACC[1],Ug[1],MatTime[1])
GluConInMatPhase3 = glucose_cons_in_mat(BRWV,ACC[2],Ug[2],MatTime[2])
GluConInMatPhase4 = glucose_cons_in_mat(BRWV,ACC[3],Ug[3],MatTime[3])
cust_GluCon_Mat = glucose_cons_in_mat(cust_BRWV,cust_ACC,float(cust_Ug),cust_MatTime)

GluConInGrowthPhase1 = total_glu_consume_growth(ACC[0],Ug[0],d[0])
GluConInGrowthPhase2 = total_glu_consume_growth(ACC[1],Ug[1],d[1])
GluConInGrowthPhase3 = total_glu_consume_growth(ACC[2],Ug[2],d[2])
GluConInGrowthPhase4 = total_glu_consume_growth(ACC[3],Ug[3],d[3])
cust_GluCon_Growth = total_glu_consume_growth(cust_ACC,cust_Ug,cust_hr_doub)
# Total Glucose in Charge (mol)
GluInCharge1 = BRWV * GConInBM[0]
GluInCharge2 = BRWV * GConInBM[1]
GluInCharge3 = BRWV * GConInBM[2]
GluInCharge4 = BRWV * GConInBM[3]
cust_GluInCharge = float(cust_BRWV * cust_GConInBM)
# Total Glucose Consumed per Batch (mol)
TotGluConBatch1 = GluConInGrowthPhase1 + GluConInMatPhase1
TotGluConBatch2 = GluConInGrowthPhase2 + GluConInMatPhase2
TotGluConBatch3 = GluConInGrowthPhase3 + GluConInMatPhase3
TotGluConBatch4 = GluConInGrowthPhase4 + GluConInMatPhase4
cust_TotCluConBatch = cust_GluCon_Growth + cust_GluCon_Mat
# Media Charges per batch (mol/mol)
MediaChargeBatch1 = TotGluConBatch1 / GluInCharge1
MediaChargeBatch2 = TotGluConBatch2 / GluInCharge2
MediaChargeBatch3 = TotGluConBatch3 / GluInCharge3
MediaChargeBatch4 = TotGluConBatch4 / GluInCharge4
cust_MediaChargeBatch = cust_TotCluConBatch / cust_GluInCharge
# Volume of Media per Batch (L)
Media_Vol1 = BRWV * MediaChargeBatch1
Media_Vol2 = BRWV * MediaChargeBatch2
Media_Vol3 = BRWV * MediaChargeBatch3
Media_Vol4 = BRWV * MediaChargeBatch4
cust_Media_Vol = cust_BRWV * cust_MediaChargeBatch
# Bacthes per Year per BioReactor
BatchPerYear1 = math.ceil(AnnOpTime / (MatTime[0] + growth_time(d[0])))
BatchPerYear2 = math.ceil(AnnOpTime / (MatTime[1] + growth_time(d[1])))
BatchPerYear3 = math.ceil(AnnOpTime / (MatTime[2] + growth_time(d[2])))
BatchPerYear4 = math.ceil(AnnOpTime / (MatTime[3] + growth_time(d[3])))
cust_BatchPerYear = math.ceil(AnnOpTime / (cust_MatTime + growth_time(cust_hr_doub)))

CellMassBatch1 = cell_mass_per_batch(BRWV,ACC[0])
CellMassBatch2 = cell_mass_per_batch(BRWV,ACC[1])
CellMassBatch3 = cell_mass_per_batch(BRWV,ACC[2])
CellMassBatch4 = cell_mass_per_batch(BRWV,ACC[3])
cust_CellMassBatch = cell_mass_per_batch(cust_BRWV,cust_ACC)

ACBM1 = CellMassBatch1 * BatchPerYear1
ACBM2 = CellMassBatch2 * BatchPerYear2
ACBM3 = CellMassBatch3 * BatchPerYear3
ACBM4 = CellMassBatch4 * BatchPerYear4
cust_ACBM = cust_CellMassBatch * cust_BatchPerYear
# Calculated BioReactor numbers 
BioReact1 = int(math.ceil(DesiredMassMeat / ACBM1))
BioReact2 = int(math.ceil(DesiredMassMeat / ACBM2))
BioReact3 = int(math.ceil(DesiredMassMeat / ACBM3))
BioReact4 = int(math.ceil(DesiredMassMeat / ACBM4))
cust_BioReact = int(math.ceil(DesiredMassMeat / cust_ACBM))

AnnBatches1 = int(math.ceil(BioReact1 * BatchPerYear1))
AnnBatches2 = int(math.ceil(BioReact2 * BatchPerYear2))
AnnBatches3 = int(math.ceil(BioReact3 * BatchPerYear3))
AnnBatches4 = int(math.ceil(BioReact4 * BatchPerYear4))
cust_AnnBatches = int(math.ceil(cust_BioReact * cust_BatchPerYear))

BIOREACTORS = [BioReact1, BioReact2, BioReact3, BioReact4] # Bioreactor numbers
# Costs for BioReactors
BioEquip1 = BIOREACTORS[0] * tot_fixed_eq_costs 
BioEquip2 = BIOREACTORS[1] * tot_fixed_eq_costs 
BioEquip3 = BIOREACTORS[2] * tot_fixed_eq_costs 
BioEquip4 = BIOREACTORS[3] * tot_fixed_eq_costs 
BioEquip_Cust = cust_BioReact * tot_fixed_eq_costs
# Total Bioequpiment costs
BioEquip1_total = BioEquip1 * 2
BioEquip2_total = BioEquip2 * 2 
BioEquip3_total = BioEquip3 * 2 
BioEquip4_total = BioEquip4 * 2 
BioEquip_Cust_total = BioEquip_Cust * 2
# Fixed Manufacturing Costs = Minimal Capital Expenditures 
Fix_Manu_Cost1 = BioEquip1_total * FixManuCost_Factor
Fix_Manu_Cost2 = BioEquip2_total * FixManuCost_Factor
Fix_Manu_Cost3 = BioEquip3_total * FixManuCost_Factor
Fix_Manu_Cost4 = BioEquip4_total * FixManuCost_Factor
Fix_Manu_Cust_Cost = BioEquip_Cust_total * FixManuCost_Factor
# Cost of Media per L
Media_Cost1 = float(BaseMedia_cost + 
                    TGFB[0] + 
                    Transferrin[0] + 
                    (Insulin_cost*Insulin_conc) + 
                    (NaSe_cost*NaSe_conc) + 
                    (NaHCO3_cost*NaHCO3_conc) + 
                    (AA2p_cost*AA2P_conc) + 
                    (FGF2Con[0]*FGF2Cost[0]))
Media_Cost2 = float(BaseMedia_cost + 
                    TGFB[1] + 
                    Transferrin[1] + 
                    (Insulin_cost*Insulin_conc) + 
                    (NaSe_cost*NaSe_conc) + 
                    (NaHCO3_cost*NaHCO3_conc) + 
                    (AA2p_cost*AA2P_conc) + 
                    (FGF2Con[1]*FGF2Cost[1]))
Media_Cost3 = float(BaseMedia_cost + 
                    TGFB[2] + 
                    Transferrin[2] + 
                    (Insulin_cost*Insulin_conc) + 
                    (NaSe_cost*NaSe_conc) + 
                    (NaHCO3_cost*NaHCO3_conc) + 
                    (AA2p_cost*AA2P_conc) + 
                    (FGF2Con[2]*FGF2Cost[2]))
Media_Cost4 = float(BaseMedia_cost + 
                    TGFB[3] + 
                    Transferrin[3] + 
                    (Insulin_cost*Insulin_conc) + 
                    (NaSe_cost*NaSe_conc) + 
                    (NaHCO3_cost*NaHCO3_conc) + 
                    (AA2p_cost*AA2P_conc) + 
                    (FGF2Con[3]*FGF2Cost[3]))
cust_Media_Cost = float(BaseMedia_cost + 
                        TGFB[0] + 
                        Transferrin[0] + 
                        (Insulin_cost*Insulin_conc) + 
                        (NaSe_cost*NaSe_conc) + 
                        (NaHCO3_cost*NaHCO3_conc) + 
                        (AA2p_cost*AA2P_conc) + 
                        (cust_FGF2Con*cust_FGF2Cost))
# Annual Volume of Media
AnnVolMedia1 = Media_Vol1 * AnnBatches1
AnnVolMedia2 = Media_Vol2 * AnnBatches2
AnnVolMedia3 = Media_Vol3 * AnnBatches3
AnnVolMedia4 = Media_Vol4 * AnnBatches4
cust_AnnVolMedia = cust_Media_Vol * cust_AnnBatches
# Total Annual Cost of Media
AnnMediaCost1 = AnnVolMedia1 * Media_Cost1
AnnMediaCost2 = AnnVolMedia2 * Media_Cost2
AnnMediaCost3 = AnnVolMedia3 * Media_Cost3
AnnMediaCost4 = AnnVolMedia4 * Media_Cost4
cust_AnnMediaCost = cust_AnnVolMedia * cust_Media_Cost