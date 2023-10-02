from flasher import FlasherInterface
from pylink import Jlink


class FlasherJlink(FlasherInterface):
    """Interface to the pynrfprog tool from nordic."""

    def erase():
        pass

    def flash(hex_file):
        serial_no = '683508544'
        jlink = JLink()
        jlink.open(serial_no)
        jlink.connect('device', verbose=True)
        jlink.flash(hex_file, 0x0)
        jlink.reset()
