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

'''
##########################################
############ Acciones TEAMS ##############
##########################################
@app.get("/teams/", response_model=List[schemas.Team])          # it works
def read_teams(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return repository.get_teams(db, skip=skip, limit=limit)


@app.post("/team/", response_model=schemas.Team)                # it works
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    db_team = repository.get_team_by_name(db, name=team.name)
    if db_team:
        raise HTTPException(status_code=400, detail="Team already Exists, Use put for updating")
    else:
        return repository.create_team(db=db, team=team)


@app.get("/team/{team_name}", response_model=schemas.Team)      # it works
def read_team(team_name: str, db: Session = Depends(get_db)):
    team = repository.get_team_by_name(db, name=team_name)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@app.put("/team/{team_name:str}", response_model=schemas.Team)                     # it works
def update_competition(team_name: str, team: schemas.TeamCreate, db: Session = Depends(get_db)):
    db_team = repository.get_team_by_name(db, name=team_name)

    if not db_team:
        raise HTTPException(status_code=404, detail="Team not found")

    resp = repository.update_team(db=db, old_name=team_name, team=team)

    return resp


@app.delete("/team/{team_name:str}")    # it works
def delete_team(team_name: str, db: Session = Depends(get_db)):
    team = repository.get_team_by_name(db, name=team_name)

    if not team:
        raise HTTPException(status_code=404, detail="Team not found")

    repository.delete_team(db, team=team)
    return {"ok": True}


##########################################
######## Acciones COMPETITIONS ###########
##########################################
@app.get("/competitions/", response_model=List[schemas.Competition])            # it works
def read_competition(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    resp = repository.get_competitions(db, skip=skip, limit=limit)

    for x in resp:
        x.sport = x.sport.value
        x.category = x.category.value

    return resp


@app.get("/competition/{comp_id:int}", response_model=schemas.Competition)      # it works
def read_comp(comp_id: int, db: Session = Depends(get_db)):
    comp = repository.get_competition(db, competition_id=comp_id)
    if not comp:
        raise HTTPException(status_code=404, detail="Competition not found")

    comp.sport = comp.sport.value
    comp.category = comp.category.value
    return comp


@app.get("/competition/{comp_name:str}", response_model=schemas.Competition)    # it works
def read_comp(comp_name: str, db: Session = Depends(get_db)):
    comp = repository.get_competition_by_name(db, name=comp_name)
    if not comp:
        raise HTTPException(status_code=404, detail="Competition not found")
    comp.sport = comp.sport.value
    comp.category = comp.category.value
    return comp


@app.post("/competition/", response_model=schemas.Competition)      # it works
def create_team(competition: schemas.CompetitionCreate, db: Session = Depends(get_db)):

    db_competition = repository.get_competition_by_name(db, name=competition.name)

    if db_competition:
        raise HTTPException(status_code=400, detail="Competition already Exists, Use put for updating")

    teams = list()
    for team in competition.teams:
        db_team = repository.get_team_by_name(db=db, name=team["name"])
        if db_team:
            teams.append(db_team)
        else:
            if "name" not in team or "country" not in team:
                raise HTTPException(status_code=400, detail="Team is not defined correctly, name and country must be defined")
            schemas.TeamCreate.parse_obj(team)
            db_team = repository.create_team(db=db, team=schemas.TeamCreate.parse_obj(team))
            teams.append(db_team)

    resp = repository.create_competition(db=db, competition=competition, teams=teams)
    resp.sport = resp.sport.value
    resp.category = resp.category.value
    return resp


@app.delete("/competition/{competition_name:str}")                  # it works
def delete_competition(competition_name: str, db: Session = Depends(get_db)):
    comp = repository.get_competition_by_name(db, name=competition_name)
    if not comp:
        raise HTTPException(status_code=404, detail="Competition not found")

    resp = repository.delete_competition(db, competition=comp)
    return {"ok": True}


@app.put("/competition/{competition_name:str}")                     # it works
def update_competition(competition_name: str, competition: schemas.CompetitionCreate, db: Session = Depends(get_db)):
    db_competition = repository.get_competition_by_name(db, name=competition_name)
    print("Paso1")
    if not db_competition:
        print("NOT")
        raise HTTPException(status_code=404, detail="Competition not found")
    else:
        print("Paso2")
        resp = repository.update_competition(db=db, old_name=competition_name, competition=competition)
        print("Paso3")

        resp.sport = resp.sport.value
        resp.category = resp.category.value

        return {"updated": True}


##########################################
########### Acciones MATCHES #############
##########################################
@app.get("/matches/", response_model=List[schemas.Match])           # it works
def read_matches(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    print("SE HA LLAMADO A MACHES")
    print(repository.get_matches(db, skip=skip, limit=limit))
    return repository.get_matches(db, skip=skip, limit=limit)


@app.post("/match/", response_model=schemas.Match)                  # it works
def create_match(match: schemas.MatchCreate, db: Session = Depends(get_db)):

    #
    # matches = db.query(models.Match).all()
    # for x in matches:
    #     #No puede jugar un equipo a la misma hora dos matches
    #     if x.date == match.date and x.local_id == match.local_id:
    #         raise HTTPException(status_code=400, detail="Match already Exists, Use put for updating")
    # teams=repository.get_teams(db)
    # teams_id=set(x.id for x in teams)
    # print(teams_id)
    # print(match.local_id,match.visitor_id )
    # if match.local_id not in teams_id or match.visitor_id not in teams_id:
    #     print("MATCHES: el equipo no existe")
    #     raise HTTPException(status_code=404, detail="Team not found")
    #
    # competitions=repository.get_competitions(db)
    # competitions_id=set(x.id for x in competitions)
    # if match.competition_id not in competitions_id:
    #     raise HTTPException(status_code=404, detail="Competition not found")
    # print("No duplicado")
    try:
        ret=repository.create_match(db=db, match=match)
    except Exception as ex:
        print(type(ex).__name__)
        print(ex)
        print("ERROR")
        raise HTTPException(status_code=404, detail="Couldnt ")
    return ret


@app.get("/match/{match_id:int}", response_model=schemas.Match)     # it works
def read_match(match_id: int, db: Session = Depends(get_db)):
    match = repository.get_match_by_id(db, match_id=match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match


@app.put("/match/{match_id:int}", response_model=schemas.Match)     # it works
def update_match(match_id: int, match: schemas.MatchCreate, db: Session = Depends(get_db)):
    db_match = repository.get_match_by_id(db, match_id=match_id)
    db_local = repository.get_team(db=db, team_id=match.local_id)
    db_visitor = repository.get_team(db=db, team_id=match.visitor_id)
    db_competition = repository.get_competition(db=db, competition_id=match.competition_id)

    if not db_match:
        raise HTTPException(status_code=404, detail="Competition not found")
    if not db_local:
        raise HTTPException(status_code=404, detail="Local team not found")
    if not db_visitor:
        raise HTTPException(status_code=404, detail="Visitor team not found")
    if not db_competition:
        raise HTTPException(status_code=404, detail="Competition not found")

    resp = repository.update_match(db=db, match_id=match_id, match=match)

    return resp


@app.delete("/match/{match_id:int}")    # it works
def delete_match(match_id: int, db: Session = Depends(get_db)):
    match = repository.get_match_by_id(db, match_id=match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Team not found")
    repository.delete_match(db, match=match)
    return {"ok": True}



###############################################
########### Acciones RELACIONALES #############
###############################################
# GET /teams/{team_name}/matches: retorna tots els partits d'un equip, donat el seu nom.
@app.get("/teams/{team_name}/matches", response_model=List[schemas.Match])  # it works
def read_matches_from_team_name(team_name: str, db: Session = Depends(get_db), skip: int = 1, limit: int = 10, ):
    resp = repository.get_matches_from_team(db, team_name, skip=skip, limit=limit)

    return resp


# GET /teams/{team_name}/competitions: retorna totes les competicions d'un equip, donat el seu nom.
@app.get("/teams/{team_name}/competitions", response_model=List[schemas.Competition])  # it works
def read_competition_from_team_name(team_name: str, db: Session = Depends(get_db), skip: int = 1, limit: int = 10, ):
    resp = repository.get_competitions_from_team(db, team_name, skip=skip, limit=limit)

    return resp


# GET /competitions/{competition_name}/matches: retorna tots els partits d'una competició, donada el seu nom.
@app.get("/competitions/{competition_name}/matches", response_model=List[schemas.Match])  # it works
def read_matches_from_competition_name(competition_name: str, db: Session = Depends(get_db), skip: int = 1,
                                       limit: int = 10, ):
    resp = repository.get_matches_from_competition(db, competition_name, skip=skip, limit=limit)

    return resp


# GET /competitions/{competition_name}/teams retorna tots els equips d'una competició, donada el seu nom.
@app.get("/competitions/{competition_name}/teams", response_model=List[schemas.Team])  # it works
def read_teams_from_competition_name(competition_name: str, db: Session = Depends(get_db), skip: int = 1,
                                     limit: int = 10, ):
    resp = repository.get_teams_from_competition(db, competition_name, skip=skip, limit=limit)
    return list(resp)


# GET /matches/{match_id}/teams retorna l'equip local i visitant d'un partit, donat el seu id.
@app.get("/matches/{match_id}/teams", response_model=List[schemas.Team])
def read_teams_from_match_id(match_id: int, db: Session = Depends(get_db), skip: int = 1,
                                     limit: int = 10, ):
    match = repository.get_match_by_id(db=db, match_id=match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match id does not exists in our database")
    resp = repository.get_teams_from_match(db, match, skip=skip, limit=limit)
    return list(resp)


# GET /matches/{match_id}/competition retorna la competició d'un partit, donat el seu id.
@app.get("/matches/{match_id}/competition", response_model=schemas.Competition)
def read_teams_from_competition_name(match_id: int, db: Session = Depends(get_db), skip: int = 1,
                                     limit: int = 10, ):
    match = repository.get_match_by_id(db=db, match_id=match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match id does not exists in our database")
    resp = repository.get_competition_from_match(db, match, skip=skip, limit=limit)
    return resp

###############################################
########### Acciones RELACIONALES #############
###############################################
@app.post('/account', response_model=schemas.Account)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    try:
        ret=repository.create_account(db=db, account=account)
    except Exception as ex:
        print(type(ex).__name__)
        print(ex)
        print("ERROR")
        raise HTTPException(status_code=404, detail="Couldnt ")
    return ret

@app.get('/orders/{username}', response_model=schemas.Order)
def read_account(username: str, db: Session = Depends(get_db)):
    account = repository.get_acc_by_username(db=db, username=username)
    if not account:
        raise HTTPException(status_code=404, detail="Account username does not exists in our database")
    return account
@app.post('/orders/{username}', response_model=schemas.Order)
def create_order(username: str,order: schemas.OrderCreate, db: Session = Depends(get_db)):
    try:
        ret = repository.create_order(db=db, order=order,username=username)
    except Exception as ex:
        print(type(ex).__name__)
        print(ex)
        print("ERROR")
        raise HTTPException(status_code=404, detail="Couldnt ")
    return ret

@app.get('/orders', response_model=list[schemas.Order])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return repository.get_orders(db, skip=skip, limit=limit)
'''