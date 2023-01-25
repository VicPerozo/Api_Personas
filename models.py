from pony.orm import *
from pony.utils import  datetime



db = Database()
db.bind(provider='postgres', user='postgres', password='0414', host='localhost', database='Personas')


class TablaPersonas(db.Entity):
    Nombre         = Required(str,unique=False)
    Apellido       = Required(str,unique=False)
    Edad           = Required(int,unique=False)
    Fecha_Creacion = Required(datetime,6)
    Fechar_Actualizaion =Optional(datetime,6)



db.generate_mapping(create_tables=True)



@db_session
def crear_persona(nombre,apellido,edad,fecha=datetime.now()):
     TablaPersonas(Nombre=nombre, Apellido=apellido, Edad=edad, Fecha_Creacion=fecha)


@db_session
def consulta_general():
    consulta = TablaPersonas.select()[:]
    consulta_dic = [f"Personas registradas a la fecha de = {datetime.now()}"
        ,(i.to_dict() for i in consulta)]
    print(consulta_dic)
    return consulta_dic

@db_session
def consulta_id(id):
    print(id)
    consulta = TablaPersonas[id]
    return {"Nombre":consulta.Nombre,"Apellido":consulta.Apellido,
            "Edad":consulta.Edad,"Fecha de creacion":consulta.Fecha_Creacion}


@db_session
def consulta_nombre(nombre):
    consulta = select(p for p in TablaPersonas if p.Nombre == nombre)[:]
    dic = list(i.to_dict() for i in consulta)
    print(dic)
    return dic

@db_session
def borarpersona_id(id):
    TablaPersonas[id].delete()

@db_session
def actualizar_personaid(id,nombre,apellido,edad,fecha=datetime.now()):
    con = TablaPersonas[id]
    con.Nombre   = nombre
    con.Apellido = apellido
    con.Edad     = edad
    con.Fechar_Actualizaion = fecha

#Creado Por = Victo Perozo