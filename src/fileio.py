## @file fileio.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief Handles the file read/write between bot savestates
#  @date Apr 1, 2020

from project import *
from projectList import ProjectList
import datetime as dt
import glob, os

## @brief Class that handles file read/write between bot savestates
class fileio():
    PATH = os.path.dirname(sys.argv[0]) + "/data/"

    @staticmethod
    def read():
        project_list = ProjectList()
        if (len([name for name in os.listdir(fileio.PATH)]) == 0):
            return project_list
        
        read_path = fileio.PATH + "*.txt"
        for filepath in glob.iglob(read_path):
            with open(filepath, "r") as f:
                data = f.read().splitlines()

            # Line 0 is project information
            p_data = data[0].split(',')
            if (p_data[2] == "None"):
                proj = Project(p_data[1])
            else:
                proj = Project(p_data[1], p_data[2])
            project_list.update(int(p_data[0]), proj)

            # Project requirements
            if (len(p_data) > 3):
                for i in range(3, len(p_data)):
                    proj.add_rqe(p_data[i])

            # From ~meetings to the line prior to first '&' relates to meetings
            counter = 2
            for i, line in enumerate(data[2:]):
                if (line[0] == '&'):
                    counter += i
                    break
                m_data = line.split(',')
                if (m_data[3] == "None"):
                    proj.update_meeting(int(m_data[0]), m_data[1], m_data[2])
                else:
                    proj.update_meeting(int(m_data[0]), m_data[1], m_data[2], m_data[3])
                
                # Meeting description
                if (len(m_data) == 5):
                    proj.set_meeting_desc(i, m_data[4])

            # Each & represents a sprint, with terms in between meaning tasks
            for i, line in enumerate(data[counter:]):
                # Sprint
                if (line[0] == '&'):
                    date = line[0][1:].replace('-','/')
                    proj.add_sprint_from_file(date)
                else:
                # Task
                    t_data = line.split(',')
                    if (t_data[3] == "None"):
                        proj.add_task_from_file(int(t_data[0]), t_data[1], t_data[2])
                    else:
                        proj.add_task_from_file(int(t_data[0]), t_data[1], t_data[2], t_data[3])

                    # Feedback
                    if (len(t_data) > 4):
                        for i in range(4, len(t_data)):
                            proj.add_feedback(int(t_data[0]), t_data[i])
        
        return project_list
        
            


            

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