import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objs as go
#import plotly.express as px
import os
import math
import base64
import webbrowser
from threading import Timer
from constants import *
from bioreactor_and_media import *
from financing import *
from oxygen import *
from energy import *
from labor import *
from non_electric import *

#### Data Lists #####

Scenarios = ["Scenario 1","Scenario 2","Scenario 3","Scenario 4","Custom Scenario"]
Costs_Bioequip = [BioEquip1,BioEquip2,BioEquip3,BioEquip4,BioEquip_Cust]
Min_Cap_Exp = [BioEquip1_total,BioEquip2_total,BioEquip3_total,BioEquip4_total,BioEquip_Cust_total]
Costs_Fixed_Manu = [Fix_Manu_Cost1,Fix_Manu_Cost2,Fix_Manu_Cost3,Fix_Manu_Cost4,Fix_Manu_Cust_Cost]
Media_Costs = [AnnMediaCost1,AnnMediaCost2,AnnMediaCost3,AnnMediaCost4,cust_AnnMediaCost]
O2_costs = [Ann_O2_Cost1,Ann_O2_Cost2,Ann_O2_Cost3,Ann_O2_Cost4,cust_Ann_O2_Cost]
Elect_costs = [Elect_Cost1,Elect_Cost2,Elect_Cost3,Elect_Cost4,cust_Elect_Cost]
Labor_costs = [Ann_Labor_Cost1,Ann_Labor_Cost2,Ann_Labor_Cost3,Ann_Labor_Cost4,cust_Ann_Labor_Cost]
Non_Electric_costs =[Ann_Water_Cost1,Ann_Water_Cost2,Ann_Water_Cost3,Ann_Water_Cost4,cust_Ann_Water_Cost]
Min_Ann_Op_Cost = [Min_Ann_Op_Cost1,Min_Ann_Op_Cost2,Min_Ann_Op_Cost3,Min_Ann_Op_Cost4,cust_Min_Ann_Op_Cost]
cap_expend_with_debt_equity = [cap_expend_with_debt_equity1,
                                       cap_expend_with_debt_equity2,
                                       cap_expend_with_debt_equity3,
                                       cap_expend_with_debt_equity4,
                                       cust_cap_expend_with_debt_equity]
Min_ACBM_tomeet_Exp = [Min_ACBM_tomeet_Exp1,
                       Min_ACBM_tomeet_Exp2,
                       Min_ACBM_tomeet_Exp3,
                       Min_ACBM_tomeet_Exp4,
                       cust_Min_ACBM_tomeet_Exp]
Min_Ann_Cap_Op_Expend = [Min_Ann_Cap_Op_Expend1,
                         Min_Ann_Cap_Op_Expend2,
                         Min_Ann_Cap_Op_Expend3,
                         Min_Ann_Cap_Op_Expend4,
                         cust_Min_Ann_Cap_Op_Expend]
Min_ACBM_Price = [Min_ACBM_Price1,Min_ACBM_Price2,Min_ACBM_Price3,Min_ACBM_Price4,cust_Min_ACBM_Price]

#### Figure 1: Scenario Cost Traces #######

fig1 = go.Figure()

fig1.add_trace(go.Bar(
    x=Scenarios,
    y=Costs_Bioequip,
    name='Bioreactor Costs',
    marker_color='indianred',
    offsetgroup=0,
    hovertemplate='Scenario: %{x}<br>Bioreactor Cost: %{y}<extra></extra>'
))

fig1.add_trace(go.Bar(
    x=Scenarios,
    y=Costs_Fixed_Manu,
    name='Fixed Manufacturing Cost',
    marker_color='firebrick',
    offsetgroup=1,
    hovertemplate='Scenario: %{x}<br>Fixed Manufacturing Cost: %{y}<extra></extra>'
))

fig1.add_trace(go.Bar(
    x=Scenarios,
    y=Media_Costs,
    name='Annual Media Cost',
    marker_color='teal',
    offsetgroup=2,
    hovertemplate='Scenario: %{x}<br>Annual Media Cost: %{y}<extra></extra>'
))

fig1.add_trace(go.Bar(
    x=Scenarios,
    y=O2_costs,
    name='Annual O2 Cost',
    marker_color='grey',
    offsetgroup=3,
    hovertemplate='Scenario: %{x}<br>Annual O2 Cost: %{y}<extra></extra>'
))

fig1.add_trace(go.Bar(
    x=Scenarios,
    y=Elect_costs,
    name='Annual Energy Costs',
    marker_color='#ff0586',
    offsetgroup=4,
    hovertemplate='Scenario: %{x}<br>Annual Energy Cost: %{y}<extra></extra>'
))

fig1.add_trace(go.Bar(
    x=Scenarios,
    y=Labor_costs,
    name='Annual Labor Costs',
    marker_color='#75264f',
    offsetgroup=5,
    hovertemplate='Scenario: %{x}<br>Annual Labor Cost: %{y}<extra></extra>'
))

fig1.add_trace(go.Bar(
    x=Scenarios,
    y=Non_Electric_costs,
    name='Annual Non-Electric Utility Costs',
    marker_color='#6a2675',
    offsetgroup=6,
    hovertemplate='Scenario: %{x}<br>Annual Non-Electric Utility Cost: %{y}<extra></extra>'
))

fig1.update_layout(xaxis_tickangle=45, yaxis_type="log", yaxis_title="US Dollars ($)")

#### Figure 2: Scenario Total/Operating Cost Traces #######

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=Scenarios,
    y=Min_Cap_Exp,
    name='Min. Capital Expeditures',
    marker_color='#FFA505',
    offsetgroup=0,
    hovertemplate='Scenario: %{x}<br>Minimal Capital Expediture: %{y}<extra></extra>'
))

