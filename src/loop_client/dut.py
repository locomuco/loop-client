import json

class Dut(object):
    """ Device under Test (DUT) class."""

    def __init__(self, config: dict):
        self.mcus = config["dut_mcus"]
        pass

    def run_action(self, action: str):
        print("Running action: {}".format(action))
        pass


