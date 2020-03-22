## @file meetingTypes.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Class with enumeration of meeting types
#  @date Mar 17, 2020

from enum import Enum, auto

## @brief Class containing enumeration of meeting types
class MeetingTypes():
        GROOMING = auto()
        STANDUP = auto()
        RETROSPECTIVE = auto()
        SPRINTPLANNING = auto()
