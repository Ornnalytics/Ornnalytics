import enum

from sqlalchemy import Boolean, MetaData, Column, ForeignKey, Integer, String, Date, Float, Enum, UniqueConstraint, \
    Table, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Champ(Base):
    __tablename__ = 'champ'

    champ_id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    type = Column(String(45), nullable=False)
    main_role = Column(String(3), nullable=True)
    secondary_role = Column(String(3), nullable=False)
    timeline_results = Column(String(6), nullable=False)



'''
# categories_list = ['Juvenil','Pro']
# sports_list = ['Lol','Minecraft']
categories_list = ("Pro", "Junior")
sports_list = ("Lol", "Football")
# categories_enum=Enum(*categories_list)
# print(categories_enum)
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
    


CategoryType: Enum = Enum(
    Category_Enum,
    name="post_category_type",
    create_constraint=True,
    metadata=Base.metadata,
    validate_strings=True,
)


class Team(Base):
    __tablename__ = 'teams'  # This is table name

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False, index=True)
    country = Column(String(30), nullable=False)
    description = Column(String(100))


class Match(Base):
    __tablename__ = 'matches'  # This is table name
    __table_args__ = (UniqueConstraint('local_id', 'visitor_id', 'competition_id', 'date'),)

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
    __table_args__ = (UniqueConstraint('name', 'category', 'sport'),)

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    category = Column(Enum(Category_Enum), nullable=False)
    sport = Column(Enum(Sports_Enum), nullable=False)

    teams = relationship(Team, secondary=teams_in_competitions, backref="competitions")
'''


