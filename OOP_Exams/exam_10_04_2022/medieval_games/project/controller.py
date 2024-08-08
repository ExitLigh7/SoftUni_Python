from typing import List
from project.player import Player
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args: Player):
        pass

    def add_supply(self, *args: Supply):
        pass

    def sustain(self, player_name: str, sustenance_type: str):
        pass

    def duel(self, first_player_name: str, second_player_name: str):
        pass

    def next_day(self):
        pass

    def __str__(self):
        pass
