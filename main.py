from fastapi import FastAPI
import models
from Shemas import *
app = FastAPI()



@app.get("/")
def root():
    return {"Mensaje":"Bienvenido a mi apiCrud"}

@app.get("/Persona")
def General():
    con = models.consulta_general()
    return con

@app.get("/Persona/id/{Persona_id}")
def consultaId(Persona_id:int):
    con = models.consulta_id(Persona_id)
    return con

@app.get("/Persona/{Nombre_persona}")
def consultaNombre(Nombre_persona:str):
    con = models.consulta_nombre(Nombre_persona)
    return con

@app.post("/Persona")
def insertar_persona(persona:Persona_post):
    models.crear_persona(persona.Nombre.lower(),
                         persona.Apellido.lower(),persona.Edad)
    return

@app.delete("/Persona/{id_persona}")
def borrar_persona(id_persona:int):
    models.borarpersona_id(id_persona)
    return {f"Persona id: {id_persona}":"Borrado con exito"}

@app.put("/Persona")
def actualizar(persona:Personas):
    models.actualizar_personaid(persona.id,persona.Nombre.lower()
                                ,persona.Apellido.lower(),persona.Edad)
    return "Exito"