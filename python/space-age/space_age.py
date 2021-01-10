class SpaceAge:
    orbital_periods = {
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Earth": 1,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132,
    }

    seconds_in_an_Earth_year = 31557600

    def __init__(self, seconds):
        self.seconds = seconds

    def _age_on_planet(self, planet):
        return round(self.seconds / (SpaceAge.orbital_periods[planet] * SpaceAge.seconds_in_an_Earth_year), 2)

    def on_earth(self):
        return self._age_on_planet("Earth")

    def on_mercury(self):
        return self._age_on_planet("Mercury")

    def on_venus(self):
        return self._age_on_planet("Venus")

    def on_mars(self):
        return self._age_on_planet("Mars")

    def on_jupiter(self):
        return self._age_on_planet("Jupiter")

    def on_neptune(self):
        return self._age_on_planet("Neptune")

    def on_saturn(self):
        return self._age_on_planet("Saturn")

    def on_uranus(self):
        return self._age_on_planet("Uranus")
