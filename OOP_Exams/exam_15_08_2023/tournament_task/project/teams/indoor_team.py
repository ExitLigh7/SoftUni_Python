from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    ADVANTAGE_POINTS = 145
    INITIAL_BUDGET = 500.0

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.INITIAL_BUDGET)

    def win(self):
        self.advantage += self.ADVANTAGE_POINTS
        self.wins += 1