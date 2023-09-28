import abc
from pathlib import Path

def FlasherInterface(object):
    """Interface for flasher classes."""

    def __init__(self, id: str):
        """
        Combined Test device
        """
        self._id = id

    @abc.abstractmethod
    def erase(self) -> None:
        """Erase the device."""
        pass

    @abc.abstractmethod
    def flash(self, hex_file: Path) -> None:
        """Write FW to device."""
        pass
