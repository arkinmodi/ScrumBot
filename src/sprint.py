## @file sprint.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Class representing Sprint objects
#  @date Mar 21, 2020

from task import *
from taskList import *
import datetime as dt

## @brief Class representing Sprint objects
class Sprint():

    ## @brief Constructor for Sprint object
    def __init__(self):
        self.tasks = TaskList()
        self.date = dt.date.today()

    ## @brief Accessor for date of sprint
    def get_date(self):
        return self.date.strftime("%b %d, %Y")

    ## @brief Accessor for list of tasks
    def get_tasks(self):
        return self.tasks.to_seq()

    ## @brief Mutator for adding task to list
    #  @param task Task to be added
    def add_task(self, task):
        self.tasks.add(task)

    ## @brief Mutator for updating task
    #  @param id ID of task to be updated
    #  @param e Value of task to be updated
    def update_task(self, id, e):
        self.tasks.update(id, e)

    ## @brief Mutator for removing task from list
    #  @param n Key-value of task to be removed
    def rm_task(self, n):
        self.tasks.remove(n)

    
