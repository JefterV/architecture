# EXTERNAL IMPORTS

# NATIVE IMPORTS
from enum import IntEnum, auto

# INTERNAL IMPORTS


class UserStatusEnum(IntEnum):
    active = auto()
    disabled = auto()
    blocked = auto()
