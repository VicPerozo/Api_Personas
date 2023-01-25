from pydantic import BaseModel



class Personas(BaseModel):
    id       : int
    Nombre   : str
    Apellido : str
    Edad     : int

class Persona_post(BaseModel):
    Nombre: str
    Apellido: str
    Edad: int