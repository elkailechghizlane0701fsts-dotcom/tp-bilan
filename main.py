from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calculs import filtration, chauffage

app = FastAPI(title="TP Bilan matière")

class Donnees(BaseModel):
    m0: float = 1000      # débit initial (kg/h)
    x0: float = 0.02      # fraction d'insoluble
    y0: float = 0.1       # fraction de soluble
    xeau: float = 0.88    # fraction d'eau
    cp: float = 3.8       # kJ/kg.K
    t1: float = 20        # température initiale (°C)
    t2: float = 80        # température finale (°C)

@app.get("/")
def accueil():
    return {"message": "API du TP bilan matière. Allez sur /docs pour tester."}

@app.post("/bilan")
def calcul_bilan(d: Donnees):
    if abs(d.x0 + d.y0 + d.xeau - 1) > 1e-6:
        raise HTTPException(status_code=400, detail="La somme des fractions doit être égale à 1")

    m1, y1, xeau1 = filtration(d.m0, d.x0, d.y0, d.xeau)
    q_kj_h, q_kw = chauffage(m1, d.cp, d.t1, d.t2)

    return {
        "debit_apres_filtration_kg_h": round(m1, 2),
        "fraction_soluble": round(y1, 4),
        "fraction_eau": round(xeau1, 4),
        "chaleur_kJ_h": round(q_kj_h, 2),
        "puissance_kW": round(q_kw, 2),
    }