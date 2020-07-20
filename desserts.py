"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}


    def __init__(self, name, flavor, price):
      """Create a Cupcake object"""
      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = 0

      Cupcake.cache[self.name] = self


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    def add_stock(self, amount):
      """Add amount to the quantity"""

      self.qty += amount


    def sell(self, amount):
      """Subtract amount from quantity"""

      if self.qty == 0:
        print('Sorry, these cupcakes are sold out')

      if amount > self.qty:
        self.qty -= self.qty
      elif amount < self.qty:
        self.qty -= amount


    @staticmethod
    def scale_recipe(ingredients, amount):
      """Returns list of tuples with each ingredient qty scaled by amount"""

      scaled_recipe = []

      for ingredient in ingredients:
        scaled_ingredient = (ingredient[0], ingredient[1] * amount)
        scaled_recipe.append(scaled_ingredient)

      return scaled_recipe

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')

    test_cupcake1 = Cupcake('Cupcake1', 'Lemon', 3)
    test_cupcake2 = Cupcake('Cupcake2', 'Strawberry', 4)


