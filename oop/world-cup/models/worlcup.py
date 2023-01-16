from abc import abstractclassmethod, ABC
from models.team import AutomatedPlayingTeam, ManualPlayingTeam
from models.group import GroupGenerator 
from models.sFinal import sFinal
from models.qFinal import qFinal
from models.final import Final
from models.round16 import Round16

class WorlCupModel:
    def __init__(self, groups):
        self.round16 = Round16()
        self.qfinal = qFinal()
        self.sfinal = sFinal()
        self.final = Final()
        self.teams = []
        self.groups = groups


    def play(self):
        for group in self.groups:
            group.elimination_process()

        round16 = Round16(self.groups)
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
        