fig2.add_trace(go.Bar(
    x=Scenarios,
    y=cap_expend_with_debt_equity,
    name='Capital Expenditures (with debt & equity)',
    marker_color='#ff0586',
    offsetgroup=1,
    hovertemplate='Scenario: %{x}<br>Capital Expeditures: %{y}<extra></extra>'
))

fig2.add_trace(go.Bar(
    x=Scenarios,
    y=Min_Ann_Op_Cost,
    name='Min. Ann. Op. Costs',
    marker_color='#6a2675',
    offsetgroup=2,
    hovertemplate='Scenario: %{x}<br>Minimum Annual Operating Cost: %{y}<extra></extra>'
))

fig2.add_trace(go.Bar(
    x=Scenarios,
    y=Min_ACBM_tomeet_Exp,
    name='Min. price of ACBM for Ann. Op. Ex.',
    marker_color='firebrick',
    offsetgroup=3,
    hovertemplate='Scenario: %{x}<br>Minimum Price of ACBM To Meet Annual Operating Expenses: %{y}<extra></extra>'
))

fig2.add_trace(go.Bar(
    x=Scenarios,
    y=Min_Ann_Cap_Op_Expend,
    name='Min. Ann. Capital & Op. Expend.',
    marker_color='#ff4500',
    offsetgroup=4,
    hovertemplate='Scenario: %{x}<br>Minimum Annual Capital & Operating Expenditures: %{y}<extra></extra>'
))

fig2.add_trace(go.Bar(
    x=Scenarios,
    y=Min_ACBM_Price,
    name='Min. price of ACBM for Ann. Capital & Op. Exp.',
    marker_color='#C7509F',
    offsetgroup=5,
    hovertemplate='Scenario: %{x}<br>Minimum price of ACBM to meet Annual Capital and Operating Expenses: %{y}<extra></extra>'
))

fig2.update_layout(xaxis_tickangle=45, yaxis_type="log", yaxis_title="US Dollars ($)")

#### Dash Things

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

image_filename = 'The_University_of_California_Davis.svg.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

header = html.Div([html.H3('The Animal Cell Based Meat Cost Calculator.')], style={'textAlign': 'center'})

