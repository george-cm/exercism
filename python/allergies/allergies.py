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
        self.allergic_to = []
        for i, allergen in enumerate(Allergies.allergens):
            if bool(score & 2**i):
                self.allergic_to.append(allergen)

    def is_allergic_to(self, item):
        if item in self.allergic_to:
            return True
        return False

    @property
    def lst(self):
        return self.allergic_to
