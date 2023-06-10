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


def get_winrateOfLine(db: Session, line, side, elo='GLOBAL'):
    statement = select(models.Winrate.champ_id,
                       getattr(models.Winrate, 'winrate_' + line.lower() + '_' + side.lower())).where(
        models.Winrate.elo_id == elo)

    db_data = db.execute(statement).all()
    champs = get_champs(db)

    data = []
    for var in db_data:
        if var[1]:
            varChamp = ''
            for champ in champs:
                if champ.champ_id == var[0]:
                    varChamp = champ
            ponderation = var[1] * 1 if varChamp.main_role.upper() == line.upper() else var[
                                                                                            1] * 1 if varChamp.secondary_role and varChamp.secondary_role.upper() == line.upper() else \
            var[1] * 0.5
            data.append({'champ_id': var[0], 'winrate': var[1], 'ponderation': ponderation})

    print("pre",data)

    data.sort(key=lambda x: x['ponderation'])
    print("post",data[::-1])
    return data[::-1]


def get_winrateByLane(db: Session, champ_id, linea, elo_id = 'GLOBAL'):
    statement = select(getattr(models.Winrate, 'winrate_' + linea.lower())).where((models.Winrate.elo_id == elo_id) &
                                                                                 (models.Winrate.champ_id == champ_id))

    db_data = db.execute(statement).first()
    print()
    print(db_data)

    return db_data[0]


def get_champ_by_champId(db: Session, champ_id):
    return db.query(models.Champ).where(models.Champ.champ_id == champ_id).first()


def get_winrateAgainst(db: Session, champ_a_id, champ_b_id, line='GLOBAL', elo='GLOBAL'):
    champ_a = champ_a_id
    champ_b = champ_b_id
    if champ_a > champ_b:
        temp = champ_a
        champ_a = champ_b
        champ_b = temp

    print(champ_a, champ_b, line, elo)
    data = db.query(models.Winrate_Against).filter((models.Winrate_Against.champ_id == champ_a) &
                                                   (models.Winrate_Against.champ_against_id == champ_b) &
                                                   (models.Winrate_Against.line == line) &
                                                   (models.Winrate_Against.elo == elo)).first()

    print(data)

    return data

def get_winrateWith(db: Session, champ_a_id, champ_b_id, _line_a='GLOBAL', _line_b='GLOBAL', elo='GLOBAL'):
    champ_a = champ_a_id
    champ_b = champ_b_id
    line_a = _line_a
    line_b = _line_b
    if champ_a > champ_b:
        temp = champ_a
        champ_a = champ_b
        champ_b = temp
        temp = line_a
        line_a = line_b
        line_b = temp
    return db.query(models.Winrate_With).where((models.Winrate_With.champ_a_id == champ_a) &
                                               (models.Winrate_With.champ_b_id == champ_b) &
                                               (models.Winrate_With.line_a == line_a) &
                                               (models.Winrate_With.line_b == line_b) &
                                               (models.Winrate_With.elo_id == elo)).first()