body = html.Div([     
    html.Div([ # Block 1: Logo, Graph, and Custom Variables with Outputs
        html.Div([ # Left side: Logo
            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'height':'25%', 'width':'25%'}),
            html.Div(children='This Cell-Based-Meat calculator app was written by Dr. Jason S. Fell.'),
            html.Div(children='This calculator is based upon the [PAPER CITATION].'),
            html.Div(children='The code will be released when the manuscript is published.'),
            html.Div(children='Please send email to jsfell@ucdavis.edu if you would like to review the code.'),
            html.Div([
                dcc.Graph( # Output of Custom Annual Scenario Values
                    id='graph1',
                    figure=fig1,
                    #style={'padding':10}
                    ),
                html.Div(children='The desired mass of meat being produced is 121,000,000 kg.'),
                html.Div(id="cust_bioreactors",
                    children=u'The custom number of bioreactors is {:20}.'.format(int(cust_BioReact))),
                html.Div(id="cust_ann_batch_output",
                    children=u'The custom number of annual batches is {:20}.'.format(int(cust_AnnBatches))),
                html.Div(id="cust_bioreact_cost_output",
                    children=u'The custom bioreactor cost is ${:20,.2f}.'.format(BioEquip_Cust)),
                html.Div(id="cust_fix_manu_cost_output",
                    children=u'The custom fixed manufacturing cost is ${:20,.2f}.'.format(Fix_Manu_Cust_Cost)),
                html.Div(id='cust_vol_media_batch_output', 
                         children=u'The custom volume of media per batch is {:20,.2f} L'.format(cust_Media_Vol)),
                html.Div(id='cust_mediachargebatch_output', 
                         children=u'The custom media charge per batch is {:20,.2f}.'.format(cust_MediaChargeBatch)),
                html.Div(id='cust_TotCluConBatch_output',
                        children=u'The custom total glucose consumed per batch is {:20,.2f}.'.format(cust_TotCluConBatch)),
                html.Div(id='cust_GluInCharge_output',
                        children=u'The custom glucose per charge is {:20,.2f}.'.format(cust_GluInCharge)),
                html.Div(id='cust_GluCon_Mat_output',
                        children=u'The custom glucose consumed during maturation is {:20,.2f}.'.format(cust_GluCon_Mat)),
                html.Div(id='cust_GluCon_Growth_output',
                        children=u'The custom glucose consumed during growth is {:20,.2f}.'.format(cust_GluCon_Growth)),
                html.Div(id="cust_vol_media_output",
                    children=u'The custom annual volume of media is {:20,.2f} liter.'.format(cust_AnnVolMedia)),
                html.Div(id="cust_media_cost_output",
                    children=u'The custom cost of media is ${:20,.2f} per liter.'.format(cust_Media_Cost)),
                html.Div(id="annmediacost_output",
                    children=u'The custom annual cost of media is ${:20,.2f}.'.format(cust_AnnMediaCost)),
                html.Div(id="annO2cons_output",
                    children=u'The custom annual consumption of O2 is {:20,.2f}.'.format(cust_Ann_O2_Consum)),
                html.Div(id="cust_O2_consum_batch_output",
                    children=u'The custom consumption of O2 per batch is {:20,.2f}.'.format(cust_O2_consum_batch)),
                html.Div(id="ann_o2_cost_output",
                    children=u'The custom annual cost of O2 is ${:20,.2f}.'.format(cust_Ann_O2_Cost)),
                html.Div(id="cust_total_O2_cons_growth_output",
                    children=u'The custom O2 consumed in growth phase is {:20,.2f}.'.format(cust_total_O2_cons_growth)),
                html.Div(id="ann_energy_cost_output",
                    children=u'The custom annual energy cost is ${:20,.2f}.'.format(cust_Elect_Cost)),
                html.Div(id="cust_total_Elect_output",
                    children=u'The custom total energy requirement is {:20,.2f} kWh.'.format(cust_total_Elect)),
                html.Div(id='cust_Elect_Cool_BioReact_output',
                         children=u'The custom energy requirement to cool bioreactors is {:20,.2f} kWh.'.format(cust_Elect_Cool_BioReact)),
                html.Div(id='cust_Elect_Heat_Media_output',
                         children=u'The custom energy requirement to heat bioreactors is {:20,.2f} kWh.'.format(cust_Elect_Heat_Media)),
                html.Div(id="ann_labor_cost_output",
                    children=u'The custom annual labor cost is ${:20,.2f}.'.format(cust_Ann_Labor_Cost)),
                html.Div(id="ann_nonE_cost_output",
                    children=u'The custom annual non-electric utility cost is ${:20,.2f}.'.format(cust_Ann_Water_Cost)),
                html.Div(id='cust_tot_ann_payment_output',
                         children=u'The custom total annual payment with captial expenditures is ${:20,.2f}.'.format(cust_tot_ann_payment)),
                dcc.Graph( # Output of Custom Operating Scenario Costs
                    id='graph2',
                    figure=fig2,
                    style={'padding':10}
                    ),
                html.Div(id="cust_min_cap_exp",
                    children=u'The custom minimum capital expenditures is ${:20,.2f}.'.format(BioEquip_Cust_total)),
                html.Div(id="cust_cap_exp_with_DandE_output",
                    children=u'The custom capital expenditures, with debt and equity recovery, is ${:20,.2f}.'.format(cap_expend_with_debt_equity[4])),
                html.Div(id="cust_MinAnnOpCost_output",
                    children=u'The custom minimum annual operating costs are ${:20,.2f}.'.format(cust_Min_Ann_Op_Cost)),
                html.Div(id="cust_MinACBMPrice_AnOp_output",
                    children=u'The custom minimum price of ACBM to meet annual operating expenses are ${:20,.2f} per kg.'.format(cust_Min_ACBM_tomeet_Exp)),
                html.Div(id="cust_MinAnnCapOpExp_output",
                    children=u'The custom minimum annual capital and operating expenses are ${:20,.2f}.'.format(cust_Min_Ann_Cap_Op_Expend)),
                html.Div(id="cust_MinACBM_output",
                    children=u'The custom minimum price of ACBM to meet annual capital and operating expenses are ${:20,.2f} per kg.'.format(cust_Min_ACBM_Price))
            ])], 
            className="six columns",style={'marginBottom': 20}),
    html.Div([ # Block 2: Custom Cost Variable Scales
        html.Div([
             html.H5('Custom Cost Scales',
                 style={'textAlign': 'center'}),
            # First Scale: Achievable Cell Concentration (ACC; cell/mL)
            html.Div([
                html.I("Adjust the achievable cell concentration (cells/mL).")],
                style={'marginBottom': 10,'marginTop': 20}),
            html.Div([
                dcc.Slider(
                    id = 'acc_slider',
                    min = float(min(ACC) / 2),
                    max = 2*max(ACC),
                    value = cust_ACC#,
                    #step=1
                )],
                style={'marginBottom': 20,'marginTop': 20}),
            html.Div([
                html.Div(id="acc_output",
                        children=u'The custom achievable cell concentration is set to {:.2e} cells/mL.'.format(cust_FGF2Cost)
                        )],
                style={'marginBottom': 10,'marginTop': 10}),
            # Second Scale: Custom Bioreactor Working Volume
            html.Div([
                html.I("Adjust the working volume of the bioreactors.")],
                style={'marginBottom': 10,'marginTop': 20}),
            html.Div([
                dcc.Slider(
                    id = 'bioreactslider',
                    min = (0.25 * BRWV),
                    max = (1000000),
                    value = cust_BRWV,
                    step=1000.0,
                    marks={25000: "25,000 L"}
                )],
                style={'marginBottom': 20,'marginTop': 20}),
            html.Div([
                html.Div(id="bioreactor_output",
                        children=u'The custom working volume of the bioreactors is set to {} L.'.format(cust_BRWV)
                        )],
                style={'marginBottom': 10,'marginTop': 10}),
            # Slider 3: Custom FGF2 Concentration (g/L) 
            html.Div([
                html.I("Adjust the g/L needed of FGF-2.")],
                style={'marginBottom': 10,'marginTop': 20}),
            html.Div([
                dcc.Slider(
                    id = 'fgf2_gL_slider',
                    min = 0,
                    max = 2*max(FGF2Con),
                    value = cust_FGF2Con,
                    step=0.00001
                )],
                style={'marginBottom': 20,'marginTop': 20}),
            html.Div([
                html.Div(id="cust_FGF2Con_output",
                        children=u'The concentration of FGF-2 is set to {:.2e} g/L.'.format(cust_FGF2Con)
                        )],
                style={'marginBottom': 10,'marginTop': 10}),
            # Slider 4: Custom FGF-2 Cost $/g
            html.Div([
                html.I("Adjust the $ per g of FGF-2.")],
                style={'marginBottom': 10,'marginTop': 20}),
            html.Div([
                dcc.Slider(
                    id = 'fgf2_costg_slider',
                    min = 0,
                    max = 2*max(FGF2Cost),
                    value = cust_FGF2Cost,
                    step=1
                )],
                style={'marginBottom': 20,'marginTop': 20}),
            html.Div([
                html.Div(id="cust_FGF2Cost_output",
                        children=u'The custom cost of FGF-2 is set to $ {:.2e} per gram.'.format(cust_FGF2Cost)
                        )],
                style={'marginBottom': 10,'marginTop': 10}),
            # Slider 5: Custom Glucose concentration in basal media (mol/L)
            html.Div([
                html.I("Adjust the custom Glucose concentration in basal media (mol/L).")],
                style={'marginBottom': 10,'marginTop': 20}),
            html.Div([
                dcc.Slider(
                    id = 'GConInBM_slider',
                    min = float(0.0089),
                    max = float(0.0712),
                    value = cust_GConInBM,
                    step=0.0001
                )],
                style={'marginBottom': 20,'marginTop': 20}),
            html.Div([
                html.Div(id="GConInBM_output",
                        children=u'The custom Glucose concentration in basal media is set to {:.2e} mol/L.'.format(cust_GConInBM)
                        )],
                style={'marginBottom': 10,'marginTop': 10}),
            # Slider 6: Custom Glucose consumption rate per cell [Ug; (mol/(hr*cell))]
            html.Div([
                html.I("Adjust the custom Glucose consumption rate per cell (mol/(h*cell)).")],
                style={'marginBottom': 10,'marginTop': 20}),
            html.Div([
                dcc.Slider(
                    id = 'ug_slider',
                    min = 100,
                    max = 10000,
                    value = cust_Ug * 10**16,
                    step=1
                )],
                style={'marginBottom': 20,'marginTop': 20}),
            html.Div([
                html.Div(id="ug_output",
                        children=u'The custom Glucose consumption rate per cell is set to {:.2e} mol/(h*cell).'.format(cust_Ug)
                        )],
                style={'marginBottom': 10,'marginTop': 10}),
            # Slider 7: Custom Hours per doubling (hours, h)
            html.Div([
                html.I("Adjust the custom hours per doubling of cells (h).")],
                style={'marginBottom': 10,'marginTop': 20}),
            html.Div([
                dcc.Slider(
                    id = 'hr_doub_slider',
                    min = float(0.5 * min(d)),
                    max = float(2 * max(d)),
                    value = cust_hr_doub#,
                    #step=1
                )],
                style={'marginBottom': 20,'marginTop': 20}),
            html.Div([
                html.Div(id="hr_doub_output",
                        children=u'The custom hours per doubling of cells is set to {} hours.'.format(cust_hr_doub)
                        )],
                style={'marginBottom': 10,'marginTop': 10}),
            # Slide 8: Custom Maturation Time (h; hours)
            html.Div([
                html.I("Adjust the cell maturation time (h).")],
                style={'marginBottom': 10,'marginTop': 20}),
            html.Div([
                dcc.Slider(
                    id = 'mat_time_slider',
                    min = float(0),
                    max = 2*max(MatTime),
                    value = cust_MatTime,
                    step=1
                )],
                style={'marginBottom': 20,'marginTop': 20}),
            html.Div([
                html.Div(id="mat_time_output",
                        children=u'The cell maturation time is set to {} hours.'.format(cust_MatTime)
                        )],
                style={'marginBottom': 10,'marginTop': 10}),
            # Scenario Variables List
            html.Div([
                html.Div([
                    html.Div([html.H6(children='Scenario 1 Values'),
                              html.Div(children=u'Achievable Cell Conc. = {:.2e} cells/mL'.format(ACC[0])),
                              html.Div(children=u'Bioreactor Working Volume = 20.0 m\u00b3'),
                              html.Div(children=u'FGF-2 Conc. = {:.2e} g/L'.format(FGF2Con[0])),
                              html.Div(children=u'FGF-2 Cost = {:.2e} $/g'.format(FGF2Cost[0])),
                              html.Div(children=u'Glucose Conc. in basal media = {:.2e} mol/L'.format(GConInBM[0])),
                              html.Div(children=u'Glucose Cons. Rate per Cell = {:.2e} mol/(h*cell)'.format(Ug[0])),
                              html.Div(children=u'Hours per Doubling = {} h'.format(d[0])),
                              html.Div(children=u'Maturation Time = {} h'.format(MatTime[0]))
                             ],className="six columns"),
                    html.Div([html.H6(children='Scenario 2 Values'),
                              html.Div(children=u'Achievable Cell Conc. = {:.2e} cells/mL'.format(ACC[1])),
                              html.Div(children=u'Bioreactor Working Volume = 20.0 m\u00b3'),
                              html.Div(children=u'FGF-2 Conc. = {:.2e} g/L'.format(FGF2Con[1])),
                              html.Div(children=u'FGF-2 Cost = {:.2e} $/g'.format(FGF2Cost[1])),
                              html.Div(children=u'Glucose Conc. in basal media = {:.2e} mol/L'.format(GConInBM[1])),
                              html.Div(children=u'Glucose Cons. Rate per Cell = {:.2e} mol/(h*cell)'.format(Ug[1])),
                              html.Div(children=u'Hours per Doubling = {} h'.format(d[1])),
                              html.Div(children=u'Maturation Time = {} h'.format(MatTime[1]))
                             ],className="six columns"),
                ],className="six columns"),
                html.Div([
                    html.Div([html.H6(children='Scenario 3 Values'),
                              html.Div(children=u'Achievable Cell Conc. = {:.2e} cells/mL'.format(ACC[2])),
                              html.Div(children=u'Bioreactor Working Volume = 20.0 m\u00b3'),
                              html.Div(children=u'FGF-2 Conc. = {:.2e} g/L'.format(FGF2Con[2])),
                              html.Div(children=u'FGF-2 Cost = {:.2e} $/g'.format(FGF2Cost[2])),
                              html.Div(children=u'Glucose Conc. in basal media = {:.2e} mol/L'.format(GConInBM[2])),
                              html.Div(children=u'Glucose Cons. Rate per Cell = {:.2e} mol/(h*cell)'.format(Ug[2])),
                              html.Div(children=u'Hours per Doubling = {} h'.format(d[2])),
                              html.Div(children=u'Maturation Time = {} h'.format(MatTime[2]))
                             ],className="six columns"),
                    html.Div([html.H6(children='Scenario 4 Values'),
                              html.Div(children=u'Achievable Cell Conc. = {:.2e} cells/mL'.format(ACC[3])),
                              html.Div(children=u'Bioreactor Working Volume = 20.0 m\u00b3'),
                              html.Div(children=u'FGF-2 Conc. = {:.2e} g/L'.format(FGF2Con[3])),
                              html.Div(children=u'FGF-2 Cost = {:.2e} $/g'.format(FGF2Cost[3])),
                              html.Div(children=u'Glucose Conc. in basal media = {:.2e} mol/L'.format(GConInBM[3])),
                              html.Div(children=u'Glucose Cons. Rate per Cell = {:.2e} mol/(h*cell)'.format(Ug[3])),
                              html.Div(children=u'Hours per Doubling = {} h'.format(d[3])),
                              html.Div(children=u'Maturation Time = {} h'.format(MatTime[3]))
                             ],className="six columns")
                ],className="six columns")
            ], className="row")
        ], className="six columns")
        ])
     ], className="row"),
],style={'textAlign': 'center'})

