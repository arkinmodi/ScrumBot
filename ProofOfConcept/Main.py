from Meeting import *

print("Hello, I am ScrumBot!")
print("To add a meeting, use command !addMeeting DD/MM/YYYY HH:MM [Meeting Type: SP, SU, R, G, Other]")
print("e.g. !addMeeting 02/15/2020 12:30 SP")
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

            print(meeting.get_date_time())
            print(meeting.get_meeting_type())
