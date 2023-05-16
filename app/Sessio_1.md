Sessió 1
=========
FastAPI és un dels framweworks per a web aplications més ràpids del mercat, ja que es basa en Starlette un framework web de tipus
ASGI (Asyncronous Server Gateway Interface) que utilitza rutines asíncrones (asyncio) en comptes de síncrones 
com en els WSGI (Web Server Gateway Interface). A part, també segueix l'estàndard de definició d'API d'openAPI i JSON.


Instal·lació de FastAPI i la vostra primera aplicació web Rest-ful
--------------------------------------------------

Obriu el PyCharm Editor i creeu un projecte FastAPI (*FastAPI\>New
Project*). 

Es recomana crear un _environment_ de Python nou per a separar els paquets que farem servir en aquesta pràctica dels que ja tenim instal·lats. Si decidiu crear un, A _Location_ poseu una carpeta fora del projecte. Si la col·loqueu dins, assegureu-vos d'afegir aquest _environment_ al fitxer _.gitignore_ per a que no es puji al vostre repositori.

En les últimes versions de PyCharm, en crear un nou projecte de tipus fastapi ens l'instal·la automàticament. Si no, l'instal·larem escrivint:

`>>> pip install fastapi`

Després de la creació del projecte fastapi, veureu que hi ha un fitxer anomenat `main.py`

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

```

Podeu executar aquesta aplicació executant Run al menú del PyCharm. Després d'això
podeu veure la vostra primera aplicació web fastapi obrint aquest enllaç en
el vostre navegador web: <http://127.0.0.1:8000/>

També podeu executar-lo al terminal fent:

    uvicorn main:app --reload

Mireu la línia de codi anterior: `app.get (’/’)`. Aquest decorador
indica en quina URL i amb quin mètode HTTP s'executarà la funció que ve a continuació.

### Exercici 1: 

Afegeix aquest tros de codi a `main.py` després de la funció  `def say_hello`:

```python
@app.get('/python')
def like_python():
    return {'I like Python!'}
```

Torneu a executar l'aplicació i intenteu obrir al vostre navegador la URL corresponent a aquest nou missatge. Quina URL és? perquè?

Mireu la documentació de la vostra API generada de forma automàtica fent servir Swagger a:
<http://127.0.0.1:8000/docs>

i fent servir Redoc:
<http://127.0.0.1:8000/redoc>


A part del navegador podeu fer servir l'HTTP Client de Pycharm per provar els endpoints. Simplement cal que obriu el fitxer
`test_main.http` i escriviu allà les peticions HTTP que voleu fer, amb el format vist a classe de teoria, separats per `###`
Llavors podeu executar cada una de les peticions per separat o totes de cop. 
Per exemple:
```text
# Test your FastAPI endpoints

GET http://127.0.0.1:8000/
Accept: application/json

###
```


També ho podeu fer amb un script de python. El paquet `requests` us permet enviar sol·licituds HTTP amb molta facilitat. Com a exemple podeu escriure això en una consola interactiva de python. 
```python
import requests
url = "YOUR_URL"
response = requests.get(url)
response.json()
```

I finalment, hi ha una altra coneguda eina per a comprovar les crides a http anomenada Postman, que ofereix una interfície d'usuari amigable amb la qual fer sol·licituds HTTP:

<https://www.postman.com/downloads/>


Desenvolupament d'APIs amb fastapi
----------------------------------
### Operacions

Operacions és com es diuen als mètodes de HTTP en l'openAPI

A part del mètode `get`, en el decorator podeu fer servir tots els que hem vist a teoria:

- `@app.get()`: s’utilitza per sol·licitar informació 

- `@app.post()`: s’utilitza per afegir nous elements a la nostra estructura de dades 

- `@app.delete()`: s'utilitza per eliminar elements de la nostra estructura de dades

- `@app.put()`: s’utilitza per modificar els elements existents a la nostra estructura de dades

### PATH

Tal com vam veure a teoria, el path és l'última part de l'URL començant per la primera /.  També se'l pot anomenar
"endpoint" a "ruta". 
Veiem el següent exemple:

```python

from fastapi import FastAPI,HTTPException

fake_teams_db = [{"team_name": "Barça"}, {"team_name": "Madrid"}, {"team_name": "Valencia"}]

app = FastAPI()
@app.get("/teams/")
async def read_teams(skip: int = 0, limit: int = 10):
    return fake_teams_db[skip : skip + limit]

@app.get("/team/{team_name}")
async def read_team(team_name: str):
    team = next(iter([x for x in fake_teams_db if x["team_name"] == team_name]), None)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return {'team': team_name}


```
En el primer endpoint `/teams/` estem definint una funció `read_teams` on li diem els possibles paràmetres http que pot rebre.
Com heu vist a teoria aquests paràmetres, en l'URL, van a continuació d'un interrogant '?' i se separen entre ells per un `&`.
Entre la clau i el valor del paràmetre s'hi posa un '='.
Per exemple, 
http://127.0.0.1:8000/teams/?skip=1&limit=2
El resultat d'aquesta URl seria retornar 2 teams a partir del segon.

La part `{team_name}` a `’/team/{team_name}’` indica que hi ha una part variable en el path.
La funció `read_team` rebrà el paràmetre que hi hagi en la ruta i el passarà com `team_name` que serà de tipus string.
Es pot definir qualsevol tipus de dades per als paràmetres, en cas que falli la conversió donarà un error `HTTP/1.1 422 Unprocessable Entity`.

