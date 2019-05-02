from sqlalchemy import create_engine
# Import pandas
import pandas as pd
import math
import sys

engine = create_engine('postgresql://postgres:123@localhost:5432/diana')

renomear1 = {'ALT (m)':'alt','COB. PAIS (%)':'cob_pais',
'COB. ARB.(%)':'cob_arb','SOLO EXP.(%)':'solo_exp','A. PAV.(%)':'a_pav','A. EDF. (%)':'a_edf','ÁGUA(%)':'agua'}

renomear2 = {'T(°C) ':'temp','Ur (%)':'ur','ALT (m)':'alt','V(km/h)':'v'}

# Assign spreadsheet filename to `file`
file = 'DADOS REDE NEURAL COBERTURA DO SOLO TRANSECTOS.xlsx'
xl = pd.ExcelFile(file)
for sheet in xl.sheet_names:
    planilha = xl.parse(sheet)
    planilha.rename(columns=renomear1,inplace=True)
    planilha.columns = map(str.lower, planilha.columns)
    print(planilha.columns)
    planilha.to_sql(sheet.replace('.csv','').replace(' ','_').replace('VERÃO','VERAO').lower(), engine)

file = 'DADOS REDE NEURAL ESTAÇÕES UTM.xlsx'
xl = pd.ExcelFile(file)

for sheet in xl.sheet_names:
    planilha = xl.parse(sheet)
    planilha.rename(columns=renomear2,inplace=True)
    planilha.columns = map(str.lower, planilha.columns)
    planilha.to_sql(sheet.replace('.csv','').replace(' ','_').replace('VERÃO','VERAO').lower(), engine)