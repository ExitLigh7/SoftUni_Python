from typing import List
from project.player import Player
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args: Player):
        added_players_names = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_players_names.append(player.name)
        return f"Successfully added: {', '.join(added_players_names)}"

    def add_supply(self, *args: Supply):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self._find_player_by_name(player_name)
        if player.stamina == player.MAX_STAMINA:
            return f"{player.name} have enough stamina."
        supply = self.__take_last_supply(sustenance_type)
        if supply:
            player._sustain_player(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_1 = self._find_player_by_name(first_player_name)
        player_2 = self._find_player_by_name(second_player_name)

        if player_1.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        if player_2.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if player_1 < player_2:
            return self.__attack(player_1, player_2)
        else:
            return self.__attack(player_2, player_1)

    def next_day(self):
        for player in self.players:
            decrease = (player.age * 2)
            if player.stamina - decrease < 0:
                player.stamina = 0
            else:
                player.stamina -= decrease

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        info = []
        for p in self.players:
            info.append(p.__str__())
        for s in self.supplies:
            info.append(s.details())
        result = "\n".join(info)
        return result

    # helper methods

    def _find_player_by_name(self, player_name: str):
        player = next((p for p in self.players if p.name == player_name), None)
        return player

    @staticmethod
    def __attack(p1, p2):
        p2.stamina -= (p1.stamina / 2)
        if p1.stamina - (p2.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= (p2.stamina / 2)
        if p1 < p2:
            return f"Winner: {p2.name}"
        else:
            return f"Winner: {p1.name}"

    def __take_last_supply(self, supply_type: str):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")
