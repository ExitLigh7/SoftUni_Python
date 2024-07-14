from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):

    def __init__(self, name: str) :
        super().__init__(name, 200)

    def can_climb(self) :
        if self.strength >= 100:
            return True

    def climb(self, peak: BasePeak):
        base_strength_reduction = 20

        if peak.difficulty_level == "Extreme":
            self.strength -= base_strength_reduction * 2
        else:
            self.strength -= base_strength_reduction * 1.5

        self.conquered_peaks.append(peak.name)



