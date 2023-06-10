from sqlite3 import IntegrityError

from fastapi import Depends, FastAPI, HTTPException
from pydantic.main import Enum
from sqlalchemy.orm import Session
from typing import List
import repository, models, schemas
from pprint import pprint
from database import SessionLocal, engine

from sqlalchemy import select


from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/dist/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


templates = Jinja2Templates(directory="frontend/dist")
@app.get("/")
async def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/")
async def main():
    return {"message": "Hello World"}


################################CROSS ARRIBA###########3

models.Base.metadata.create_all(bind=engine)  # Creem la base de dades amb els models que hem definit a SQLAlchemy

#app = FastAPI()
#print(Enum(*models.categories_list))




# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
Session = Depends(get_db)




@app.get("/champs", response_model=list[schemas.Champ])
def get_champs(db: Session = Depends(get_db)):
    return repository.get_champs(db)

@app.get("/souls", response_model=list[schemas.SoulPassive])
def get_souls(db: Session = Depends(get_db)):
    ret = repository.get_souls(db)
    for soul in ret:
        passive_description = repository.get_passive_by_id(db=db, id=soul.passive).description
        soul.passive_desc = passive_description
    print(ret)
    return ret

@app.get("/build/{champ_id}", response_model=List[schemas.Build])
def get_build_by_champId(champ_id: str, db: Session = Depends(get_db)):
    return repository.get_build_by_champId(db=db, id=champ_id)

@app.get("/runes/{champ_id}", response_model=List[schemas.Runes])
def get_build_by_champId(champ_id: str, db: Session = Depends(get_db)):
    return repository.get_runes_by_champId(db=db, id=champ_id)

@app.post("/suggestion/", response_model=List[schemas.Suggestion])
def get_champSuggestion(suggData: schemas.SuggestionInput, db: Session = Depends(get_db)):
    lineDict = {'TOP': 0, 'JGL': 1, 'MID': 2, 'ADC': 3, 'SUP': 4}
    print("AAAAAAAAAAAAAAAAA")
    print(suggData)

    anyPick = False
    for pick in suggData.picks:
        if pick != 0:
            anyPick = True

    if anyPick:
        blue_picks = suggData.picks[:5]
        red_picks = suggData.picks[5:]
        print(blue_picks, " || " ,red_picks)

        ally_team = blue_picks if suggData.player[0] == 'b' else red_picks
        enemy_team = blue_picks if suggData.player[0] != 'b' else red_picks

        print("ENTERING THE DUNGEOOON:", suggData.role, ally_team, enemy_team)
        dataSuggestion = repository.get_sugestions(db=db, role=suggData.role, ally_team=ally_team, enemy_team=enemy_team)

    else:
        dataSuggestion = repository.get_winrateOfLine(db, suggData.role, suggData.player[0])

    print(dataSuggestion)
    return dataSuggestion

@app.post("/team_data/", response_model=schemas.TeamData)
def get_teamData(teamData: schemas.TeamDataInput, db: Session = Depends(get_db)):
    AP = 0
    AD = 0
    TD = 0
    WR = 0
    cnt = 0
    for champ in teamData.picks:
        if champ != 0:
            enemy_champ = repository.get_champ_by_champId(db=db, champ_id=champ)

            cnt += 1
            AP += enemy_champ.AP
            AD += enemy_champ.AD
            TD += enemy_champ.TrueDamage

    if cnt != 0:
        AP = AP / cnt
        AD = AD / cnt
        TD = TD / cnt

    WR = repository.get_winrateOfTeam(db=db, team=teamData.picks)

    return {'AP': AP, 'AD': AD, 'TD': TD, 'WR': WR}