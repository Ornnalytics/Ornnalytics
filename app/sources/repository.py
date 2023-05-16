from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.inspection import inspect
from sqlalchemy import select

import models
import schemas



def TEST_CHAMP(db: Session):
    return db.query(models.Champ).first()


def TEST_CHAMPS(db: Session):
    return db.query(models.Champ).all()
'''
##########################################
############ Acciones TEAMS ##############
##########################################
def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()


def get_team_by_name(db: Session, name: str):
    return db.query(models.Team).filter(models.Team.name == name).first()


def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Team).offset(skip).limit(limit).all()


def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(name=team.name, country=team.country, description=team.description)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def delete_team(db: Session, team: schemas.TeamCreate):
    db.delete(team)
    matches = get_matches_from_team(db=db, team_name=team.name)
    for match in matches:
        db.delete(match)  # TODO REVISAR SI ES LO QUE REALMENTE QUEREMOS AAAAAAAAAAAA!!!!!!!!!!!!!
    db.commit()


# Suponemos que la id no se cambia
def update_team(db: Session, old_name: str, team: schemas.TeamCreate):
    res = db.query(models.Team).filter(models.Team.name == old_name).first()

    res.name = team.name
    res.country = team.country
    res.description = team.description

    db.commit()
    return res


##########################################
######## Acciones COMPETITIONS ###########
##########################################
def get_competition(db: Session, competition_id: int):
    return db.query(models.Competition).filter(models.Competition.id == competition_id).first()


def get_competition_by_name(db: Session, name: str):
    return db.query(models.Competition).filter(models.Competition.name == name).first()


def get_competitions(db: Session, skip: int = 1, limit: int = 100):
    qr = db.query(models.Competition)

    return qr.offset(skip).limit(limit).all()


def create_competition(db: Session, competition: schemas.CompetitionCreate, teams: List[models.Team]):
    print("Repository")
    db.query()
    db_competition = models.Competition(name=competition.name, category=competition.category.name,
                                        sport=competition.sport.name)

    db_competition.teams.extend(teams)

    db.add(db_competition)
    db.commit()
    db.refresh(db_competition)
    return db_competition


def delete_competition(db: Session, competition: schemas.CompetitionCreate):
    db.delete(competition)
    matches = get_matches_from_competition(db=db, competition_name=competition.name)
    for match in matches:
        db.delete(match)
    db.commit()


# Suponemos que la id no se cambia
def update_competition(db: Session, old_name: str, competition: schemas.CompetitionCreate):
    res = db.query(models.Competition).filter(models.Competition.name == old_name).first()

    res.name = competition.name
    res.sport = competition.sport.name
    res.category = competition.category.name

    db.commit()
    return res


##########################################
########### Acciones MATCHES #############
##########################################

def get_matches(db: Session, skip: int = 1, limit: int = 100):
    retquery = db.query(models.Match).offset(skip).limit(limit).all()
    return retquery


def get_match_by_id(db: Session, match_id: int):
    return db.query(models.Match).filter(models.Match.id == match_id).first()


def create_match(db: Session, match: schemas.MatchCreate):
    db_match = models.Match(date=match.date, price=match.price, local_id=match.local_id, visitor_id=match.visitor_id,
                            competition_id=match.competition_id,total_available_tickets=match.total_available_tickets)
    db_match.competition = get_competition(db=db, competition_id=match.competition_id)
    db_match.local = get_team(db=db, team_id=match.local_id)
    db_match.visitor = get_team(db=db, team_id=match.visitor_id)


    db.add(db_match)
    db.commit()
    db.refresh(db_match)

    return db_match


def delete_match(db: Session, match: schemas.MatchCreate):
    db.delete(match)
    db.commit()


# Suponemos que la id no se cambia
def update_match(db: Session, match_id: int, match: schemas.MatchCreate):
    res = db.query(models.Match).filter(models.Match.id == match_id).first()

    res.local_id = match.local_id
    res.local = get_team(db=db, team_id=match.local_id)
    res.visitor_id = match.visitor_id
    res.visitor = get_team(db=db, team_id=match.visitor_id)
    res.competition_id = match.competition_id
    res.competition = get_competition(db=db, competition_id=match.competition_id)
    res.date = match.date
    res.price = match.price

    db.commit()
    return res


#################################################
############ Acciones RELACIONALES ##############
#################################################

def get_matches_from_team(db: Session, team_name: str, skip: int = 1, limit: int = 2):
    data_local = db.query(models.Match).join(models.Match.local).filter(models.Team.name == team_name).all()
    data_visitor = db.query(models.Match).join(models.Match.visitor).filter(models.Team.name == team_name).all()
    data = data_local + data_visitor
    return list(data)[::skip][:limit]


def get_competitions_from_team(db: Session, team_name: str, skip: int = 1, limit: int = 100):
    team = get_team_by_name(db=db, name=team_name)
    db_data = db.query(models.teams_in_competitions).all()[:limit]
    data = []

    for val in db_data:
        if val[1] == team.id:
            comp = get_competition(db=db, competition_id=val[2])
            comp.sport = comp.sport.value
            comp.category = comp.category.value
            data.append(comp)
    return list(data)[::skip][:limit]


def get_matches_from_competition(db: Session, competition_name: str, skip: int = 1, limit: int = 100):
    # ir a matches i coger todos aquellos con la id de competition_name
    comp = get_competition_by_name(db=db, name=competition_name)
    data = db.query(models.Match).where(models.Match.competition_id == comp.id)

    return list(data)[::skip][:limit]


def get_teams_from_competition(db: Session, competition_name: str, skip: int = 1, limit: int = 100):
    comp = get_competition_by_name(db=db, name=competition_name)
    # inner join teams in competition con competitions por id; y coges aquellos teams que tengan el nombre
    statement = select(models.teams_in_competitions)
    # Limit aqui no tiene sentido, ya que limitas la query, no el resultado
    db_data = db.execute(statement).all()
    data = []

    for val in db_data:
        if val[2] == comp.id:
            team = get_team(db=db, team_id=val[1])
            data.append(team)
    print(skip)
    return data[::skip][:limit]


def get_teams_from_match(db: Session, match: schemas.Match, skip: int = 1, limit: int = 100):
    statement = select(models.Match.local_id, models.Match.visitor_id).where(models.Match.id == match.id)
    db_data = db.execute(statement).one()
    data = []
    for var in db_data:
        data.append(get_team(db=db, team_id=var))

    return data[::skip][:limit]


def get_competition_from_match(db: Session, match: schemas.Match, skip: int = 1, limit: int = 100):
    statement = select(models.Match.competition_id).where(models.Match.id == match.id)
    db_data = db.execute(statement).one()

    data = get_competition(db=db, competition_id=db_data[0])
    data.sport = data.sport.value
    data.category = data.category.value
    return data[::skip][:limit]


def get_orders_by_username(db, username):
    return db.query(models.Order).filter(models.Order.username == username)


def create_account(db, account):
    db_acc = models.Account(username=account.username,is_admin=account.is_admin,available_money=account.available_money)
    db_acc.orders= get_orders_by_username(db=db, username=account.username)
    db.add(db_acc)
    db.commit()
    db.refresh(db_acc)

    return db_acc


def create_order(db, order, username):
    db_order = models.Order(match_id=order.match_id,tickets_bought=order.tickets_bought)
    db_order.username=username


    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order


def get_acc_by_username(db, username):
    return db.query(models.Account).filter(models.Account.username == username).first()


def get_orders(db, skip, limit):
    return db.query(models.Order).offset(skip).limit(limit).all()
'''