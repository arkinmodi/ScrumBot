## @file project.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Class representing Project objects
#  @date Mar 21, 2020

from meetingTypes import *
from meetingList import MeetingList
from task import *
from taskList import *
from sprint import *

## @brief Class representing Project objects
class Project():

    ## @brief Project constructor (no description)
    #  @param n Name of project
    def __init__(self, n):
        self.name = n
        self.desc = None
        self.meetings = MeetingList()
        self.rqes = []
        self.sprints = []
        self.c = 0

    ## @brief Prject constructor (with description)
    #  @param n Name of project
    #  @param d Descripton of project
    def __init__(self, n, d):
        self.name = n
        self.desc = d
        self.meetings = MeetingList()
        self.rqes = []
        self.sprints = []
        self.c = 0

    ## @brief Accessor for description of project
    def get_desc(self):
        if (self.desc == None):
            return "No description"
        else:
            return self.desc

    ## @brief Accessor for meetings of project
    def get_meetings(self):
        return self.meetings.to_seq()

    ## @brief Accessor for requirements of project
    def get_rqes(self):
        return self.rqes

    ## @brief Accessor for sprints of project
    def get_sprints(self):
        return self.sprints

    ## @brief Mutator for descripton of project
    #  @param s New description for project
    def set_desc(self, s):
        self.desc = s

    ## @brief Mutator for adding meeting to project
    #  @param meeting Meeting to be added
    def add_meeting(self, meeting):
        self.meetings.add(meeting)

    ## @brief Mutator for adding a requirement to project
    #  @param s Requirement to be added
    def add_rqe(self, s):
        self.rqes.append(s)


    ## @brief Mutator for adding a sprint to project
    #  @param sprint Sprint to be added
    def add_sprint(self, sprint):
        self.sprints.append(sprint)
        self.c = self.c + 1

    ## @brief Mutator for removing a meeting from project
    #  @param n Key-value of project to be removed
    def rm_meeting(self, n):
        self.meetings.remove(n)

    ## @brief Mutator for removing a requirement from project
    #  @param n Index of requirement to be removed
    def rm_rqe(self, n):
        self.rqes.pop(n)

    ## @brief Mutator for removing a sprint from project
    def rm_sprint(self):
        if (self.c==0):
            raise IndexError
        else:
            del self.sprints[-1]
            self.c = self.c - 1