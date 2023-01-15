from random import randrange

class Team:
    def __init__(self, country):
        self.points = 0
        self.country = country
        self.match_tracker = []

    def __lt__(self, obj):
        return ((self.points) < (obj.points))

    def __gt__(self, obj):
        return ((self.points) > (obj.points))

    def __le__(self, obj):
        return ((self.points) <= (obj.points))

    def __ge__(self, obj):
        return ((self.points) >= (obj.points))

    def __eq__(self, obj):
        return ((self.points) == (obj.points))

    def win(self):
        self.points += 3

    def draw(self):
        self.points += 1

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
       print("{0} {1} --- {2} {3}".format(self.country,
                                        first_team_score, team.country,
                                        second_team_score))