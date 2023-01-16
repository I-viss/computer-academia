from random import randrange
from abc import ABC, abstractclassmethod

class AbstractModel(ABC):

    def __init__(self, country):
        self.points = 0
        self.country = country

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

    @abstractclassmethod
    def play(self, team):
        pass 

class ManualPlayingTeam(AbstractModel):

    def __ini__(self, name):
        super().__init__(name)

    def play(self, team):
       print('{0} vs {1}'.format(self.country, team.country))
       first_team_score = int(input('Enter {0} score: '.format(self.country)))
       second_team_score =int(input('Enter {0} score: '.format(team.country)))
       if first_team_score < second_team_score:
            team.win()
       elif second_team_score < first_team_score:
            self.win()
       else:
            self.draw()
            team.draw()
       print("{0} {1} --- {2} {3}\n".format(self.country,
                                        first_team_score, team.country,
                                        second_team_score))

class AutomatedPlayingTeam(AbstractModel):

    def __ini__(self, name):
        super().__init__(name)

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
       print("{0} {1} --- {2} {3}\n".format(self.country,
                                        first_team_score, team.country,
                                        second_team_score))

