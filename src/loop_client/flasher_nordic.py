from flasher import FlasherInterface
from pynrfjprog import HighLevel


class FlasherNordic(FlasherInterface):
    """Interface to the pynrfprog tool from nordic."""

    def erase():
        pass

    def flash(hex_file):
        flasher_serial_number = self._id

        with HighLevel.API() as api:
            snrs = api.get_connected_probes()
            if flasher_serial_number not in snrs:
                raise Exception(
                    "Flasher with serial number {} not found.".format(
                        flasher_serial_number
                    )
                )

        with HighLevel.API() as api:
            with HighLevel.DebugProbe(api, snrs[0]) as probe:
                probe.program(hex_file)
