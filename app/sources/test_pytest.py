from fastapi.testclient import TestClient
import DateTime

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_python():
    response = client.get('/python')
    assert response.status_code == 200
    assert response.json() == ["I like Python!"]


#################################################################################################################
###########################################  TEAM TESTS  ########################################################
#################################################################################################################

def test_get_team():

    response = client.get("/teams/")
    assert response.status_code == 200
    assert response.json() == {"name": "Lleida", "country": "Espana", "description": None}
def test_post_team():
    team = {"name": "Lleida", "country": "Espana"}
    response = client.post("/teams/", json=team)
    assert response.status_code == 200
    assert response.json() == {"name": "Lleida", "country": "Espana", "description": None}


def test_delete_team():
    team = {"name": "DeleteTeam", "country": "DeleteCountry"}
    response = client.post("/teams/", json=team)
    assert response.status_code == 200
    assert response.json() == {"name": "DeleteTeam", "country": "DeleteCountry", "description": None}
    response2 = client.delete("/team/DeleteTeam")
    assert response2.status_code == 200
    assert response2.json() == {"deleted '" + team.get("name") + "'": True}


#################################################################################################################
########################################  COMPETITION TESTS  ####################################################
#################################################################################################################

def test_get_byname():
    response = client.get("/competitions/1st Division League")
    print(response)
    assert response.status_code == 200
    assert response.json() == {'Competition':{'id': 1,
     'name': "1st Division League",
     'category': 'Junior',
     'sport': 'Football',
     'teams': None}}

def test_get_byid():
    response = client.get("/competitions/1")

    assert response.status_code == 200
    assert response.json() == {'Competition':{'id': 1,
     'name': "1st Division League",
     'category': 'Junior',
     'sport': 'Football',
     'teams': None}}




def test_post_competition():
    comp = {'id': 99,
            'name': "LVP",
            'category': 'Senior',
            'sport': 'LeagueOfLegends',
            'teams': [{'name': "CV Vall D'Hebron",
                       'country': 'Spain'},
                      {'name': 'CE Sabadell',
                       'country': 'Spain'}]
            }
    response = client.post("/competitions/", json=comp)
    assert response.status_code == 200
    assert response.json() == {'id': 99,
                               'name': "LVP",
                               'category': 'Senior',
                               'sport': 'LeagueOfLegends',
                               'teams': [{'name': "CV Vall D'Hebron",
                                          'country': 'Spain',
                                          'description': None},
                                         {'name': 'CE Sabadell',
                                          'country': 'Spain',
                                          'description': None}]}

# ToDo implementar delete competition
def test_delete_competition():
    comp = {'id': -1,
            'name': "DeleteTest",
            'category': 'Senior',
            'sport': 'LeagueOfLegends',
            'teams': None}
    response = client.post("/competitions/", json=comp)
    assert response.status_code == 200
    assert response.json() == {'id': -1,
                               'name': "DeleteTest",
                               'category': 'Senior',
                               'sport': 'LeagueOfLegends',
                               'teams': None}
    response2 = client.delete("/competitions/DeleteTest")
    assert response2.status_code == 200
    assert response2.json() == {"deleted '" + comp.get("name") + "'": True}

# ToDo implementar put competition
def test_put_competition():
    comp = {'id': -1,
            'name': "DeleteTest",
            'category': 'Senior',
            'sport': 'LeagueOfLegends',
            'teams': None}
    response = client.post("/competitions/", json=comp)
    assert response.status_code == 200
    assert response.json() == {'id': -1,
                               'name': "DeleteTest",
                               'category': 'Senior',
                               'sport': 'LeagueOfLegends',
                               'teams': None}

    comp2 = {'id': 99,
             'name': "LVP",
             'category': 'Senior',
             'sport': 'LeagueOfLegends',
             'teams': None}
    response2 = client.put("/competitions/LVP", json=comp2)
    assert response2.status_code == 200
    assert response2.json() == {'ok': True}
