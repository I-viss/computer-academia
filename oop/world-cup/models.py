from random import randrange


class Team:
    def __init__(self, country):
        self.points = 0
        self.country = country
        self.match_tracker = []

    def win(self):
        self.points += 3

    def draw(self):
        self.points += 1

    def update_tracker(self, match_info):
        self.match_tracker.append(match_info)

    def __str__(self) -> str:
        return '{0} {1}'.format(self.country, self.points)

    def play(self, team):
       first_team_score = randrange(0, 7)
       second_team_score = randrange(0, 7)
       if first_team_score < second_team_score:
            team.win()
       elif second_team_score < first_team_score:
            self.win()
       else:
            self.draw()
            team.draw()



class Group:

    def __init__(self, name):
        self.name = name 
        self.teams = []

    def add(self, team:Team):
        if len(self.teams) <= 4:
            self.teams.append(team)

    def __str__(self):
        str = 'GROUP NAME: {0}\n'.format(self.name)
        for team in self.teams:
            str += '{0}\n'.format(team)
        return str

    def elimination_process(self):
        temp = self.teams.copy()
        for team in self.teams:
            temp.remove(team)
            for t in temp:
                team.play(t)
        
        return self.teams

    def results(self):
        "sort teams by points and take the first and second of the group"


class Round16:

    def __init__(self):
        self.result = []
        self.teams = []

    def add(self, team):
        self.teams.append(team)

class qFinal:

    def __init__(self):
        self.result = []
        self.teams = []

    def add(self, team):
        self.teams.append(team)

class sFinal:

    def __init__(self):
        self.result = []
        self.teams = []

    def add(self, team):
        self.teams.append(team)


class Final:

    def __init__(self):
        self.result = []
        self.teams = []

    def add(self, team):
        self.teams.append(team)
