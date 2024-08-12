from typing import Set
from project.band_members.musician import Musician


class Guitarist(Musician):

    @property
    def available_skills(self) -> Set[str]:
        return {"play metal", "play rock", "play jazz"}
