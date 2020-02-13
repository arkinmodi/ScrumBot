from Meeting import *

class MeetingList:
    def __init__(self):
        self._meeting_list = {}
        self._idCount = 0

    def add_meeting(self, meeting):
        self._meeting_list[self._idCount] = Meeting
    
    def list_meetings(self):
        sortedList = []
        for key in sorted(self._meeting_list.keys()) :
            meeting_str = "(" + str(key) + ")" + self._meeting_list[key].get_meeting_type() + " Meeting - " +  self._meeting_list[key].get_date_time()
            sortedList.push()
        return sortedList
