from typing import List
from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        try:
            equip_unit = self.VALID_EQUIPMENT_TYPES[equipment_type]()
        except KeyError:
            raise Exception("Invalid equipment type!")

        self.equipment.append(equip_unit)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        try:
            team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        except KeyError:
            raise Exception("Invalid team type!")

        if self.capacity > len(self.teams):
            self.teams.append(team)
            return f"{team_type} was successfully added."
        else:
            return "Not enough tournament capacity."

    def sell_equipment(self, equipment_type: str, team_name: str):
        reversed_equipment_list = self.equipment[::-1]
        team = next(filter(lambda t: t.name == team_name, self.teams))
        equip_unit = next(filter(lambda eq: eq.TYPE_ == equipment_type, reversed_equipment_list))

        if team.budget < equip_unit.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equip_unit)
        team.equipment.append(equip_unit)
        team.budget -= equip_unit.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0
        for eq in self.equipment:
            if eq.TYPE_ == equipment_type:
                eq.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = next(filter(lambda t: t.name == team_name1, self.teams))
        team_2 = next(filter(lambda t: t.name == team_name2, self.teams))

        if not team_1.__class__.__name__ == team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        protection_team_1 = sum(eq.protection for eq in team_1.equipment)
        total_pts_team1 = team_1.advantage + protection_team_1

        protection_team_2 = sum(eq.protection for eq in team_2.equipment)
        total_pts_team2 = team_2.advantage + protection_team_2

        points_to_team = {
            total_pts_team1: team_1,
            total_pts_team2: team_2
        }

        if total_pts_team1 == total_pts_team2:
            return "No winner in this game."

        max_points = max(total_pts_team1, total_pts_team2)
        winner = points_to_team[max_points]
        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: (-t.wins))
        teams_statistics = "\n".join(t.get_statistics() for t in sorted_teams)
        result = (f"Tournament: {self.name}\n"
                  f"Number of Teams: {len(self.teams)}\n"
                  f"Teams:\n")
        result += teams_statistics
        return result
