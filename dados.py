# Import pandas
import pandas as pd
import math
import sys

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

    if('2011' in sheet):
        nomes = list(planilha.columns)+list(solo2011.columns)
        res = pd.DataFrame(columns=nomes)
        idx=0
        menor = sys.float_info.max
        linha = None
        for i in range(1, planilha.shape[0]):
            l1 = planilha.iloc[[i]]
            for j in range(1, solo2011.shape[0]):
                l2 = solo2011.iloc[[j]]
                distancia = math.sqrt((l2.values[0][0] - l1.values[0][1])**2 + (l2.values[0][1] - l1.values[0][2])**2)
                if(distancia < menor):
                    menor = distancia
                    linha = l2
            nova = list(l1.values[0])  + list(linha.values[0])
            res.loc[idx] = nova
            idx=idx+1

        res.to_csv(sheet + '.csv',index=False)
        exit(1)
