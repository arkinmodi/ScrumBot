from Meeting import *

while True:
    command = input()


    if (command == ''):
        print("Goodbye"); break
    elif (command[0] == "!"):
        if ("addMeeting" in command):
            # !addMeeting 02/15/2020 12:30 Sprint Meeting
            command = command.split(' ')
            date = command[1]
            time = command[2]
            desc = ' '.join(command[3:])

            meeting = Meeting(date, time, desc)

            print(meeting.getDateTime())
            print(meeting.getDescription())
