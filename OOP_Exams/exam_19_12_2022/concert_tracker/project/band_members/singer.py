from typing import Set
from project.band_members.musician import Musician


class Singer(Musician):

    @property
    def available_skills(self) -> Set[str]:
        return {"sing high pitch notes", "sing low pitch notes"}
