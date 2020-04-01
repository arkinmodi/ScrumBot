## @file meetingTypes.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Class with enumeration of meeting types
#  @date Mar 17, 2020

from enum import Enum, auto

## @brief Class containing enumeration of meeting types
class MeetingTypes(Enum):
    GROOMING = auto()
    STANDUP = auto()
    RETROSPECTIVE = auto()
    SPRINTPLANNING = auto()

    @staticmethod
    def from_str(label):
        if label in ('GROOMING', 'grooming'):
            return MeetingTypes.GROOMING
        elif label in ('STANDUP', 'standup'):
            return MeetingTypes.STANDUP
        elif label in ('RETROSPECTIVE', 'retrospective'):
            return MeetingTypes.RETROSPECTIVE
        elif label in ('SPRINTPLANNING', 'sprintplanning'):
            return MeetingTypes.SPRINTPLANNING
        else:
            raise NotImplementedError

    @staticmethod
    def to_str(label):
        return label.name
