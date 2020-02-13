from Meeting import *

class MeetingList:
    def init():
        MeetingList._meeting_list = {}
        MeetingList._idCount = 0

    def add_meeting(date: str, time: str, meeting_type: str):
        MeetingList._meeting_list[MeetingList._idCount] = Meeting(date, time, meeting_type)
        MeetingList._idCount += 1
        return(MeetingList._idCount - 1)

    def get_meeting_datetime(id: int):
        return MeetingList._meeting_list[id].get_date_time()
    
    def list_meetings():
        sorted_list = []
        for key in sorted(MeetingList._meeting_list.keys()) :
            meeting_str = "ID: " + str(key) + " | Type: " + MeetingList._meeting_list[key].get_meeting_type() + " | Date: " +  MeetingList._meeting_list[key].get_date_time()
            sorted_list.append(meeting_str)
        return sorted_list

    def remove_meeting(id):
        del MeetingList._meeting_list[id]

    # def set_description(self, id, desc):
    #     self._meeting_list[id].set_description(desc)

