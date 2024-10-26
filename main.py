from fastapi import FastAPI #import de fastapi
from pydantic import BaseModel #import de BaseModel para validar los datos
from typing import Optional #import de Optional para que un dato sea opcional
from routes.gasto import gasto #importar las rutas de gasto

app = FastAPI()

app.include_router(gasto) #usar las rutas de gasto


class Gasto(BaseModel):
    nombre: str
    valor: int
    categoria: str
    descripcion: Optional[str]

@app.get("/")
def index():
    return {"msj": "Hola mundo"}

# @app.get("/gastos/{id}")
# def mostrarGastos(id: int):
#     return {"data": id}

# @app.post("/gastos")
# def insertarGastos(gasto: Gasto):
#     return {"msj": f"gasto {gasto.nombre} insertado"}

