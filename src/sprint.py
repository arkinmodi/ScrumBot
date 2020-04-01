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
        seq = self.tasks.to_seq()
        for i, j in seq:
            j = self.__get_task(j)

        return seq

    def get_task(self, index):
        seq = self.get_tasks()
        for i, j in seq:
            if (i == index):
                return j
        return None

    ## @brief Mutator for adding task to list
    #  @param name Name of task to be added
    #  @param deadline Deadline of task to be added
    #  @param details Details of task to be added
    def add_task(self, name, deadline, details=None):
        task = Task(name, deadline, details)
        self.tasks.add(task)

    ## @brief Mutator for removing task from list
    #  @param n Key-value of task to be removed
    def rm_task(self, n):
        self.tasks.remove(n)

    ## @brief Mutator for adding feedback to a task
    #  @param index Index of task
    #  @param feedback Feedback to be added
    def add_feedback(self, index, feedback):
        task = self.__get_task_by_id(index)
        if (not task):
            raise KeyError
        
        task.add_feedback(feedback)

    def get_feedback(self, index):
        task = self.__get_task_by_id(index)
        if (not task):
            raise KeyError

        task.get_feedback()

    ## @brief Mutator for removing feedback from a task
    #  @param task_index Index of task
    #  @param feedback_index Index of feedback to be removed
    def rm_feedback(self, task_index, feedback_index):
        task = self.__get_task_by_id(task_index)
        if (not task):
            raise KeyError

        task.rm_feedback(feedback_index)

    ## @brief Mutator for setting the details of a task
    #  @param index Index of task
    #  @param details Details of task
    def set_details(self, index, details):
        task = self.__get_task_by_id(index)
        if (not task):
            raise KeyError

        task.set_details(details)

    def __get_task(self, task):
        return (task.get_name(), task.get_deadline(), task.get_details(), task.get_feedback())

    def __get_task_by_id(self, id):
        for i, j in self.tasks.to_seq():
            if (id == i):
                return j
        return None

    
