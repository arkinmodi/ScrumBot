from task import *
from dict import Dict
from taskList import *
from sprint import *

def main():
    task1 = Task("task1", "2020-03-23", "details1")
    sprint1 = Sprint()
    print(sprint1.get_tasks())
    print("Flag 1")
    sprint1.add_task(task1)
    print(sprint1.get_tasks())
    print(sprint1.get_tasks()[0])
    print(sprint1.get_tasks()[0][1].get_name())
    print(sprint1.get_tasks()[0][1].get_feedback())
    print("Flag 2")
    sprint1.get_tasks()[0][1].add_feedback("feedback1")
    print(sprint1.get_tasks()[0][1].get_feedback())
    print("Flag 3")
    sprint1.get_tasks()[0][1].rm_feedback(0)
    print(sprint1.get_tasks()[0][1].get_feedback())


if __name__== "__main__":
  main()

