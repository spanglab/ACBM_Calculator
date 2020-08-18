import math
from constants import *
from bioreactor_and_media import *

## Process Water Required

Process_Water1 = AnnVolMedia1 / 1000
Process_Water2 = AnnVolMedia2 / 1000
Process_Water3 = AnnVolMedia3 / 1000
Process_Water4 = AnnVolMedia4 / 1000
cust_Process_Water = cust_AnnVolMedia / 1000

## Annual Water Costs

Ann_Water_Cost1 = Process_Water1 * (Process_Water_Cost + Waste_Water_Cost + Oxidation_Water_Cost)
Ann_Water_Cost2 = Process_Water2 * (Process_Water_Cost + Waste_Water_Cost + Oxidation_Water_Cost)
Ann_Water_Cost3 = Process_Water3 * (Process_Water_Cost + Waste_Water_Cost + Oxidation_Water_Cost)
Ann_Water_Cost4 = Process_Water4 * (Process_Water_Cost + Waste_Water_Cost + Oxidation_Water_Cost)
cust_Ann_Water_Cost = cust_Process_Water * (Process_Water_Cost + Waste_Water_Cost + Oxidation_Water_Cost)