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

    class Config:
        orm_mode = True


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

class SuggestionInput(BaseModel):
    picks: List[int]
    player: str
    role: str
    timeline: str

class Suggestion(BaseModel):
    champ_id: int
    winrate: float
    wr_ag_lane: Optional[float] = 0
    wr_ag_team: Optional[float] = 0
    wr_with: Optional[float] = 0
    wr_total: Optional[float] = 0
    engage: Optional[float] = 0
    timemod: Optional[float] = 0
    difficulty: Optional[float] = 0
    tank: Optional[float] = 0
    damage: Optional[float] = 0
    multiplier: Optional[float] = 0
    ponderation: float

    class Config:
        orm_mode = True

class TeamDataInput(BaseModel):
    picks: List[int]

class TeamData(BaseModel):
    AP: float
    AD: float
    TD: float

class WholeWinrate(BaseModel):
    r_WR: float
    b_WR: float

class WholeWinrateInput(BaseModel):
    r_picks: List[int]
    b_picks: List[int]


class AbilitySet(BaseModel):
    champ_id: int
    ability_order: str
    q_key: int
    w_key: int
    e_key: int
    r_key: int
    passive_id: int

    class Config:
        orm_mode = True
