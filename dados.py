# Import pandas
import pandas as pd
import math

# Assign spreadsheet filename to `file`
file = 'DADOS REDE NEURAL COBERTURA DO SOLO TRANSECTOS.xlsx'
xl = pd.ExcelFile(file)
solo2011 = xl.parse('COB. TRANSECTO 2011-2012')
solo2016 = xl.parse('COB. TRANSECTO 2016')

file = 'DADOS REDE NEURAL ESTAÇÕES UTM.xlsx'
xl = pd.ExcelFile(file)

for sheet in xl.sheet_names:
    planilha = xl.parse(sheet)
    print(planilha.shape)
    distancias = []
    if('2011' in sheet):
        for i in range(1, planilha.shape[0]):
            for j in range(1, solo2011.shape[0]):
                l1 = planilha.iloc[[i]]
                l2 = solo2011.iloc[[j]]
                distancia = math.sqrt((l2[0] - l1[1])**2 + (l2[1] - l1[2])**2)
                distancias.append(distancia)
                