app.layout = html.Div([
        #nav,
        header,
        body#,
        #output
    ])

######## Begining of Callbacks #########

@app.callback(
    [Output('graph1', 'figure'),
     Output('cust_bioreactors', 'children'),
     Output('cust_bioreact_cost_output', 'children'),
     Output('cust_min_cap_exp', 'children'),
     Output('cust_fix_manu_cost_output', 'children'),
     Output('cust_media_cost_output', 'children'),
     Output("annmediacost_output",'children'),
     Output("ann_o2_cost_output",'children'),
     Output('ann_energy_cost_output','children'),
     Output('ann_labor_cost_output','children'),
     Output('ann_nonE_cost_output','children'),
     Output('graph2','figure'),
     Output("cust_ann_batch_output",'children'),
     Output('cust_vol_media_output','children'),
     Output("cust_cap_exp_with_DandE_output",'children'),
     Output('cust_MinAnnOpCost_output','children'),
     Output('cust_MinACBMPrice_AnOp_output','children'),
     Output('cust_MinAnnCapOpExp_output','children'),
     Output('cust_MinACBM_output','children'),
     Output('cust_vol_media_batch_output','children'),
     Output('cust_mediachargebatch_output','children'),
     Output('cust_TotCluConBatch_output','children'),
     Output('cust_GluInCharge_output','children'),
     Output('cust_GluCon_Mat_output','children'),
     Output('cust_GluCon_Growth_output','children'),
     Output('annO2cons_output','children'),
     Output('cust_O2_consum_batch_output','children'),
     Output('cust_total_O2_cons_growth_output','children'),
     Output('cust_total_Elect_output','children'),
     Output('cust_Elect_Cool_BioReact_output','children'),
     Output('cust_Elect_Heat_Media_output','children'),
     Output('cust_tot_ann_payment_output','children')
    ],
    [Input('bioreactslider','value'),
     Input('fgf2_gL_slider','value'),
     Input('fgf2_costg_slider','value'),
     Input('acc_slider','value'),
     Input('mat_time_slider','value'),
     Input('hr_doub_slider','value'),
     Input('ug_slider','value'),
     Input('GConInBM_slider','value')
    ])

