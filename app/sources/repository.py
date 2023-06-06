from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.inspection import inspect
from sqlalchemy import select
from pprint import pprint
import models
import schemas


def get_champs(db: Session):
    return db.query(models.Champ).all()

def get_souls(db: Session):
    return db.query(models.Soul).all()

def get_passive_by_id(db: Session, id):
    return db.query(models.Passive).where(models.Passive.passive_id == id).first()

def get_build_by_champId(db: Session, id):
    return db.query(models.Build).where(models.Build.champ_id == id).all()

def get_runes_by_champId(db: Session, id):
    return db.query(models.Runes).where(models.Runes.champ_id == id).all()