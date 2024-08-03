from typing import List
from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_BREEDS = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        pass

    def add_jockey(self, jockey_name: str, age: int):
        pass

    def create_horse_race(self, race_type: str):
        pass

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        pass

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        pass

    def start_horse_race(self, race_type: str):
        pass
