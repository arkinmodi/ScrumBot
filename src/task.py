## @file task.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A class representing tasks during the software development cycle
#  @date Mar 17, 2020

from datetime import *

## @brief Class representing task object
#  @details Class representing tasks with fields name, deadline, details and feedback
class Task():

    ## @brief Constructor for Task object
    #  @param s Name of task
    #  @param dt Date and time representing the deadline of task
    #  @param d Details of task
    def __init__(self, s, dt, d=None):
        self.name = s

        dt = dt.replace(' ', ':')
        dt = dt.replace(':', '/')
        dl = [int(i) for i in dt.split('/')]
        self.deadline = datetime(dl[0], dl[1], dl[2], dl[3], dl[4])
        self.details = d
        self.feedback = []

    ## @brief Accessor for name of task
    def get_name(self):
        return self.name

    ## @brief Accessor for deadline of task
    def get_deadline(self):
        return self.deadline.strftime("%b %d, %Y at %I:%M %p")

    ## @brief Accessor for details of task
    def get_details(self):
        if (self.details == None):
            return "No details"
        else:
            return self.details

     ## @brief Accessor for feedback of task
    def get_feedback(self):
        return self.feedback

     ## @brief Mutator for adding new feedback to task
     #  @param s The new feedback to be added to task
    def add_feedback(self, s):
        self.feedback.append(s)

     ## @brief Mutator for removing feedback from task
     #  @param i Index for feedback
    def rm_feedback(self, i):
        # return self.feedback.remove(s)
        self.feedback.pop(i) #if remove by index instead?

     ## @brief Mutator for setting details of a task
     #  @param s Details of task
    def set_details(self, s):
        self.details = s

    

    