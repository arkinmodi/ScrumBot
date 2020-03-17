## @file task.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A class representing tasks during the software development cycle
#  @date Mar 17, 2020

## @brief Class representing tasks
#  @details Class representing tasks with fields name, deadline, details and feedback
class Task():

    ## @brief Constructor for Task object
    def __init__(self, s, dt):
        self.name = s
        self.deadline = dt
        self.details = None
        self.feedback = []

    ## @brief Constructor for Task object
    def __init__(self, s, dt, d):
        self.name = s
        self.deadline = dt
        self.details = d
        self.feedback = []

    ## @brief Accessor for deadline of task
    def get_deadline(self):
        return self.deadline

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
    def add_feedback(self, s):
        return self.feedback.append(s)

     ## @brief Mutator for removing feedback from task
    def rm_feedback(self, s):
        return self.feedback.remove(s)

     ## @brief Mutator for setting details of a task
    def set_details(self, s):
        self.details = s

    

    