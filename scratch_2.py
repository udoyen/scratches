class PartyAnimal:
    """PartyAnimal."""

    _x = 0
    name = ""
    def __init__(self, nam):
        """__init__.
        :param nam:
        """
        self.name = nam
        print(self.name, "constructed")

    def party(self) -> None:
        """party.
        :rtype: None
        """
        self._x = self._x + 1
        print(self.name, "party count", self._x)

    def night_party(self, venue: str) -> str:
        """night_party.
        :param venue:
        :type venue: str
        :rtype: str
        """
        self._x = self._x + 1
        print(self.name, "party count", self._x)
        return venue

m = PartyAnimal("koko")
m.party()