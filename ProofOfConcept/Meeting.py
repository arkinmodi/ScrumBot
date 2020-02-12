from datetime import datetime

class Meeting:
    
    def __init__(self, date: str, time: str, description: str) -> None:
        date = list(map(int, date.split('/')))
        time = list(map(int, time.split(':')))
        self.__dateTime = datetime(date[2], date[0], date[1], time[0], time[1])
        self.__description = description

    def getDateTime(self) -> str:
        return self.__dateTime.strftime("Meeting at: %b %d, %Y at %I:%M%p")

    def getDescription(self) -> str:
        return self.__description