def update_figure(slider1,slider2,slider3,slider4,slider5,slider6,slider7,slider8):
    '''Function to update custom cost from 
    slider1 input. '''    
    # New Custom Variables from sliders
    new_cust_BRWV = slider1
    new_cust_FGF2Con = slider2
    new_cust_FGF2Cost = slider3
    new_cust_ACC = slider4
    new_cust_MatTime = slider5
    new_cust_hr_doub = slider6
    new_cust_Ug = slider7 / 10**16
    new_cust_GConInBM = slider8    
    # New Custom Media Cost Variables
    new_cust_GluCon_Mat = glucose_cons_in_mat(new_cust_BRWV,new_cust_ACC,new_cust_Ug,new_cust_MatTime)
    new_cust_GluCon_Growth = total_glu_consume_growth(new_cust_ACC,new_cust_Ug,new_cust_hr_doub)
    new_cust_GluInCharge = float(new_cust_BRWV * new_cust_GConInBM)
    new_cust_TotCluConBatch = new_cust_GluCon_Growth + new_cust_GluCon_Mat
    new_cust_MediaChargeBatch = new_cust_TotCluConBatch / new_cust_GluInCharge
    new_cust_Media_Vol = new_cust_BRWV * new_cust_MediaChargeBatch
    new_cust_BatchPerYear = AnnOpTime / (new_cust_MatTime + growth_time(new_cust_hr_doub))
    new_cust_CellMassBatch = cell_mass_per_batch(new_cust_BRWV,new_cust_ACC)
    new_cust_ACBM = new_cust_CellMassBatch * new_cust_BatchPerYear
    new_cust_BioReact = DesiredMassMeat / new_cust_ACBM
    new_cust_AnnBatches = new_cust_BioReact * new_cust_BatchPerYear
    new_BioEquip_Cust = new_cust_BioReact * tot_fixed_eq_costs
    new_BioEquip_Cust_total = new_BioEquip_Cust * 2
    new_Fix_Manu_Cust_Cost = new_BioEquip_Cust_total * FixManuCost_Factor
    new_cust_Media_Cost = float(BaseMedia_cost + 
                        TGFB[0] + 
                        Transferrin[0] + 
                        (Insulin_cost * Insulin_conc) + 
                        (NaSe_cost * NaSe_conc) + 
                        (NaHCO3_cost * NaHCO3_conc) + 
                        (AA2p_cost * AA2P_conc) + 
                        (new_cust_FGF2Con * new_cust_FGF2Cost))
    new_cust_AnnVolMedia = new_cust_Media_Vol * new_cust_AnnBatches
    new_cust_AnnMediaCost = new_cust_AnnVolMedia * new_cust_Media_Cost
    # New O2 Custom Costs
    new_cust_O2_cons_in_mat = float((new_cust_BRWV * new_cust_ACC * 1000) * new_cust_MatTime * oxygen_comsump)
    new_cust_initial_O2_batch = float(((new_cust_MediaChargeBatch * new_cust_BRWV) 
                                       * media_Density * perc_O2_initial_charge) / mm_O2)
    new_cust_total_O2_cons_growth = total_O2_consume_growth(new_cust_ACC,new_cust_hr_doub)
    new_cust_O2_consum_batch = new_cust_total_O2_cons_growth + new_cust_initial_O2_batch + new_cust_O2_cons_in_mat
    new_cust_Ann_O2_Consum = (new_cust_O2_consum_batch * mm_O2 * new_cust_AnnBatches)/1000
    new_cust_Ann_O2_Cost = new_cust_Ann_O2_Consum * cost_O2
    # New Energy Costs
    new_cust_Elect_Cool_BioReact = float((new_cust_O2_consum_batch * new_cust_AnnBatches * heat_release_O2) / water_cooler_eff)
    new_cust_Elect_Heat_Media = float(((new_cust_AnnVolMedia * media_Density)*(desired_Temp - starting_Water_temp) 
                               * water_spec_Heat) / heater_eff)
    new_cust_total_Elect = new_cust_Elect_Heat_Media + new_cust_Elect_Cool_BioReact + Elect_Cool_ACBM
    new_cust_Elect_Cost = new_cust_total_Elect * cost_of_elect
    # New Labor Costs
    new_cust_Manpower_Cost = (new_cust_BioReact)
    new_cust_Ann_Labor_Cost = new_cust_Manpower_Cost * Labor_Cost_Corr_Fact * prod_worker_wage * AnnOpTime
    # New Non-Electric Costs
    new_cust_Process_Water = new_cust_AnnVolMedia / 1000
    new_cust_Ann_Water_Cost = new_cust_Process_Water * (Process_Water_Cost + Waste_Water_Cost + Oxidation_Water_Cost)
    # New Financing Values
    new_cust_tot_equity_cost = Total_Equity_Cost(new_BioEquip_Cust_total)
    new_cust_ann_equity_recov = Ann_Equity_Recov(new_cust_tot_equity_cost)
    new_cust_tot_debt_cost = Total_Debt_Cost(new_BioEquip_Cust_total)
    new_cust_ann_debt_payment = Ann_Debt_Payment(cust_tot_debt_cost)
    new_cust_tot_ann_payment = new_cust_ann_debt_payment + new_cust_ann_equity_recov
    new_cust_cap_expend_with_debt_equity = float(new_cust_tot_ann_payment * Economic_Life)
    new_cust_Min_Ann_Op_Cost = float(new_Fix_Manu_Cust_Cost + 
                                     new_cust_AnnMediaCost + 
                                     new_cust_Ann_O2_Cost + 
                                     new_cust_Elect_Cost + 
                                     new_cust_Ann_Labor_Cost + 
                                     new_cust_Ann_Water_Cost)
    new_cust_Min_ACBM_tomeet_Exp = float(new_cust_Min_Ann_Op_Cost / DesiredMassMeat)
    new_cust_Min_Ann_Cap_Op_Expend = (new_BioEquip_Cust_total / Economic_Life) + new_cust_Min_Ann_Op_Cost
    new_cust_Min_ACBM_Price = float(new_cust_Min_Ann_Cap_Op_Expend / DesiredMassMeat)
    # New Data lists 
    new_Costs_Bioequip = [BioEquip1,BioEquip2,BioEquip3,BioEquip4,new_BioEquip_Cust]
    new_Min_Cap_exp = [BioEquip1_total,BioEquip2_total,BioEquip3_total,BioEquip4_total,new_BioEquip_Cust_total]
    new_Costs_Fixed_Manu = [Fix_Manu_Cost1,Fix_Manu_Cost2,Fix_Manu_Cost3,Fix_Manu_Cost4,new_Fix_Manu_Cust_Cost]
    new_AnnMediaCosts = [AnnMediaCost1,AnnMediaCost2,AnnMediaCost3,AnnMediaCost4,new_cust_AnnMediaCost]
    new_O2_costs = [Ann_O2_Cost1,Ann_O2_Cost2,Ann_O2_Cost3,Ann_O2_Cost4,new_cust_Ann_O2_Cost]
    new_Elect_costs = [Elect_Cost1,Elect_Cost2,Elect_Cost3,Elect_Cost4,new_cust_Elect_Cost]
    new_Labor_costs = [Ann_Labor_Cost1,Ann_Labor_Cost2,Ann_Labor_Cost3,Ann_Labor_Cost4,new_cust_Ann_Labor_Cost]
    new_Non_Electric_costs =[Ann_Water_Cost1,Ann_Water_Cost2,Ann_Water_Cost3,Ann_Water_Cost4,new_cust_Ann_Water_Cost]
    new_cap_expend_with_debt_equity = [cap_expend_with_debt_equity1,
                                       cap_expend_with_debt_equity2,
                                       cap_expend_with_debt_equity3,
                                       cap_expend_with_debt_equity4,
                                       new_cust_cap_expend_with_debt_equity]
    new_Min_Ann_Op_Cost = [Min_Ann_Op_Cost1,
                           Min_Ann_Op_Cost2,
                           Min_Ann_Op_Cost3,
                           Min_Ann_Op_Cost4,
                           new_cust_Min_Ann_Op_Cost]
    new_Min_ACBM_tomeet_Exp = [Min_ACBM_tomeet_Exp1,
                               Min_ACBM_tomeet_Exp2,
                               Min_ACBM_tomeet_Exp3,
                               Min_ACBM_tomeet_Exp4,
                               new_cust_Min_ACBM_tomeet_Exp]
    new_Min_Ann_Cap_Op_Expend = [Min_Ann_Cap_Op_Expend1,
                         Min_Ann_Cap_Op_Expend2,
                         Min_Ann_Cap_Op_Expend3,
                         Min_Ann_Cap_Op_Expend4,
                         new_cust_Min_Ann_Cap_Op_Expend]
    new_Min_ACBM_Price = [Min_ACBM_Price1,Min_ACBM_Price2,Min_ACBM_Price3,Min_ACBM_Price4,new_cust_Min_ACBM_Price]
    # Updated Figure 1
    new_fig1 = go.Figure()    
    new_fig1.add_trace(go.Bar(
        x=Scenarios,
        y=new_Costs_Bioequip,
        name='Bioreactor Costs',
        marker_color='indianred',
        offsetgroup=0,
        hovertemplate='Scenario: %{x}<br>Bioreactor Cost: %{y}<extra></extra>'
    ))
    new_fig1.add_trace(go.Bar(
        x=Scenarios,
        y=Costs_Fixed_Manu,
        name='Fixed Manufacturing Cost',
        marker_color='firebrick',
        offsetgroup=1,
        hovertemplate='Scenario: %{x}<br>Fixed Manufacturing Cost: %{y}<extra></extra>'
    ))
    new_fig1.add_trace(go.Bar(
        x=Scenarios,
        y=new_AnnMediaCosts,
        name='Annual Media Cost',
        marker_color='teal',
        offsetgroup=2,
        hovertemplate='Scenario: %{x}<br>Annual Media Cost: %{y}<extra></extra>'
    ))    
    new_fig1.add_trace(go.Bar(
        x=Scenarios,
        y=new_O2_costs,
        name='Annual O2 Cost',
        marker_color='grey',
        offsetgroup=3,
        hovertemplate='Scenario: %{x}<br>Annual O2 Cost: %{y}<extra></extra>'
    ))
    new_fig1.add_trace(go.Bar(
        x=Scenarios,
        y=new_Elect_costs,
        name='Annual Energy Costs',
        marker_color='#ff0586',
        offsetgroup=4,
        hovertemplate='Scenario: %{x}<br>Annual Energy Cost: %{y}<extra></extra>'
    ))
    new_fig1.add_trace(go.Bar(
        x=Scenarios,
        y=new_Labor_costs,
        name='Annual Labor Costs',
        marker_color='#75264f',
        offsetgroup=5,
        hovertemplate='Scenario: %{x}<br>Annual Labor Cost: %{y}<extra></extra>'
    ))
    new_fig1.add_trace(go.Bar(
        x=Scenarios,
        y=new_Non_Electric_costs,
        name='Annual Non-Electric Utility Costs',
        marker_color='#6a2675',
        offsetgroup=6,
        hovertemplate='Scenario: %{x}<br>Annual Non-Electric Utility Cost: %{y}<extra></extra>'
    ))
    new_fig1.update_layout(xaxis_tickangle=45, yaxis_type="log", yaxis_title="US Dollars ($)")
    # Update Figure 2
    new_fig2 = go.Figure()
    new_fig2.add_trace(go.Bar(
        x=Scenarios,
        y=new_Min_Cap_exp,
        name='Min. Capital Expeditures',
        marker_color='#FFA505',
        offsetgroup=0,
        hovertemplate='Scenario: %{x}<br>Minimal Capital Expediture: %{y}<extra></extra>'
    ))
    new_fig2.add_trace(go.Bar(
        x=Scenarios,
        y=new_cap_expend_with_debt_equity,
        name='Capital Expenditures (with debt & equity)',
        marker_color='#ff0586',
        offsetgroup=1,
        hovertemplate='Scenario: %{x}<br>Capital Expeditures: %{y}<extra></extra>'
    ))
    new_fig2.add_trace(go.Bar(
        x=Scenarios,
        y=new_Min_Ann_Op_Cost,
        name='Min. Ann. Op. Costs',
        marker_color='#6a2675',
        offsetgroup=2,
        hovertemplate='Scenario: %{x}<br>Minimum Annual Operating Cost: %{y}<extra></extra>'
    ))
    new_fig2.add_trace(go.Bar(
        x=Scenarios,
        y=new_Min_ACBM_tomeet_Exp,
        name='Min. price of ACBM for Ann. Op. Exp.',
        marker_color='firebrick',
        offsetgroup=3,
        hovertemplate='Scenario: %{x}<br>Minimum price of ACBM to meet Annual Operating Expenses: %{y}<extra></extra>'
    ))
    new_fig2.add_trace(go.Bar(
        x=Scenarios,
        y=new_Min_Ann_Cap_Op_Expend,
        name='Min. Ann. Capital & Op. Expend.',
        marker_color='#ff4500',
        offsetgroup=4,
        hovertemplate='Scenario: %{x}<br>Minimum Annual Capital and Operating Expenditures: %{y}<extra></extra>'
    ))
    new_fig2.add_trace(go.Bar(
        x=Scenarios,
        y=new_Min_ACBM_Price,
        name='Min. price of ACBM for Ann. Capital & Op. Exp.',
        marker_color='#C7509F',
        offsetgroup=5,
        hovertemplate='Scenario: %{x}<br>Minimum price of ACBM to meet Annual Capital and Operating Expenses: %{y}<extra></extra>'
    ))
    new_fig2.update_layout(xaxis_tickangle=45, yaxis_type="log", yaxis_title="US Dollars ($)")
    return [new_fig1, 
            u'The custom number of bioreactors is {:20}.'.format(int(new_cust_BioReact)),
            u'The custom bioreactor cost is ${:20,.2f}.'.format(new_BioEquip_Cust),
            u'The custom minimum capital expenditures is ${:20,.2f}.'.format(new_BioEquip_Cust_total),
            u'The custom fixed manufacturing cost is ${:20,.2f}.'.format(new_Fix_Manu_Cust_Cost),
            u'The custom cost of media is ${:20,.2f} per liter.'.format(new_cust_Media_Cost),            
            u'The custom annual cost of media is ${:20,.2f}.'.format(new_cust_AnnMediaCost),
            u'The custom annual cost of O2 is ${:20,.2f}.'.format(new_cust_Ann_O2_Cost),
            u'The custom annual energy cost is ${:20,.2f}.'.format(new_cust_Elect_Cost),
            u'The custom annual labor cost is ${:20,.2f}.'.format(new_cust_Ann_Labor_Cost),
            u'The custom annual non-electric utility cost is ${:20,.2f}.'.format(new_cust_Ann_Water_Cost),
            new_fig2,
            u'The custom number of annual batches is {:20}.'.format(int(new_cust_AnnBatches)),
            u'The custom annual volume of media is {:20,.2f} liter.'.format(new_cust_AnnVolMedia),
            u'The custom capital expenditures, with debt and equity recovery, is ${:20,.2f}.'.format(new_cust_cap_expend_with_debt_equity),
            u'The custom minimum annual operating costs are ${:20,.2f}.'.format(new_cust_Min_Ann_Op_Cost),
            u'The custom minimum price of ACBM to meet annual operating expenses are ${:20,.2f} per kg.'.format(new_cust_Min_ACBM_tomeet_Exp),
            u'The custom minimum annual capital and operating expenses are ${:20,.2f}.'.format(new_cust_Min_Ann_Cap_Op_Expend),
            u'The custom minimum price of ACBM to meet annual capital and operating expenses are ${:20,.2f} per kg.'.format(new_cust_Min_ACBM_Price),
            u'The custom volume of media per batch is {:20,.2f} L'.format(new_cust_Media_Vol),
            u'The custom media charge per batch is {:20,.2f}.'.format(new_cust_MediaChargeBatch),
            u'The custom total glucose consumed per batch is {:20,.2f}.'.format(new_cust_TotCluConBatch),
            u'The custom glucose per charge is {:20,.2f}.'.format(cust_GluInCharge),
            u'The custom glucose consumed during maturation is {:20,.2f}.'.format(new_cust_GluCon_Mat),
            u'The custom glucose consumed during growth is {:20,.2f}.'.format(cust_GluCon_Growth),
            u'The custom annual consumption of O2 is {:20,.2f}.'.format(new_cust_Ann_O2_Consum),
            u'The custom consumption of O2 per batch is {:20,.2f}.'.format(new_cust_O2_consum_batch),
            u'The custom O2 consumed in growth phase is {:20,.2f}.'.format(new_cust_total_O2_cons_growth),
            u'The custom total energy requirement is {:20,.2f} kWh.'.format(new_cust_total_Elect),
            u'The custom energy requirement to cool bioreactors is {:20,.2f} kWh.'.format(new_cust_Elect_Cool_BioReact),
            u'The custom energy requirement to heat bioreactors is {:20,.2f} kWh.'.format(new_cust_Elect_Heat_Media),
            u'The custom total annual payment with captial expenditures is ${:20,.2f}.'.format(new_cust_tot_ann_payment)
           ]

