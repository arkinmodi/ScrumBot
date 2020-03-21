## @file sprint.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Class representing Sprint objects
#  @date Mar 21, 2020

from task import *
from taskList import *

## @brief Class representing Sprint objects
class Sprint():

    ## @brief Constructor for Sprint object
    def __init__(self):
        tasks = TaskList()

    ## @brief Accessor for list of tasks
    def get_tasks(self):
        return self.tasks.to_seq()

    ## @brief Mutator for adding task to list
    #  @param task Task to be added
    def add_task(task):
        self.tasks.add(task)

    
    ## @brief Mutator for removing task from list
    #  @param n Key-value of task to be removed
    def rm_task(n):
        self.tasks.remove(n)

    
