import random



class Group:

    def __init__(self, name):
        self.name = name 
        self.teams = []

    def add(self, team):
        if len(self.teams) <= 4:
            self.teams.append(team)
    
    def __str__(self):
        str = ''
        for team in self.teams:
            str += '{0}\n'.format(team)
        return str

    def elimination_process(self):
        temp = self.teams.copy()
        print('------- Elimination 32 stage match results group -------{0}'.format(self.name))
        for team in self.teams:
            temp.remove(team)
            for t in temp:
                team.play(t)
        print('\n')

        return self.teams

    def results(self):
        self.teams = sorted(self.elimination_process(), reverse=True)
        print("---- results of group {0} after elimination 32 stage----".format(self.name))
        print(self)

class GroupGenerator:

    def __init__(self, teams):
        self.teams = teams 
        self.groups = []
        self.names = ['A', 'F', 'K', 'B', 'R', 'T', 'H', 'L']

    def generate(self):
        splitted = self.split()
        for team_array in splitted:
            name = random.choice(self.names)
            self.names.remove(name)
            group = Group(name)
            for team in team_array:
                group.add(team)
            self.groups.append(group)
                        
        return self.groups

    def split(self):
        next = 4 
        prev = 0
        temp = []
        while next <= 32:
            temp.append(self.teams[prev:next])
            prev = next
            next += 4

        return temp 