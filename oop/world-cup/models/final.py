from models import BaseModel

class Final(BaseModel):

    def __init__(self, groups=None):
        super().__init__(groups)
        self.stage_name = "Final"

    def build(self):
        if self.groups is None:
            return

        for group in self.groups:
           group[0].points = 0
           group[1].points = 0

           self.teams.append(group[0])
           self.teams.append(group[1])

        print('\n-------- Teams qualfied for Final -------')
        self.display()
        return self.teams

    def display(self):
        if self.teams == []:
            return
        for team in self.teams:
            print(team)
        print('---------------------------\n')

    def elimination_process(self):
        print("\n----- Final match result -----\n")
        self.teams[0].play(self.teams[1])
        self.teams = sorted(self.teams, reverse=True)

        print("\n------ The Winner of the World Cup is {0} --------".format(self.teams[0].country))