import enum
#from models import Sports_Enum, Category_Enum
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class Champ(BaseModel):
    champ_id: int
    name: str
    type: str
    main_role: str
    secondary_role: Optional[str]
    timeline_results: str

    class Config:
        orm_mode = True

class ChampWinrate(Champ):
    winrate_global: float

'''
class TeamBase(BaseModel):
    name: str
    country: str
    description: Optional[str] = None


class TeamCreate(TeamBase):
    pass


class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    username: str
    match_id: int
    tickets_bought: int


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True


class AccountBase(BaseModel):
    username: str
    password: str
    is_admin: int
    available_money: float


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id: int

    class Config:
        orm_mode = True



class CompetitionBase(BaseModel):
    name: str
    category: Category_Enum
    sport: Sports_Enum



class CompetitionCreate(CompetitionBase):
    teams: List[dict]
    pass


class Competition(CompetitionBase):
    id: int


    class Config:
        orm_mode = True


class MatchBase(BaseModel):
    date: datetime
    price: float
    total_available_tickets: int
    competition_id: int
    local_id: int
    visitor_id: int


class MatchCreate(MatchBase):
    pass


class Match(MatchBase):
    id: int
    local:Team
    visitor:Team


    class Config:
        orm_mode = True
'''