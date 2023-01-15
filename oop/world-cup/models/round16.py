
class Round16:

    def __init__(self, groups=None):
        self.groups = groups
        self.teams = []

    def build(self):
        if self.groups is None:
            return

        for group in self.groups:
           group.teams[0].points = 0
           group.teams[1].points = 0

           self.teams.append(group.teams[0])
           self.teams.append(group.teams[1])

        self.teams = self.split()
        print('\n-------- Teams qualfied for round 16 -------')
        self.display()
        return self.teams

    def display(self):
        if self.teams == []:
            return
        for teams in self.teams:
            for team in teams:
                print(team)
            print('---------------------------\n')

    def split(self):
        next = 4 
        prev = 0
        temp = []
        while next <= 16:
            temp.append(self.teams[prev:next])
            prev = next
            next += 4

        return temp

    def elimination_process(self):
        print("\n----- Round 16 stage Elimination process -----\n")
        for teams in self.teams:
            teams[0].play(teams[2])
            teams[1].play(teams[3])   

        self.teams = self.sorting()
        print('\n----- Results of Round 16 Elimination stage')
        self.display()

    def sorting(self):
        temp = []
        for team in self.teams:
            team = sorted(team, reverse=True)
            temp.append(team)

        return temp