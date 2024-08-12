from project.movie_specification.movie import Movie


class Fantasy(Movie):
    DEFAULT_MIN_AGE: int = 6

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = DEFAULT_MIN_AGE):
        super().__init__(title, year, owner, age_restriction)

    @property
    def default_min_age(self):
        return self.DEFAULT_MIN_AGE
