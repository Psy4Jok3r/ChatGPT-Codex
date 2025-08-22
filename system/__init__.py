from enum import Enum

class SystemState(Enum):
    WAKE = "wake"
    REST = "rest"
    OVERWHELMED = "overwhelmed"
    DREAM = "dream"
    REFLECT = "reflect"
    FOCUS = "focus"
