import data
from models.group import GroupGenerator 
from models.team import AutomatedPlayingTeam, ManualPlayingTeam
from models.worlcup import WorlCupModel

def create_automated_teams(teams_data):
    data = []
    for team in teams_data:
        new_team = AutomatedPlayingTeam(team)
        data.append(new_team)

    return data 

def create_manual_teams(teams_data):
    data = []
    for team in teams_data:
        new_team = ManualPlayingTeam(team)
        data.append(new_team)

    return data 

if __name__ == "__main__":

    print("Welcome to World Cup\n1.Manual World Cup\n2.Automated World Cup\n0.To exit the program")
    res = int(input('Enter your choice: '))

    if res == 1:
        generator = GroupGenerator(create_manual_teams(data.teams))
        groups = generator.generate()
        world_cup = WorlCupModel(groups)
        world_cup.play()

    elif res == 2:
        generator = GroupGenerator(create_automated_teams(data.teams))
        groups = generator.generate()
        world_cup = WorlCupModel(groups)
        world_cup.play()

    else:
        exit()