##Bioreactor Slider Chained Callbacks ##

@app.callback(
    Output('bioreactor_output', 'children'),
    [Input('bioreactslider','value')])

def update_scale1_output1(slider1_input):
    bio_output = slider1_input
    if bio_output > 25000:
        return u'The custom working volume of the bioreactors is set to {} L. Bioreactors used for animal cell culture with working volumes greater than 25,000 L are custom bioreactors and as of 2019 are not commercially available.'.format(bio_output)
    else:
        return u'The custom working volume of the bioreactors is set to {} L.'.format(bio_output)

## Slider Chained Callbacks ##

@app.callback(Output('cust_FGF2Con_output', 'children'),
              [Input('fgf2_gL_slider','value')])

def update_scale2_output(slider2_input):
    return u'The concentration of FGF-2 is set to {:.2e} g/L.'.format(slider2_input)

@app.callback(Output('cust_FGF2Cost_output','children'),
              [Input('fgf2_costg_slider','value')])

def update_scale3_output(slider3_input):
    return u'The custom cost of FGF-2 is set to $ {:.2e} per gram.'.format(slider3_input)

@app.callback(Output('acc_output','children'),
              [Input('acc_slider','value')])

def update_scale4_output(slider4_input):
    return u'The custom achievable cell concentration is set to {:.2e} cells/mL.'.format(slider4_input)

@app.callback(Output('mat_time_output','children'),
              [Input('mat_time_slider','value')])

def update_scale5_output(slider5_input):
    return u'The cell maturation time is set to {} hours.'.format(slider5_input)

@app.callback(Output('hr_doub_output','children'),
              [Input('hr_doub_slider','value')])

def update_scale6_output(slider6_input):
    return u'The custom hours per doubling of cells is set to {} hours.'.format(slider6_input)

@app.callback(Output('ug_output','children'),
              [Input('ug_slider','value')])

def update_scale7_output(slider7_input):
    return u'The custom Glucose consumption rate per cell is set to {:.2e} mol/(h*cell).'.format(slider7_input / 10**16)

@app.callback(Output('GConInBM_output','children'),
              [Input('GConInBM_slider','value')])

def update_scale8_output(slider8_input):
    return u'The custom Glucose concentration in basal media is set to {:.2e} mol/L.'.format(slider8_input)

#### App launching functions ######

port = 8050 

def open_browser():
    webbrowser.open_new("http://localhost:{}".format(port))
    
application = app.server

if __name__ == '__main__':
    Timer(0, open_browser).start();
    app.run_server(debug=True, port=port)
