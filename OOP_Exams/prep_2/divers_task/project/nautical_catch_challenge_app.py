from typing import List
from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {
        "FreeDiver" : FreeDiver,
        "ScubaDiver" : ScubaDiver,
    }
    VALID_FISH_TYPES = {
        "DeepSeaFish" : DeepSeaFish,
        "PredatoryFish" : PredatoryFish,
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        try:
            diver = self.VALID_DIVER_TYPES[diver_type](diver_name)
        except KeyError:
            return f"{diver_type} is not allowed in our competition."

        try:
            next(filter(lambda d: d.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."
        except StopIteration:
            self.divers.append(diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        try:
            fish = self.VALID_FISH_TYPES[fish_type](fish_name,points)
        except KeyError:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            next(filter(lambda f: f.name == fish_name, self.fish_list))
            return f"{fish_name} is already permitted."
        except StopIteration:
            self.fish_list.append(fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level == 0:
            diver.has_health_issue = True

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."

            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        else:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.renew_oxy()
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = next(filter(lambda d: d.name == diver_name, self.divers))

        fish_details = '\n'.join(f.fish_details () for f in diver.catch)
        return (f"**{diver_name} Catch Report**\n"
                f"{fish_details}")

    def competition_statistics(self):
        divers_in_good_health = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(divers_in_good_health, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        divers_details = '\n'.join(d.__str__() for d in sorted_divers)

        return (f"**Nautical Catch Challenge Statistics**\n"
                f"{divers_details}")
