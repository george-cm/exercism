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
        self._allergic_to = [allergen for i, allergen in enumerate(Allergies.allergens) if score & (1 << i)]       

    def allergic_to(self, item):
        return item in self._allergic_to

    @property
    def lst(self):
        return self._allergic_to
