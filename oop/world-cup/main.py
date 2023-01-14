import models 
import data
import random


def create_teams(teams_data):
    data = []
    for team in teams_data:
        new_team = models.Team(team)
        data.append(new_team)

    return data 

def split_teams(teams):
    next = 4 
    prev = 0
    temp = []
    while next < 32:
        temp.append(teams[prev:next])
        prev = next
        next += 4

    return temp 

def generate_groups(teams):
    groups = []
    names = ['A', 'F', 'K', 'B', 'R', 'T', 'H', 'L']
    for team_array in teams:
        name = random.choice(names)
        names.remove(name)
        group = models.Group(name)
        for team in team_array:
            group.add(team)
        groups.append(group)
                
    return groups
    

def match_simulation(group):
    temp = group.teams.copy()
    for team in group.teams:
        temp.remove(team)
        for t in temp:
            team.play(t)
        
    return group 


data = generate_groups(split_teams(create_teams(data.teams)))

for group in data:
    group.elimination_process()

for group in data:
    print(group)