La funció la definim de tipus `async` perquè estem agafant les dades d'una estructura interna i, per tant, es pot fer 
de forma concurrent. Penseu que aquests mètodes es poden cridar de forma simultània per molts clients.

Com podeu veure, si no es troba l'equip, retornem un valor 404 corresponent a un error de sol·licitud http "No trobat".
També es poden enviar missatges que ajudin a obtenir més informació sobre possibles problemes.
Si voleu més informació sobre els codis de resposta HTTP, podeu trobar més informació en aquesta pàgina web (secció *Codis d’estat de la resposta HTTP*):
<https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods>

Així doncs, un URL vàlid que anomeni aquest recurs hauria de tenir aquest format: `http: //127.0.0.1:8000/team/Barça`.

#### L'ordre importa!

Si teniu dos paths que comencen iguals heu de declarar primer aquells que siguin fixos i després els que 
tinguin una part variable, sempre entra en el primer path que trobi que compleixi les condicions:

```python
from fastapi import FastAPI

app = FastAPI()
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

```
En aquest cas si voleu que entri a `users/me` ha d'estar definit abans del genèric `/users/{user_id}` 

Afegir un equip a la llista d'equips (exemple POST)
--------------------------------------------
El tipus de sol·licitud determinarà el tipus d’acció que volem realitzar amb les nostres dades. 
Ara implementarem, doncs, el mètode POST `@app.post("/teams/")` que utilitzarem per afegir un equip nou a les nostres
dades (a la nostra llista d'equips). És important entendre que la nova informació de l'equip s’inclourà al cos de sol·licitud 
POST.

Però primer farem un model de dades usant `Pydantic`

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

class Team(BaseModel):
    name: str
    country: str
    description: Optional[str] = None
    
    
fake_teams_db = []


app = FastAPI()



@app.post("/teams/")
async def create_team(team: Team):
    if not fake_teams_db:
        fake_teams_db.append(team)
    else:
        exists_team = next(iter([x for x in fake_teams_db if x.name == team.name]), None)
        if not exists_team:
            fake_teams_db.append(team)
        else:
            raise HTTPException(status_code=404, detail="Team already Exists, Use put for updating")
    return team

```

### Exercici 2:

Escriviu la classe `Team` en un fitxer anomenat `models.py` i importeu-la al fitxer principal `main.py`. 
Proveu el mètode post fent servir `requests` o una altra eina per fer tests d'APIs tot afegint la següent informació al cos del request:

``` html
###
POST http://127.0.0.1:8000/teams
Content-Type: application/json

{   "name": "CSC Futsal",
    "country": "Spain",
    "description": "Futbol Sala Team"}
```

Testing fent servir Pytest.
--------------------------

Per testejar els nostres endpoints, farem servir la llibreria `pytest` que ens permetrà fer tests unitaris i de integració.

Instal·leu els requeriments del fitxer `requirements.txt` amb el següent comandament:

```bash
pip install -r requirements.txt
```

Per definir els test farem servir el TestClient de FastAPI que ens permetrà fer peticions a la nostra API.
Escriviu aquest codi dins d'un fitxer anomenat `test_main.py`:

```python
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

```
Ara per executar pytest simplement heu d'executar el següent comandament:

```bash
pytest
```


Deures per a la propera setmana
--------

1. Adapteu el mètode `@app.get("/team/{team_name}")`  per a que funcioni amb el model anterior.

2. Escriviu el mètode DELETE que elimini un equip de la llista d'equips. Torneu un missatge indicant si aquest usuari s'ha suprimit o no i el codi corresponent.

3. Escriviu el mètode PUT que, si no existeix aquest equip, crea un equip nou i l'afegeix a la llista d'equips. En cas contrari, modifica els valors de l'equip amb aquest identificador amb la informació del cos de la sol·licitud del PUT (aquesta informació pot ser completa o parcial!). Retorna l'equip creat o modificat.

4.  Escriviu els mètodes GET, POST, DELETE i PUT per a un model anomenat Competition amb la URL:

        '/competitions/
    A sota teniu exemples de competicions, definiu el model Pydantic segons els exemples.

5.  Escriviu els mètodes GET, POST, DELETE i PUT per a un model anomenat Match amb la URL:

        '/matches/'

    A sota teniu exemples de competicions, definiu el model Pydantic segons els exemples.

6. Feu els mètodes GET per a competicions i matches donat l'ID. 
    
7. Proveu i comproveu tots els mètodes desenvolupats amb `requests` o una altra eina de prova d'APIs.

8. Feu un test per a cada mètode desenvolupat i proveu que tot funciona correctament.

``` python
competitions = [
    {'id': 0,
    'name': "Women's European Championship",
    'category': 'Senior',
    'sport': 'Volleyball',
    'teams': []},
    {'id': 1,
    'name': "1st Division League",
    'category': 'Junior',
    'sport': 'Football',
    'teams': []},
    {'id': 2,
    'name': "Women's Copa Catalunya",
    'category': 'Senior',
    'sport': 'Basketball',
    'teams': []},
    {'id': 3,
    'name': "1st Division League",
    'category': 'Junior',
    'sport': 'Futsal',
    'teams': []}
]

teams = [
    {'name': "CV Vall D'Hebron",
     'country': 'Spain'},
    {'name': 'CE Sabadell',
     'country': 'Spain'},
    {'name': 'Club Juventut Les Corts',
     'country': 'Spain'},
    {'name': 'Volei Rubi',
     'country': 'Spain'}
]

matches = [
    {'id': 0,
     'local': "CV Vall D'Hebron",
     'visitor': 'Volei Rubi',
     'date': '2022-07-03',
     'price': 15.20}
]
```


