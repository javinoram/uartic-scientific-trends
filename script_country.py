import pandas as pd
import numpy as np

lista_paises = ["chile", "spain", "united kingdom", "united states",
                "germany", "france", "argentina", "australia", "brazil",
                "canada", "italy", "south africa", "china", "switzerland",
                "japan", "new zealand", "mexico", "netherlands", "norway",
                "belgium", "portugal", "denmark", "peru", "india", "sweden",
                "austria", "colombia", "south korea", "czech republic", "poland",
                "ecuador", "malaysia", "russian federation", "ireland", "costa rica",
                "finland", "uruguay"]
def contador_paises(cadena):
    contador = 0
    for p in lista_paises:
        if p in cadena.lower():
            contador = contador+1
    return contador

def contar_veces_chile(cadena):
    lista_personas = cadena.split(";")
    contador = 0
    for l in lista_personas:
        l_lower = l.lower()
        if "chile" in l_lower:
            contador = contador +1
    return contador


xls_base = pd.read_excel("data/lorenafiltro.xlsx")
xls_base_colums = xls_base.columns
xls_final = xls_base[["Authors", "Affiliations", "Authors with affiliations"]].to_numpy()
contador = 0
for row in xls_final:
    cociente = 1.0
    num_paises = contador_paises(row[1])
    contador = contador + cociente/num_paises
print("conteo parcial paises (lorena): ", contador )


xls_base = pd.read_excel("data/filtrouartic.xlsx")
xls_base_colums = xls_base.columns
xls_final = xls_base[["Authors", "Affiliations", "Authors with affiliations"]].to_numpy()
contador = 0
for row in xls_final:
    cociente = 1
    num_paises = contador_paises(row[1])
    contador = contador + cociente/num_paises
print("conteo parcial paises (uartic): ", contador )

