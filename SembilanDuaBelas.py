import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#ffood
ffood = ctrl.Antecedent(
    np.arange(0,11,1),
    'consumption of fast food'
)
ffood['rarely'] = fuzz.trapmf(
    ffood.universe,
    [0,0,1,4]
)

ffood['moderate'] = fuzz.trapmf(
    ffood.universe,
    [1,4,6,9]
)

ffood['often'] = fuzz.trapmf(
    ffood.universe,
    [6,8,10,10]
)

#BMI
bmi = ctrl.Antecedent(
    np.arange(12,24,1),
    'BMI'
)

bmi['underweight'] = fuzz.trapmf(
    bmi.universe,
    [12,12, 13 ,14]
)

bmi['normal'] = fuzz.trapmf(
    bmi.universe,
    [13.5, 14, 17.5 ,18]
)

bmi['overweight'] = fuzz.trapmf(
    bmi.universe,
    [17, 18, 20.5 ,20.5]
)

#physical_activity
activities = ctrl.Antecedent(
    np.arange(0,11,1),
    'Physical activities'
)

activities['rarely'] = fuzz.trapmf(
    activities.universe,
    [0,0,1,5]
)
activities['moderate'] = fuzz.trapmf(
    activities.universe,
    [1,4,6,9]
)
activities['often'] = fuzz.trapmf(
    activities.universe,
    [5,9,10,10]
)

#fibre
fibre = ctrl.Antecedent(
    np.arange(0,101,1),
    'Consumption of fibre'
)

fibre['low'] = fuzz.trapmf(
fibre.universe,
    [0,0,20,40]
)
fibre['medium'] = fuzz.trapmf(
fibre.universe,
    [20,40,60,80]
)
fibre['high'] = fuzz.trapmf(
    fibre.universe,
    [60,80,100,100]
)

#output
risk_level = ctrl.Consequent(
    np.arange(0,101,1),
    'risk_level'
)
risk_level['minimal'] = fuzz.trimf(
    risk_level.universe,
    [0, 15 ,25]
)

risk_level['low'] = fuzz.trimf(
    risk_level.universe,
    [20,35,50]
)

risk_level['moderate'] = fuzz.trimf(
    risk_level.universe,
    [40,  57.5 ,75]
)
risk_level['high'] = fuzz.trimf(
    risk_level.universe,
    [70,  85, 100]
)

