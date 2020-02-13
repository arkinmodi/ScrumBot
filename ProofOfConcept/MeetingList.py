from Meeting import *

class MeetingList:
    def __init__():
        _meeting_list = {}
        _idCount = 0

    def add_meeting(meeting):
        MeetingList._meeting_list[self._idCount] = meeting
        MeetingList._idCount += 1
    
    def list_meetings():
        sorted_list = []
        for key in sorted(MeetingList._meeting_list.keys()) :
            meeting_str = "(" + str(key) + ")" + MeetingList._meeting_list[key].get_meeting_type() + " Meeting - " +  MeetingList._meeting_list[key].get_date_time()
            sorted_list.append(meeting_str)
        return sorted_list

    def remove_meeting(id):
        del MeetingList._meeting_list[id]

    # def set_description(self, id, desc):
    #     self._meeting_list[id].set_description(desc)

