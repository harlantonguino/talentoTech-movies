from fastapi import FastAPI, Body 
from fastapi.responses import HTMLResponse
from movies_list import movies_list



app=FastAPI() 
app.title= "Mi primera aplicación de peliculas y análisis de datos"
app.version = "0.0.1"



@app.get('/', tags=['Home']) 
def message(): 
    return HTMLResponse('<h1> Hello World </h1>')



@app.get('/movies', tags=['Movies'])
def movies():
    return movies_list
  

@app.get('/movies/{_id}',tags=['Movies'])
def get_movie(id:int):
    for item in movies_list:
        if item['id']==id:
            return item
    return []
  
  

@app.post('/movies',tags=['Movies'])
def create_movie(id: int=Body (), title:str=Body(), overview:str=Body(), year:int=Body(),rating:float=Body(), category:str=Body()):
     
    movies_list.append({
         "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })

    return movies_list
     