R1=ctrl.Rule(bmi ['underweight'] & activities ['rarely'] & ffood  ['rarely'] & fibre ['low'], risk_level ['minimal'])
R2=ctrl.Rule(bmi ['underweight'] & activities ['moderate'] & ffood  ['rarely'] & fibre ['low'], risk_level ['minimal'])
R3=ctrl.Rule(bmi ['underweight'] & activities ['often'] & ffood  ['rarely'] & fibre ['low'], risk_level ['minimal'])
R4=ctrl.Rule(bmi ['underweight'] & activities ['rarely'] & ffood  ['moderate'] & fibre ['low'], risk_level ['low'])
R5=ctrl.Rule(bmi ['underweight'] & activities ['rarely'] & ffood  ['often'] & fibre ['low'], risk_level ['moderate'])
R6=ctrl.Rule(bmi ['underweight'] & activities ['rarely'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['minimal'])
R7=ctrl.Rule(bmi ['underweight'] & activities ['rarely'] & ffood  ['rarely'] & fibre ['high'], risk_level ['minimal'])
R8=ctrl.Rule(bmi ['normal'] & activities ['rarely'] & ffood  ['rarely'] & fibre ['low'], risk_level ['low'])
R9=ctrl.Rule(bmi ['normal'] & activities ['moderate'] & ffood  ['rarely'] & fibre ['low'], risk_level ['minimal'])
R10=ctrl.Rule(bmi ['normal'] & activities ['often'] & ffood  ['rarely'] & fibre ['low'], risk_level ['low'])
R11=ctrl.Rule(bmi ['normal'] & activities ['rarely'] & ffood  ['moderate'] & fibre ['low'], risk_level ['moderate'])
R12=ctrl.Rule(bmi ['normal'] & activities ['rarely'] & ffood  ['often'] & fibre ['low'], risk_level ['high'])
R13=ctrl.Rule(bmi ['normal'] & activities ['rarely'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['minimal'])
R14=ctrl.Rule(bmi ['normal'] & activities ['rarely'] & ffood  ['rarely'] & fibre ['high'], risk_level ['minimal'])
R15=ctrl.Rule(bmi ['overweight'] & activities ['rarely'] & ffood  ['rarely'] & fibre ['low'], risk_level ['high'])
R16=ctrl.Rule(bmi ['overweight'] & activities ['moderate'] & ffood  ['rarely'] & fibre ['low'], risk_level ['moderate'])
R17=ctrl.Rule(bmi ['overweight'] & activities ['often'] & ffood  ['rarely'] & fibre ['low'], risk_level ['moderate'])
R18=ctrl.Rule(bmi ['overweight'] & activities ['rarely'] & ffood  ['moderate'] & fibre ['low'], risk_level ['high'])
R19=ctrl.Rule(bmi ['overweight'] & activities ['rarely'] & ffood  ['often'] & fibre ['low'], risk_level ['high'])
R20=ctrl.Rule(bmi ['overweight'] & activities ['rarely'] & ffood  ['rarely'] & fibre ['high'], risk_level ['moderate']) 
R21=ctrl.Rule(bmi ['overweight'] & activities ['rarely'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['high'])
R22=ctrl.Rule(bmi ['underweight'] & activities ['moderate'] & ffood  ['moderate'] & fibre ['medium'], risk_level ['minimal'])
R23=ctrl.Rule(bmi ['underweight'] & activities ['rarely'] & ffood  ['moderate'] & fibre ['medium'], risk_level ['low'])
R24=ctrl.Rule(bmi ['underweight'] & activities ['often'] & ffood  ['moderate'] & fibre ['medium'], risk_level ['moderate'])
R25=ctrl.Rule(bmi ['underweight'] & activities ['moderate'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['minimal'])
R26=ctrl.Rule(bmi ['underweight'] & activities ['moderate'] & ffood  ['often'] & fibre ['medium'], risk_level ['low'])
R27=ctrl.Rule(bmi ['underweight'] & activities ['moderate'] & ffood  ['moderate'] & fibre ['low'], risk_level ['low'])
R28=ctrl.Rule(bmi ['underweight'] & activities ['moderate'] & ffood  ['moderate'] & fibre ['high'], risk_level ['minimal'])
R29=ctrl.Rule(bmi ['normal'] & activities ['moderate'] & ffood  ['moderate'] & fibre ['medium'], risk_level ['moderate'])
R30=ctrl.Rule(bmi ['normal'] & activities ['rarely'] & ffood  ['moderate'] & fibre ['medium'], risk_level ['high'])
R31=ctrl.Rule(bmi ['normal'] & activities ['often'] & ffood  ['moderate'] & fibre ['medium'], risk_level ['moderate'])
R32=ctrl.Rule(bmi ['normal'] & activities ['moderate'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['low'])
R33=ctrl.Rule(bmi ['normal'] & activities ['moderate'] & ffood  ['often'] & fibre ['medium'], risk_level ['high'])
R34=ctrl.Rule(bmi ['normal'] & activities ['moderate'] & ffood  ['moderate'] & fibre ['low'], risk_level ['moderate'])
R35=ctrl.Rule(bmi ['normal'] & activities ['moderate'] & ffood  ['moderate'] & fibre ['high'], risk_level ['low'])
R36=ctrl.Rule(bmi ['overweight'] & activities ['moderate'] & ffood  ['moderate'] & fibre ['medium'], risk_level ['high'])
R37=ctrl.Rule(bmi ['overweight'] & activities ['rarely'] & ffood  ['moderate'] & fibre ['medium'], risk_level ['high'])
R38=ctrl.Rule(bmi ['overweight'] & activities ['often'] & ffood  ['moderate'] & fibre ['medium'], risk_level ['moderate'])
R39=ctrl.Rule(bmi ['overweight'] & activities ['moderate'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['moderate'])
R40=ctrl.Rule(bmi ['overweight'] & activities ['moderate'] & ffood  ['often'] & fibre ['medium'], risk_level ['high'])
R41=ctrl.Rule(bmi ['overweight'] & activities ['moderate'] & ffood  ['moderate'] & fibre ['low'], risk_level ['high'])
R42=ctrl.Rule(bmi ['overweight'] & activities ['moderate'] & ffood  ['moderate'] & fibre ['high'], risk_level ['high'])
R43=ctrl.Rule(bmi ['underweight'] & activities ['often'] & ffood  ['often'] & fibre ['high'], risk_level ['minimal'])
R44=ctrl.Rule(bmi ['underweight'] & activities ['rarely'] & ffood  ['often'] & fibre ['high'], risk_level ['moderate'])
R45=ctrl.Rule(bmi ['underweight'] & activities ['moderate'] & ffood  ['often'] & fibre ['high'], risk_level ['low'])
R46=ctrl.Rule(bmi ['underweight'] & activities ['often'] & ffood  ['rarely'] & fibre ['high'], risk_level ['minimal'])
R47=ctrl.Rule(bmi ['underweight'] & activities ['often'] & ffood  ['moderate'] & fibre ['high'], risk_level ['low'])
R48=ctrl.Rule(bmi ['underweight'] & activities ['often'] & ffood  ['often'] & fibre ['low'], risk_level ['moderate'])
R49=ctrl.Rule(bmi ['underweight'] & activities ['often'] & ffood  ['often'] & fibre ['medium'], risk_level ['low'])
R50=ctrl.Rule(bmi ['normal'] & activities ['often'] & ffood  ['often'] & fibre ['high'], risk_level ['moderate'])
R51=ctrl.Rule(bmi ['normal'] & activities ['rarely'] & ffood  ['often'] & fibre ['high'], risk_level ['high'])
R52=ctrl.Rule(bmi ['normal'] & activities ['moderate'] & ffood  ['often'] & fibre ['high'], risk_level ['high'])
R53=ctrl.Rule(bmi ['normal'] & activities ['often'] & ffood  ['rarely'] & fibre ['high'], risk_level ['low'])
R54=ctrl.Rule(bmi ['normal'] & activities ['often'] & ffood  ['moderate'] & fibre ['high'], risk_level ['moderate'])
R55=ctrl.Rule(bmi ['normal'] & activities ['often'] & ffood  ['often'] & fibre ['low'], risk_level ['high'])
R56=ctrl.Rule(bmi ['normal'] & activities ['often'] & ffood  ['often'] & fibre ['medium'], risk_level ['high'])
R57=ctrl.Rule(bmi ['overweight'] & activities ['often'] & ffood  ['often'] & fibre ['high'], risk_level ['high'])
R58=ctrl.Rule(bmi ['overweight'] & activities ['rarely'] & ffood  ['often'] & fibre ['high'], risk_level ['high'])
R59=ctrl.Rule(bmi ['overweight'] & activities ['moderate'] & ffood  ['often'] & fibre ['high'], risk_level ['high'])
R60=ctrl.Rule(bmi ['overweight'] & activities ['often'] & ffood  ['rarely'] & fibre ['high'], risk_level ['low'])
R61=ctrl.Rule(bmi ['overweight'] & activities ['often'] & ffood  ['moderate'] & fibre ['high'], risk_level ['moderate'])
R62=ctrl.Rule(bmi ['overweight'] & activities ['often'] & ffood  ['often'] & fibre ['low'], risk_level ['high'])
R63=ctrl.Rule(bmi ['overweight'] & activities ['often'] & ffood  ['often'] & fibre ['medium'], risk_level ['high']) 
R64=ctrl.Rule(bmi ['underweight'] & activities ['rarely'] & ffood  ['moderate'] & fibre ['high'], risk_level ['minimal'])
R65=ctrl.Rule(bmi ['underweight'] & activities ['rarely'] & ffood  ['often'] & fibre ['medium'], risk_level ['low'])
R66=ctrl.Rule(bmi ['underweight'] & activities ['moderate'] & ffood  ['rarely'] & fibre ['high'], risk_level ['minimal'])
R67=ctrl.Rule(bmi ['underweight'] & activities ['often'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['minimal'])
R68=ctrl.Rule(bmi ['underweight'] & activities ['often'] & ffood  ['moderate'] & fibre ['low'], risk_level ['minimal'])
R69=ctrl.Rule(bmi ['underweight'] & activities ['often'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['minimal'])
R70=ctrl.Rule(bmi ['normal'] & activities ['rarely'] & ffood  ['moderate'] & fibre ['high'], risk_level ['moderate']) 
R71=ctrl.Rule(bmi ['normal'] & activities ['rarely'] & ffood  ['often'] & fibre ['medium'], risk_level ['high'])
R72=ctrl.Rule(bmi ['normal'] & activities ['moderate'] & ffood  ['rarely'] & fibre ['high'], risk_level ['low'])
R73=ctrl.Rule(bmi ['normal'] & activities ['often'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['minimal'])
R74=ctrl.Rule(bmi ['normal'] & activities ['often'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['moderate'])
R75=ctrl.Rule(bmi ['normal'] & activities ['often'] & ffood  ['moderate'] & fibre ['low'], risk_level ['low'])
R76=ctrl.Rule(bmi ['overweight'] & activities ['often'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['moderate'])
R77=ctrl.Rule(bmi ['overweight'] & activities ['rarely'] & ffood  ['often'] & fibre ['medium'], risk_level ['high'])
R78=ctrl.Rule(bmi ['overweight'] & activities ['moderate'] & ffood  ['rarely'] & fibre ['high'], risk_level ['moderate'])
R79=ctrl.Rule(bmi ['overweight'] & activities ['often'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['low'])
R80=ctrl.Rule(bmi ['overweight'] & activities ['often'] & ffood  ['moderate'] & fibre ['low'], risk_level ['moderate'])
R81=ctrl.Rule(bmi ['overweight'] & activities ['often'] & ffood  ['rarely'] & fibre ['medium'], risk_level ['moderate'])

risk_control = ctrl.ControlSystem([R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,R19,R20,R21,R22,R23,R24,R25,R26,
R27,
R28,
R29,
R30,
R31,
R32,
R33,
R34,
R35,
R36,
R37,
R38,
R39,
R40,
R41,
R42,
R43,
R44,
R45,
R46,
R47,
R48,
R49,
R50,
R51,
R52,
R53,
R54,
R55,
R56,
R57,
R58,
R59,
R60,
R61,
R62,
R63,
R64,
R65,
R66,
R67,
R68,
R69,
R70,
R71,
R72,
R73,
R74,
R75,
R76,
R77,
R78,
R79,
R80,
R81])

obesity_risk = ctrl.ControlSystemSimulation(risk_control)

class SembilanDuaBelas:
    bmi = 0
    ffood = 0
    fibre = 0
    activities = 0
    
    def __init__(self):
        print('nice')
    
    def set_data(self, bmi, ffood, fibre, activities):
        self.bmi = bmi
        self.ffood = ffood
        self.fibre = fibre
        self.activities = activities
        
        obesity_risk.input['BMI'] = bmi
        obesity_risk.input['Physical activities'] = activities
        obesity_risk.input['consumption of fast food'] = ffood
        obesity_risk.input['Consumption of fibre'] = fibre
        
    def calc_risk(self):
        obesity_risk.compute()
        return (obesity_risk.output['risk_level'])
        