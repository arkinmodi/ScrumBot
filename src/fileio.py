## @file fileio.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Handles the file read/write between bot savestates
#  @date Apr 1, 2020

from project import *
import datetime as dt
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
            flag = True
            for i in range(len(data)):
                if (data[i][0] == '&'):
                    data.insert(i, info[0])
                    flag = False
                    break
            if (flag):
                data.append(info[0])

        # info is meeting id
        elif (task == "rmMeeting"):
            for i in range(2, len(data)):
                if (data[i][0] == str(info[0])):
                    data.pop(i)
                    break
                if (data[i][0] == '&'):
                    break
            
        # info is meeting id and meeting desc
        elif (task == "setMeetingDesc"):
            for i in range(2, len(data)):
                if (data[i][0] == str(info[0])):
                    temp = data[i].split(',')
                    temp[4] = info[1]
                    data[i] = ','.join(temp)
                    break
                if (data[i][0] == '&'):
                    break

        # info is None
        elif (task == "addSprint"):
            data.append(f'&{dt.date.today()}')

        # info is None
        elif (task == "rmLastSprint"):
            while (data[-1][0] != '&'):
                data.pop()
            data.pop()

        # info is task id, name, deadline, details
        elif (task == "addTask"):
            temp = f'{info[0]},{info[1]},{info[2]},{info[3]}'
            data.append(temp)

        # info is task id
        elif (task == "rmTask"):
            temp = data[::-1]
            for i in range(len(temp)):
                if (temp[i][0] == str(info[0])):
                    temp.pop(i)
                    break
                if (temp[i][0] == '&'):
                    break
            data = temp[::-1]
            
        # task is task id, details
        elif (task == "setDetails"):
            temp = data[::-1]
            for i in range(len(temp)):
                if (temp[i][0] == str(info[0])):
                    str_temp = temp[i].split(',')
                    str_temp[3] = info[1]
                    temp[i] = ','.join(str_temp)
                    break
                if (temp[i][0] == '&'):
                    break
            data = temp[::-1]

        # task is task id, feedback
        elif (task == "addFeedback"):
            temp = data[::-1]
            for i in range(len(temp)):
                if (temp[i][0] == str(info[0])):
                    str_temp = temp[i].split(',')
                    str_temp.append(info[1])
                    temp[i] = ','.join(str_temp)
                    break
                if (temp[i][0] == '&'):
                    break
            data = temp[::-1]

        # task is task id, feedback id
        elif (task == "rmFeedback"):
            temp = data[::-1]
            for i in range(len(temp)):
                if (temp[i][0] == str(info[0])):
                    str_temp = temp[i].split(',')
                    str_temp.pop(info[1] + 4)
                    temp[i] = ','.join(str_temp)
                    break
                if (temp[i][0] == '&'):
                    break
            data = temp[::-1]
        
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