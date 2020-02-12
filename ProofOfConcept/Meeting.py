from datetime import datetime

class Meeting:
    
    def __init__(self, date: str, time: str, meeting_type: str) -> None:
        date = list(map(int, date.split('/')))
        time = list(map(int, time.split(':')))
        self._date_time = datetime(date[2], date[0], date[1], time[0], time[1])
        self._meeting_type = meeting_type
        print self._date_time.strftime("(" + self._meeting_type + ")" + " Meeting at: %b %d, %Y at %I:%M%p"))

    def get_date_time(self) -> str:
        return self._date_time.strftime("Meeting at: %b %d, %Y at %I:%M%p")

    def get_meeting_type(self) -> str:
        return ("Type: " + self._meeting_type)