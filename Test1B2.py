#Author Kevin Turner CS21B
#Test stuff for class
from collections import defaultdict

chemicalSamples={'a':12, 'b':6, 'c':10, 'd':8}

def firstFormula(x):
    return x**3+8*x**2-12*x+125

def secondFormula(x):
    return 0.5*x**3+12*x**2-2*x+75

listOfFormulas = [firstFormula, secondFormula]
scoreReport = {}
for chemical in chemicalSamples:
    for formula in listOfFormulas:
        Score = formula(chemicalSamples[chemical])
        print('Score of',"'", chemical,"'", ' from ', formula.__name__, '%6.2f'  % Score)
        scoreReport[chemical]=formula(chemicalSamples[chemical])
        scoreReport[chemical] = scoreReport[chemical], formula(chemicalSamples[chemical])
        #scoreReport[chemical].append(formula(chemicalSamples[chemical]))
print(scoreReport)