"""Zomboid RCON: https://github.com/jmwhitworth/zomboid_rcon"""

import warnings

from .BaseRconClient import BaseRconClient
from .CommandResult import CommandResult
from .ZomboidRcon import ZomboidRcon


class ZomboidRCON(ZomboidRcon):
    """Deprecated alias for ZomboidRcon. Use ZomboidRcon instead."""

    def __init__(self, *args, **kwargs):
        warnings.warn(
            "ZomboidRCON is deprecated; use ZomboidRcon instead. "
            "Note: method signatures have changed in 2.0.0 (e.g. addvehicle now requires vehicle and user).",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(*args, **kwargs)


__title__ = "zomboid_rcon"
__version__ = "2.2.0"
