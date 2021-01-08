class Allergies(object):
    allergens = [
        'eggs',
        'peanuts',
        'shellfish',
        'strawberries',
        'tomatoes',
        'chocolate',
        'pollen',
        'cats'
    ]

    def __init__(self, score):
        self.score = score
        self._allergic_to = []
        for i, allergen in enumerate(Allergies.allergens):
            if bool(score & 2**i):
                self._allergic_to.append(allergen)

    def allergic_to(self, item):
        if item in self._allergic_to:
            return True
        return False

    @property
    def lst(self):
        return self._allergic_to
