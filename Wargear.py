"""
This sets up all the Wargear.
the switcher function needs replacing with a switchcase, based on a bastardised dictionary
"""

from Types import wargear


class Wargear:

    def StormShield(self):
        stormshield = Wargear()
        stormshield.modifier = ["I4","A1"]
        stormshield.name = "Storm Shield"
        stormshield.points = 15
        stormshield.power = 1
        return (stormshield)

    def smokelaunchers(self):
        smokelaunchers = Wargear()
        smokelaunchers.modifier=["SL"]
        smokelaunchers.points = 0
        smokelaunchers.power = 0
        return (smokelaunchers)



