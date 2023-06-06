import enum

from sqlalchemy import Boolean, MetaData, Column, ForeignKey, Integer, String, Date, Float, Enum, UniqueConstraint, \
    Table, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.types import Text
from database import Base


class Champ(Base):
    __tablename__ = 'champ'

    champ_id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    type = Column(String(45), nullable=False)
    main_role = Column(String(3), nullable=True)
    secondary_role = Column(String(3), nullable=False)
    timeline_results = Column(String(6), nullable=False)


class Soul(Base):
    __tablename__ = 'soul_drake'

    soulDrake_id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    winrate = Column(Float, nullable=False)
    passive = Column(Integer, ForeignKey("passive.passive_id"), nullable=False)

    passive_rel = relationship("Passive", foreign_keys=passive, backref="soulPassive")



class Passive(Base):
    __tablename__ = 'passive'

    passive_id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    description = Column(Text, nullable=False)

class Build(Base):
    __tablename__ = 'recommend_build'

    champ_id = Column(Integer, primary_key=True)
    line = Column(String(3), nullable=False)
    starter_1 = Column(Integer, nullable=False)
    starter_2 = Column(Integer, nullable=False)
    starter_3 = Column(Integer, nullable=False)
    mythic_1 = Column(Integer, nullable=False)
    mythic_2 = Column(Integer, nullable=False)
    mythic_3 = Column(Integer, nullable=False)
    boots_1 = Column(Integer, nullable=False)
    boots_2 = Column(Integer, nullable=False)
    legendary_1 = Column(Integer, nullable=False)
    legendary_2 = Column(Integer, nullable=False)
    legendary_3 = Column(Integer, nullable=False)
    legendary_4 = Column(Integer, nullable=False)
    trinket_1 = Column(Integer, nullable=False)
    trinket_2 = Column(Integer, nullable=False)


class Runes(Base):
    __tablename__ = 'champ_configuration'

    champ_id = Column(Integer, primary_key=True)
    opt = Column(Integer, primary_key=True)
    line = Column(String(3), primary_key=True)
    main_perk_style_id = Column(Integer, nullable=False)
    second_perk_style_id = Column(Integer, nullable=False)
    main_perk_id_1 = Column(Integer, nullable=False)
    main_perk_id_2 = Column(Integer, nullable=False)
    main_perk_id_3 = Column(Integer, nullable=False)
    main_perk_id_4 = Column(Integer, nullable=False)
    second_perk_id_1 = Column(Integer, nullable=False)
    second_perk_id_2 = Column(Integer, nullable=False)
    last_perk_id_1 = Column(Integer, nullable=False)
    last_perk_id_2 = Column(Integer, nullable=False)
    last_perk_id_3 = Column(Integer, nullable=False)
    summ_spell_id_1 = Column(Integer, nullable=False)
    summ_spell_id_2 = Column(Integer, nullable=False)


class Perk(Base):
    __tablename__ = "perk"

    perk_id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    shortDesc = Column(Text, nullable=False)
    longDesc = Column(Text, nullable=False)
    recommendationDesc = Column(Text, nullable=False)


class PerkStyle(Base):
    __tablename__ = "perk_style"

    style_id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    tooltip = Column(String(45), nullable=False)

'''
# categories_list = ['Juvenil','Pro']
# sports_list = ['Lol','Minecraft']
categories_list = ("Pro", "Junior")
sports_list = ("Lol", "Football")
# categories_enum=Enum(*categories_list)
# prInteger(categories_enum)
"""
class sports_list(enum.Enum):
    Lol = "Lol"
    Football = "Football"
    CSGO = "CSGO"
"""


class Sports_Enum(enum.Enum):
    LOL = 'League of Legends'
    CSGO = 'Counter Strike'
    MINECRAFT = 'Minecraft'
    Futsal = 'Futsal'


class Category_Enum(enum.Enum):
    JUNIOR = 'Junior'
    PRO = 'Pro'
    AMATEUR = 'Amateur'
    




class Team(Base):
    __tablename__ = 'teams'  # This is table name

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False, index=True)
    country = Column(String(30), nullable=False)
    description = Column(String(100))


class Match(Base):
    __tablename__ = 'matches'  # This is table name
    __table_args__ = (UniqueConstraInteger('local_id', 'visitor_id', 'competition_id', 'date'),)

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    price = Column(Float, nullable=False)
    total_available_tickets = Column(Integer,nullable=False)
    competition_id = Column(Integer, ForeignKey("competitions.id"), nullable=False)
    competition = relationship("Competition", backref="matches")


    local_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    visitor_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    local = relationship("Team", foreign_keys=local_id, backref="localTeam")
    visitor = relationship("Team", foreign_keys=visitor_id, backref="visitorTeam")


teams_in_competitions = Table("teams_in_competitions", Base.metadata,
                              Column("id", Integer, primary_key=True),
                              Column("team_id", Integer, ForeignKey("teams.id")),
                              Column("competition_id", Integer, ForeignKey("competitions.id")))


class Competition(Base):
    __tablename__ = 'competitions'  # This is table name
    __table_args__ = (UniqueConstraInteger('name', 'category', 'sport'),)

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    category = Column(Enum(Category_Enum), nullable=False)
    sport = Column(Enum(Sports_Enum), nullable=False)

    teams = relationship(Team, secondary=teams_in_competitions, backref="competitions")
'''


