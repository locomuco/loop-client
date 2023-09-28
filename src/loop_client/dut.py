import json

class Dut(object):
    """ Device under Test (DUT) class."""

    def __init__(self, config: dict):
        self.mcus = config["dut_mcus"]
        pass

    def flash(self, fw: str) -> None:
        """Flash the DUT with the given firmware."""
        pass


