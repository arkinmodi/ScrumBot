## @file meeting.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Class representing Meeting objects
#  @date Mar 21, 2020

from meetingTypes import *
from datetime import *

## @brief Meeting class
class Meeting():

    ## @brief Meeting constructor
    #  @param n Name of meeting
    #  @param dt Date and time of meeting
    #  @param m_type Type of meeting
    #  @param desc Descripton of meeting
    def __init__(self, n, dt, m_type, desc=None):
        self.name = n

        dt = dt.replace(' ', ':')
        dt = dt.replace(':', '/')
        d = [int(i) for i in dt.split('/')]
        self.datetime = datetime(d[0], d[1], d[2], d[3], d[4])
        self.m_type = MeetingTypes.from_str(m_type)
        self.desc = desc

    ## @brief Accessor for name of meeting
    def get_name(self):
        return self.name

    ## @brief Accessor for date of meeting
    def get_datetime(self):
        return self.datetime.strftime("%b %d, %Y at %I:%M %p")

    ## @brief Accessor for type of meeting
    def get_type(self):
        return MeetingTypes.to_str(self.m_type)

    ## @brief Accessor for description of meeting
    def get_desc(self):
        if (self.desc == None):
            return "No description"
        else:
            return self.desc

    ## @brief Mutator for descripton of meeting
    #  @param s New description for meeting
    def set_desc(self, s):
        self.desc = s