def get_sugestions(db: Session, role, ally_team, enemy_team):
    lineDict = {'TOP': 0, 'JGL': 1, 'MID': 2, 'ADC': 3, 'SUP': 4}

    # Para mantener una estructura de la info, no se que datos estan en base de datos la verdad (creoq ue esta actualizado) los que faltan se calculan
    class Champion:
        def __init__(self, id, name, type, primary_role, secundary_role, timeline, difficulty, engage, disengage, AP,
                     AD, TrueDamage):
            self.id = id
            self.name = name
            find = type.find('_')
            if find != -1:
                self.type = [type[:find], type[find + 1:]]
            else:
                self.type = [type]

            self.type = [type[:type.find('_')]]
            self.primary_role = primary_role
            self.secundary_role = secundary_role
            self.timeline = timeline
            self.difficulty = difficulty
            self.engage = engage
            self.disengage = disengage
            self.AP = AP
            self.AD = AD
            self.TrueDamage = TrueDamage
            self.wr_against_team = 0
            self.wr_against_lane = 0
            self.wr_with = 0
            self.wr_lane = 0
            self.damage_contribution = 0

    '''
    Calcula la media de winrates against entre el 'champ_id' y cada uno de los champs enemigos de 'enemy_team'.

    Return: media de los winrates against entre el 'champ_id' y cada uno de los champs en 'enemy_team' 
    '''
    # Winrate del champ contra el equipo enemigo
    def team_wr_against_team(champ_id, enemy_team):
        print("\n\nCalculando winrate against Team", champ_id, enemy_team)
        total_wr = 0
        enemy_count = 0
        enemy_i = 0

        print("Enemy team:", enemy_team)
        for enemy in enemy_team:
            print("Enemy:", enemy)
            print(enemy)
            if enemy > 0:
                if role == list(lineDict.keys())[enemy_i]:
                    data = get_winrateAgainst(db=db, champ_a_id=champ_id, champ_b_id=enemy, line=list(lineDict.keys())[enemy_i])
                else:
                    data = get_winrateAgainst(db=db, champ_a_id=champ_id, champ_b_id=enemy)

                if data != None:
                    wr_enemy = data.winrate
                    total_wr += wr_enemy
                    enemy_count += 1
                    print("WR:", wr_enemy, "total_wr:", total_wr, "enemy_count:", enemy_count)
                else:
                    print("Winrate_against_team = None")

            enemy_i += 1

        result = 0
        if enemy_count > 0:
            result = total_wr / enemy_count
            print("Return:", total_wr / enemy_count, "\n\n")

        return result


    '''
    Calcula el winrate de el aliado 'champ_id' contra el champ enemigo de la misma linea ('role') del 'enemy_team'
    en caso que el enemigo este pickeado (!= 0)

    Return: winrate against del 'champ_id' contra el mismo champ enemigo de la linea.
    '''
    def team_wr_against(champ_id, enemy_team, role):
        print("\n\nCalculando winrate against champ", champ_id, enemy_team, role)

        wr_enemy = 0

        if (enemy_team[lineDict[role]] != 0):
            print("Champ exists:", enemy_team[lineDict[role]])
            enemy_champ = get_champ_by_champId(db=db, champ_id=enemy_team[lineDict[role]])

            if role == enemy_champ.main_role or role == enemy_champ.secondary_role:
                data = get_winrateAgainst(db=db, champ_a_id=champ_id, champ_b_id=enemy_champ.champ_id,
                                          line=role)
            else:
                data = get_winrateAgainst(db=db, champ_a_id=champ_id, champ_b_id=enemy_champ.champ_id)

            if data == None:
                print("Winrate_against_lane = None")
                return 0
            wr_enemy = data.winrate

        print("Return wr_enemy:", wr_enemy)
        return wr_enemy


    '''
    Calcula el winrate de el aliado 'champ_id' a partir de los champs en 'ally_team', usa el parametro 'role' para,
    junto a el muiltiplicador 'ally_multiplier', valorar de manera distinta si estas en la botlane.

    Return: media de winrates de todas las combinaciones de winrate_with(champ_id, ally_champ_id),
    siendo ally_champ_id cada uno de los champs en ally_team distintos a 0 (A.K.A.: pickeados)
    '''
    def team_wr_with(champ_id, ally_team, role, ally_multiplier=1):
        print("\n\nCalculando winrate with", champ_id, ally_team, role, ally_multiplier)
        total_wr = 0
        ally_count = 0

        print("For each ally")
        for ally in ally_team:
            print("Ally:", ally)
            position = ally_team.index(ally)
            print("Position:")
            if ally > 0:
                data = get_winrateWith(db=db, champ_a_id=champ_id, champ_b_id=ally, _line_a=role,
                                       _line_b=list(lineDict.keys())[position])
                if data == None:
                    data = get_winrateWith(db=db, champ_a_id=champ_id, champ_b_id=ally)
                if data != None:
                    wr_ally = data.winrate
                    print(wr_ally)
                    if position == 4 or position == 5 and role in ["ADC", "SUP"]:  # si es combo de adc y suport
                        total_wr += wr_ally * ally_multiplier
                        ally_count += 1
                    else:
                        total_wr += wr_ally
                        ally_count += 1
                else:
                    print("Winrate_with = None")

        result = 0
        if ally_count > 0:
            result = total_wr / ally_count

        return result


    # Winrate del champ en la linea
    def team_wr_lane(champ_id, role):
        print("\n\n\nCalculando winrate lane")
        wr_lane = get_winrateByLane(db=db, champ_id=champ_id, linea=role)
        return wr_lane


    # Daño que aporta el champ al equipo
    def get_damage_contribution2(champ, ally_team):
        print("\n\n\nGetting damage contribution")

        damage_contribution = {'AD': 0, 'AP': 0, 'TD': 0}
        count = 1

        print("Para cada ally en", ally_team)
        for ally in ally_team:
            print("Ally:", ally)
            if ally > 0:
                ally_champ = get_champ_by_champId(db=db, champ_id=ally)
                if 'support' == ally_champ.type[0] or (
                        'tank' == ally_champ.type[0] and 'support' == ally_champ.type[1]):
                    count += 0.5
                else:
                    count += 1
                # ponemos los damages
                damage_contribution['AD'] += ally_champ.AD
                damage_contribution['AP'] += ally_champ.AP
                damage_contribution['TD'] += ally_champ.TrueDamage
                print("DamageContribution:", damage_contribution)

        damage_contribution['AD'] = (champ.AD + damage_contribution['AD']) / count
        damage_contribution['AP'] = (champ.AP + damage_contribution['AP']) / count
        damage_contribution['TD'] = (champ.TrueDamage + damage_contribution['TD']) / count

        if count > 2:
            return min(damage_contribution['AD'] / damage_contribution['AP'],
                       damage_contribution['AP'] / damage_contribution['AD'])
        else:
            return 0

        # Daño que aporta el champ al equipo


    def get_has_engage(champ, ally_team, engageMultiplier):
        print("\n\n\nGetting engage contribution")

        compo = {'engage': 0, 'disengage': 0}
        count = 0

        print("Para cada ally en", ally_team)
        for ally in ally_team:
            print("Ally:", ally)
            if ally > 0:
                ally_champ = get_champ_by_champId(db=db, champ_id=ally)
                count += 1
                # ponemos los damages
                compo['engage'] += ally_champ.engage
                compo['disengage'] += ally_champ.disengage

        result = 0
        if compo['engage'] > 0:
            result += engageMultiplier
        if compo['disengage'] > 0:
            result += engageMultiplier

        if count < 2:
            return 0
        return result


    def get_timestamp(champ_id, timeStampMultiplier):
        print("\n\n\nGetting timestamp contribution")
        ally_champ = get_champ_by_champId(db=db, champ_id=champ_id)

        result = timeStampMultiplier[0]
        result += int(champ.timeline[3]) * timeStampMultiplier[1]
        result += int(champ.timeline[5]) * timeStampMultiplier[2]
        print("\nTimestamp contribution", result)
        return result


    def get_dificulty(champ_id, difficultyMultiplier):
        print("\n\n\nGetting dificulty contribution")
        ally_champ = get_champ_by_champId(db=db, champ_id=champ_id)
        if champ.difficulty == 0:
            return difficultyMultiplier[0]
        if champ.difficulty == 1:
            return difficultyMultiplier[1]

        return difficultyMultiplier[2]


    def get_needs_tank(champ, ally_team, role, tankMultiplier):
        print("\n\n\nGetting if needs a tank contribution")

        if role == "ADC" or 'tank' not in champ.type and 'fighter' not in champ.type:
            if champ.id == 67 or champ.id == 96 or champ.id == 110:
                tanks = 0
                for enemy in enemy_team:
                    if enemy > 0:
                        enemy_champ = get_champ_by_champId(db=db, champ_id=enemy)
                        if 'tank' in enemy_champ.type:
                            tanks += 1
                        elif 'fighter' in enemy_champ.type:
                            tanks += 0.5

                return 0.03 * tanks

            else:
                return 0

        count = 0
        tanks = 0
        print("Para cada ally en", ally_team)
        for ally in ally_team:
            print("Ally:", ally)
            if ally > 0:
                count += 1
                ally_champ = get_champ_by_champId(db=db, champ_id=ally)
                # ponemos los damages
                if 'tank' in ally_champ.type:
                    tanks += 1
                if 'fighter' in ally_champ.type:
                    tanks += 0.5

        if count < 2:
            return 0
        if tanks < 1:
            if 'tank' in champ.type:
                return tankMultiplier[0]
            if 'fighter' in champ.type:
                return tankMultiplier[1]
        return tankMultiplier[2]


    # Obtenemos los champs que tengan el role en primaria o secundaria
    possible_champs = []
    temp = db.query(models.Champ).filter((models.Champ.main_role == role) | (models.Champ.secondary_role == role)).all()
    for champ in temp:
        if champ.champ_id in ally_team or champ.champ_id in enemy_team:
            continue
        possible_champs.append(
            Champion(champ.champ_id, champ.name, champ.type, champ.main_role, champ.secondary_role,
                     champ.timeline_results, champ.difficulty_level, champ.engage, champ.disengage,
                     champ.AP, champ.AD, champ.TrueDamage))
    print(len(possible_champs), possible_champs)

    # Calculamos datos para la recomendación
    for champ in possible_champs:
        champ.wr_lane = team_wr_lane(champ_id=champ.id, role=role)
        champ.wr_with = team_wr_with(champ_id=champ.id, ally_team=ally_team, role=role)
        champ.wr_against_team = team_wr_against_team(champ_id=champ.id, enemy_team=enemy_team)
        champ.wr_against_lane = team_wr_against(champ_id=champ.id, enemy_team=enemy_team, role=role)
        champ.damage_contribution = get_damage_contribution2(champ, ally_team)


    # Multiplicadores de oscar que algunos sirven no se la verdad yo los he puesto
    HAS_TANK = [0.1, 0.05, 0]  # [hay 0 tanks, hay algun fighter, hay tank]
    EQUILIBRATED_DMG = 0.5  # Proporcional al equilibrio, optimo 50/50
    TIMESTAMP = [0, 0.015, 0.04]  # [early, mid, late] || Quan importante es cada timestamp
    DIFFICULTY = [0.1, 0.05, 0]  # [eazy, normal, dificil] campeon facil 0.1, campeon dificil 0
    ENGAGE_DISENGAGE = 0.05  # si tiene engage O disengage


    champs_choosed = 0
    for enemy in enemy_team:
        if enemy > 0:
            champs_choosed += 1

    if champs_choosed <= 2:
        WIN = [3, 1, 1]

    if champs_choosed > 2 and champs_choosed < 5:
        WIN = [2, 2, 1]

    if champs_choosed == 5:
        WIN = [1, 3, 1]

    # Campeones sugeridos (id, valoracion)
    champs_suggested = []
    for champ in possible_champs:
        engage = get_has_engage(champ=champ.id, ally_team=ally_team, engageMultiplier=ENGAGE_DISENGAGE)
        timestamp = get_timestamp(champ_id=champ.id, timeStampMultiplier=TIMESTAMP)
        difficulty = get_dificulty(champ_id=champ.id, difficultyMultiplier=DIFFICULTY)
        tank = get_needs_tank(champ=champ, ally_team=ally_team, role=role, tankMultiplier=HAS_TANK)
        damage = champ.damage_contribution * EQUILIBRATED_DMG

        multiplier = engage + \
                     timestamp + \
                     difficulty + \
                     tank + \
                     damage
        print("Multiplier:", multiplier)
        print(champ.wr_against_lane, champ.wr_against_team, champ.wr_with, champ.wr_lane, champ.damage_contribution)

        if champ.wr_against_lane == 0 or champ.wr_against_lane == None:
            wr_total = (champ.wr_lane * WIN[0] + champ.wr_against_team * WIN[1] + champ.wr_with * WIN[2]) / 5
            champ_value = (wr_total) * (multiplier + 1)

        else:
            wr_total = (champ.wr_against_lane * WIN[0] + champ.wr_against_team * WIN[1] + champ.wr_with * WIN[2]) / 5
            champ_value = (wr_total) * (multiplier + 1)

        champs_suggested.append({'champ_id': champ.id,
                                 'winrate': champ.wr_lane,
                                 'wr_ag_lane': champ.wr_against_lane,
                                 'wr_ag_team': champ.wr_against_team,
                                 'wr_with': champ.wr_with,
                                 'wr_total': wr_total,
                                 'engage': engage,
                                 'timemod': timestamp,
                                 'difficulty': difficulty,
                                 'tank': tank,
                                 'damage': damage,
                                 'multiplier': multiplier,
                                 'ponderation': champ_value})

    champs_suggested.sort(key=lambda x: x['ponderation'])
    return champs_suggested[::-1]

def get_winrateOfTeam(db: Session, team):
    print("\n\n\nTotal winrate")
    count = 0
    winrate = 0
    lineDict = {'TOP': 0, 'JGL': 1, 'MID': 2, 'ADC': 3, 'SUP': 4}
    champ_i = 0

    for champ_id in team:
        if champ_id > 0:
            role = list(lineDict.keys())[champ_i]

            champ = get_champ_by_champId(db=db, champ_id=champ_id)
            count += 1
            # ponemos los damages
            if champ.main_role == role or champ.secondary_role == role:
                winrate += get_winrateByLane(db=db, champ_id=champ_id, linea=role)
            else:
                winrate += get_winrateByLane(db=db, champ_id=champ_id, linea='GLOBAL')

        champ_i += 1

    return winrate / count