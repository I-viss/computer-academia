

class BaseModel:

    def __init__(self, groups=None):
        self.teams = []
        self.team_number = 32 
        self.groups = groups
        self.stage_name = ""

    def split(self):
        next = 4 
        prev = 0
        temp = []
        while next <= self.team_number:
            temp.append(self.teams[prev:next])
            prev = next
            next += 4

        return temp

    def build(self):
        if self.groups is None:
            return

        for group in self.groups:
           group.teams[0].points = 0
           group.teams[1].points = 0

           self.teams.append(group.teams[0])
           self.teams.append(group.teams[1])

        self.teams = self.split()
        print('\n-------- Teams qualfied for {0} -------'.format(self.stage_name))
        self.display()
        return self.teams

    def elimination_process(self):
        print("\n----- {0} stage Elimination process -----\n".format(self.stage_name))
        for teams in self.teams:
            teams[0].play(teams[2])
            teams[1].play(teams[3])   

        self.teams = self.sorting()
        print('\n----- Results of {0} Elimination stage'.format(self.stage_name))
        self.display()
        return self.teams

    def sorting(self):
        temp = []
        for team in self.teams:
            team = sorted(team, reverse=True)
            temp.append(team)

        return temp

    def display(self):
        if self.teams == []:
            return
        for teams in self.teams:
            for team in teams:
                print(team)
            print('---------------------------\n')


class ModelWithIdenticalBuildMethod(BaseModel):

    def __init__(self, groups):
        super().__init__(groups)


    def build(self):
        if self.groups is None:
            return

        for group in self.groups:
           group[0].points = 0
           group[1].points = 0

           self.teams.append(group[0])
           self.teams.append(group[1])

        self.teams = self.split()
        print('\n-------- Teams qualfied for {0} -------'.format(self.stage_name))
        self.display()
        return self.teams


