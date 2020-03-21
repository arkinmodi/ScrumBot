## @file meeting.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Class representing Meeting objects
#  @date Mar 21, 2020

from meetingTypes import *

## @brief Meeting class
class Meeting():

    ## @brief Meeting constructor (no description)
    #  @param n Name of meeting
    #  @param d Date of meeting
    #  @param t Time of meeting
    #  @param mType Type of meeting
    def __init__(self, n, d, t, mType):
        self.name = n
        self.date = d
        self.time = t
        self.mType = mType
        self.desc = None

    ## @brief Meeting constructor (with description)
    #  @param n Name of meeting
    #  @param d Date of meeting
    #  @param t Time of meeting
    #  @param mType Type of meeting
    #  @param desc Descripton of meeting
    def __init__(self, n, d, t, mType, desc):
        self.name = n
        self.date = d
        self.time = t
        self.mType = mType
        self.desc = desc

    ## @brief Accessor for name of meeting
    def get_name(self):
        return self.name

    ## @brief Accessor for date of meeting
    def get_date(self):
        return self.date

    ## @brief Accessor for time of meeting
    def get_time(self):
        return self.time

    ## @brief Accessor for type of meeting
    def get_type(self):
        return self.mType

    ## @brief Accessor for description of meeting
    def get_desc(self):
        return self.desc

    ## @brief Mutator for descripton of meeting
    #  @param s New description for meeting
    def set_desc(self, s):
        self.desc = s