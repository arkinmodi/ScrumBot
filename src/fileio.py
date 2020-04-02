## @file fileio.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Handles the file read/write between bot savestates
#  @date Apr 1, 2020

from project import *
import glob, os

class fileio():
    PATH = os.path.dirname(sys.argv[0]) + "/data/"

    @staticmethod
    def read():
        read_path = fileio.PATH + "*.txt"
        
        for filepath in glob.iglob(read_path):
            print(filepath)
            

    @staticmethod
    def write(project_id, task, *info):
        write_path = fileio.PATH + str(project_id) + ".txt"
        with open(write_path, "r") as f:
            data = f.read().splitlines()

        # info is a requirement as a string
        if (task == "addRqe"):
            data[0] = data[0] + "," + info[0]

        # info is requirement id
        elif (task == "rmRqe"):
            line = data[0].split(',')
            line.pop(info[0] + 3)
            data[0] = ','.join(line)

        # info is new description
        elif (task == "setProjectDesc"):
            line = data[0].split(",")
            line[2] = info[0]
            data[0] = ','.join(line)

        # info is meeting info (id, name, datetime, meeting type, and optional description)
        elif (task == "addMeeting"):
            for i in range(len(data)):
                if (data[i][0] == '&'):
                    data.insert(i, info[0])
                    continue
            data.append(info[0])

        # info is meeting id
        elif (task == "rmMeeting"):
            for i in range(1, len(data)):
                if (data[i][0] == str(info[0])):
                    data.pop(i)
                    continue
                if (data[i][0] == '&'):
                    continue
            
        elif (task == "setMeetingDesc"):
            return
        elif (task == "addSprint"):
            return
        elif (task == "rmLastSprint"):
            return
        elif (task == "addTask"):
            return
        elif (task == "rmTask"):
            return
        elif (task == "setDetails"):
            return
        elif (task == "addFeedback"):
            return
        elif (task == "rmFeedback"):
            return
        
        print(data)
        # overwrite file
        with open(write_path, "w") as f:
            for i in data:
                f.write(i + "\n")
            

    @staticmethod
    def create(id, name, description):
        write_path = fileio.PATH + str(id) + ".txt"
        with open(write_path, "w") as f:
            f.write(f'{id},{name},{description}\n')
            f.write("~meetings\n")

    @staticmethod
    def delete(id):
        delete_path = fileio.PATH + str(id) + ".txt"
        os.remove(delete_path)