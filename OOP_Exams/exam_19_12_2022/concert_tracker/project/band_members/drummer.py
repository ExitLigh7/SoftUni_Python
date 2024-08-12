from typing import Set
from project.band_members.musician import Musician


class Drummer(Musician):

    @property
    def available_skills(self) -> Set[str]:
        return {"play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"}

