from Meeting import *
from MeetingList import *

print("Hello, I am ScrumBot!")
print("To add a meeting, use command !addMeeting DD/MM/YYYY HH:MM [Subject] [Meeting Type: SP, SU, R, G, Other]")
print("e.g. !addMeeting 02/15/2020 12:30 SP")

list_of_meetings = MeetingList() # list of meetings

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
            meeting_type = ' '.join(command[3:])

            meeting = Meeting(date, time, meeting_type)
            list_of_meetings.add_meeting(meeting)
            print(list_of_meetings.list_meetings())
            
            # print(meeting.get_date_time())
            # print(meeting.get_meeting_type())

        if ("setDescription" in command):
            command = command.split(' ')
            desc = ("").join(command[1:])
            meeting.set_description(desc)
            print(meeting.get_description())

