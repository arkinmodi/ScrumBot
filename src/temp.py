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

if __name__== "__main__":
  main()

