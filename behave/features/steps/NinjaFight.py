class NinjaFight(object):
    """
    Domain model for ninja fights.
    """

    def __init__(self, with_ninja_level=None): # constructor takes one argument, if not provided set to none
        self.with_ninja_level = with_ninja_level
        self.opponent = None

    def decision(self):
        """
        Business logic how a Ninja should react to increase his survival rate.
        """
        assert self.with_ninja_level is not None
        assert self.opponent is not None
        if self.opponent == "Red Ninja":
            return "run for his life"
        if "black-belt" in self.with_ninja_level:
            return "engage the opponent"
        else:
            return "run for his life"