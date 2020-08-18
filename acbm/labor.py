import math
from constants import *
from bioreactor_and_media import *

## Manpower Calculation

Manpower_Cost1 = (BioReact1)
Manpower_Cost2 = (BioReact2)
Manpower_Cost3 = (BioReact3)
Manpower_Cost4 = (BioReact4)
cust_Manpower_Cost = (cust_BioReact)

## Annual Labor Costs

Ann_Labor_Cost1 = Manpower_Cost1 * Labor_Cost_Corr_Fact * prod_worker_wage * AnnOpTime
Ann_Labor_Cost2 = Manpower_Cost2 * Labor_Cost_Corr_Fact * prod_worker_wage * AnnOpTime
Ann_Labor_Cost3 = Manpower_Cost3 * Labor_Cost_Corr_Fact * prod_worker_wage * AnnOpTime
Ann_Labor_Cost4 = Manpower_Cost4 * Labor_Cost_Corr_Fact * prod_worker_wage * AnnOpTime
cust_Ann_Labor_Cost = cust_Manpower_Cost * Labor_Cost_Corr_Fact * prod_worker_wage * AnnOpTime