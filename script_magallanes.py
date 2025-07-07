import pandas as pd
import numpy as np

xls_base = pd.read_excel("data/filtrouartic.xlsx")
xls_base_colums = xls_base.columns
xls_final = xls_base[["Authors", "Affiliations", "Authors with affiliations"]].to_numpy()

contador = 0
trabajos = 0
for row in xls_final:
    if "universidad de magallanes" in row[1].lower() or "university of magallan" in row[1].lower():
        trabajos = trabajos+1
        cociente = 1.0
        num_aff = len( list(set([(aff.lower().split(","))[-3] for aff in row[2].split(";")])) )
        contador = contador + cociente/num_aff

print("magallanes (uartic): ", trabajos )
print("magallanes parcial (uartic): ", contador )

