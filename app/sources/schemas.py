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


class Soul(BaseModel):
    soulDrake_id: int
    name: str
    winrate: float
    passive: int

    class Config:
        orm_mode = True

class SoulPassive(Soul):
    passive_desc: str


class Passive(BaseModel):
    passive_id: int
    name: str
    description: str


class Build(BaseModel):
    champ_id: int
    line: str
    starter_1: int
    starter_2: int
    starter_3: int
    mythic_1: int
    mythic_2: int
    mythic_3: int
    boots_1: int
    boots_2: int
    legendary_1: int
    legendary_2: int
    legendary_3: int
    legendary_4: int
    trinket_1: int
    trinket_2: int


class Runes(BaseModel):
    champ_id: int
    opt: int
    line: str
    main_perk_style_id: int
    second_perk_style_id: int
    main_perk_id_1: int
    main_perk_id_2: int
    main_perk_id_3: int
    main_perk_id_4: int
    second_perk_id_1: int
    second_perk_id_2: int
    last_perk_id_1: int
    last_perk_id_2: int
    last_perk_id_3: int
    summ_spell_id_1: int
    summ_spell_id_2: int

    class Config:
        orm_mode = True


class Perk(BaseModel):
    perk_id: int
    name: str
    shortDesc: str
    longDesc: str
    recommendationDesc: str


class PerkStyle(BaseModel):
    style_id: int
    name: str
    tooltip: str

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