import data
from models.group import GroupGenerator 
from models.team import Team
from models.sFinal import sFinal
from models.qFinal import qFinal
from models.final import Final
from models.round16 import Round16

def create_teams(teams_data):
    data = []
    for team in teams_data:
        new_team = Team(team)
        data.append(new_team)

    return data 


generator = GroupGenerator(create_teams(data.teams))
data = generator.generate()


for group in data:
    group.elimination_process()

round16 = Round16(data)
round16.build()
round16.elimination_process()

qfinal = qFinal(round16.teams)
qfinal.build()
qfinal.elimination_process()

sfinal = sFinal(qfinal.teams)
sfinal.build()
sfinal.elimination_process()

final = Final(sfinal.teams)
final.build()
final.elimination_process()

